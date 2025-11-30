from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import os

from models import db, Ong, Pet
from config import Config

# Inicialização da aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicialização das extensões
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'ong_login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'info'

# Configuração do geocoder
geolocator = Nominatim(user_agent="PetEncontraApp")

@login_manager.user_loader
def load_user(user_id):
    return Ong.query.get(int(user_id))

# Criação das tabelas do banco de dados
with app.app_context():
    db.create_all()

# ==================== ROTAS PRINCIPAIS ====================

@app.route('/')
def index():
    """Página inicial com galeria de pets e filtros"""
    # Parâmetros de filtro
    especie = request.args.get('especie', '')
    idade = request.args.get('idade', '')
    porte = request.args.get('porte', '')
    cep = request.args.get('cep', '')
    
    # Query base para pets não adotados
    query = Pet.query.filter_by(adotado=False)
    
    # Aplicar filtros de pet se fornecidos
    if especie:
        query = query.filter_by(especie=especie)
    if idade:
        query = query.filter_by(idade=idade)
    if porte:
        query = query.filter_by(porte=porte)
    
    # Filtro por CEP - busca pets de ONGs na região do CEP
    if cep:
        # Remove formatação do CEP
        cep_limpo = cep.replace('-', '').replace('.', '')
        
        # Buscar ONGs com CEP similar (mesma região - 5 primeiros dígitos)
        if len(cep_limpo) >= 5:
            # Pegar os 5 primeiros dígitos (região)
            cep_regiao = cep_limpo[:5]
            
            # Buscar ONGs que tenham CEP começando com esses dígitos
            ongs_regiao = Ong.query.filter(Ong.cep.like(f'{cep_regiao}%')).all()
            ongs_ids = [ong.id for ong in ongs_regiao]
            
            if ongs_ids:
                query = query.filter(Pet.ong_id.in_(ongs_ids))
            else:
                # Se não encontrou nenhuma ONG na região, retorna lista vazia
                query = query.filter(Pet.id == -1)
    
    pets = query.all()
    
    return render_template('index.html', 
                         pets=pets, 
                         especies=Pet.get_especies(),
                         idades=Pet.get_idades(),
                         portes=Pet.get_portes(),
                         filtro_especie=especie,
                         filtro_idade=idade,
                         filtro_porte=porte,
                         filtro_cep=cep)

@app.route('/api/pets-por-proximidade', methods=['POST'])
def pets_por_proximidade():
    """API para buscar pets por proximidade geográfica"""
    try:
        data = request.get_json()
        user_lat = data.get('latitude')
        user_lon = data.get('longitude')
        raio_km = data.get('raio', 50)  # Raio padrão de 50km
        
        if not user_lat or not user_lon:
            return jsonify({'error': 'Coordenadas não fornecidas'}), 400
        
        # Buscar todos os pets não adotados com suas ONGs
        pets = Pet.query.filter_by(adotado=False).all()
        pets_com_distancia = []
        
        for pet in pets:
            if pet.ong.latitude and pet.ong.longitude:
                # Calcular distância usando geopy
                ong_coords = (pet.ong.latitude, pet.ong.longitude)
                user_coords = (user_lat, user_lon)
                distancia = geodesic(user_coords, ong_coords).kilometers
                
                if distancia <= raio_km:
                    pet_dict = pet.to_dict()
                    pet_dict['distancia'] = round(distancia, 2)
                    pets_com_distancia.append(pet_dict)
        
        # Ordenar por distância (mais próximo primeiro)
        pets_com_distancia.sort(key=lambda x: x['distancia'])
        
        return jsonify({'pets': pets_com_distancia})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== ROTAS DAS ONGs ====================

@app.route('/ong/cadastro', methods=['GET', 'POST'])
def ong_cadastro():
    """Cadastro de nova ONG ou Pessoa Física"""
    if request.method == 'POST':
        try:
            # Coletar dados do formulário
            tipo_pessoa = request.form.get('tipo_pessoa', 'PJ')
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            endereco = request.form['endereco']
            cidade = request.form['cidade']
            cep = request.form['cep']
            telefone = request.form['telefone']
            
            # Verificar se email já existe
            if Ong.query.filter_by(email=email).first():
                flash('Email já cadastrado!', 'error')
                return render_template('ong_cadastro.html')
            
            # Processar documento conforme o tipo de pessoa
            cpf = None
            cnpj = None
            
            if tipo_pessoa == 'PF':
                cpf = request.form.get('cpf', '').replace('.', '').replace('-', '')
                if Ong.query.filter_by(cpf=cpf).first():
                    flash('CPF já cadastrado!', 'error')
                    return render_template('ong_cadastro.html')
            else:
                cnpj = request.form.get('cnpj', '').replace('.', '').replace('/', '').replace('-', '')
                if Ong.query.filter_by(cnpj=cnpj).first():
                    flash('CNPJ já cadastrado!', 'error')
                    return render_template('ong_cadastro.html')
            
            # Criar nova ONG ou Pessoa Física
            nova_ong = Ong(
                tipo_pessoa=tipo_pessoa,
                nome=nome,
                cpf=cpf,
                cnpj=cnpj,
                email=email,
                endereco=endereco,
                cidade=cidade,
                cep=cep,
                telefone=telefone
            )
            nova_ong.set_password(senha)
            
            # Tentar obter coordenadas do endereço
            try:
                endereco_completo = f"{endereco}, {cidade}"
                location = geolocator.geocode(endereco_completo, timeout=10)
                if location:
                    nova_ong.latitude = location.latitude
                    nova_ong.longitude = location.longitude
            except Exception as e:
                print(f"Erro ao obter coordenadas: {e}")
                # Continua sem coordenadas
            
            # Salvar no banco
            db.session.add(nova_ong)
            db.session.commit()
            
            tipo_texto = 'ONG' if tipo_pessoa == 'PJ' else 'Pessoa Física'
            flash(f'{tipo_texto} cadastrada com sucesso! Faça login para acessar o painel.', 'success')
            return redirect(url_for('ong_login'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar: {str(e)}', 'error')
    
    return render_template('ong_cadastro.html')

@app.route('/ong/login', methods=['GET', 'POST'])
def ong_login():
    """Login da ONG"""
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        ong = Ong.query.filter_by(email=email).first()
        
        if ong and ong.check_password(senha):
            login_user(ong)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('ong_painel'))
        else:
            flash('Email ou senha incorretos!', 'error')
    
    return render_template('ong_login.html')

@app.route('/ong/logout')
@login_required
def ong_logout():
    """Logout da ONG"""
    logout_user()
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('index'))

@app.route('/ong/painel')
@login_required
def ong_painel():
    """Painel da ONG para gerenciar pets"""
    pets = Pet.query.filter_by(ong_id=current_user.id).all()
    return render_template('ong_painel.html', pets=pets)

@app.route('/ong/adicionar-pet', methods=['GET', 'POST'])
@login_required
def adicionar_pet():
    """Adicionar novo pet"""
    if request.method == 'POST':
        try:
            novo_pet = Pet(
                nome=request.form['nome'],
                especie=request.form['especie'],
                idade=request.form['idade'],
                porte=request.form.get('porte'),
                descricao=request.form.get('descricao'),
                foto_url=request.form.get('foto_url'),
                ong_id=current_user.id
            )
            
            db.session.add(novo_pet)
            db.session.commit()
            
            flash('Pet cadastrado com sucesso!', 'success')
            return redirect(url_for('ong_painel'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar pet: {str(e)}', 'error')
    
    return render_template('adicionar_pet.html', 
                         especies=Pet.get_especies(),
                         idades=Pet.get_idades(),
                         portes=Pet.get_portes())

@app.route('/pet/<int:pet_id>')
def pet_detalhes(pet_id):
    """Página de detalhes de um pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_detalhes.html', pet=pet)

@app.route('/ong/editar-pet/<int:pet_id>', methods=['GET', 'POST'])
@login_required
def editar_pet(pet_id):
    """Editar pet existente"""
    pet = Pet.query.get_or_404(pet_id)
    
    # Verificar se o pet pertence à ONG logada
    if pet.ong_id != current_user.id:
        flash('Você não tem permissão para editar este pet!', 'error')
        return redirect(url_for('ong_painel'))
    
    if request.method == 'POST':
        try:
            pet.nome = request.form['nome']
            pet.especie = request.form['especie']
            pet.idade = request.form['idade']
            pet.porte = request.form.get('porte')
            pet.descricao = request.form.get('descricao')
            pet.foto_url = request.form.get('foto_url')
            
            db.session.commit()
            flash('Pet atualizado com sucesso!', 'success')
            return redirect(url_for('ong_painel'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar pet: {str(e)}', 'error')
    
    return render_template('editar_pet.html', 
                         pet=pet,
                         especies=Pet.get_especies(),
                         idades=Pet.get_idades(),
                         portes=Pet.get_portes())

@app.route('/ong/remover-pet/<int:pet_id>', methods=['POST'])
@login_required
def remover_pet(pet_id):
    """Remover pet"""
    pet = Pet.query.get_or_404(pet_id)
    
    # Verificar se o pet pertence à ONG logada
    if pet.ong_id != current_user.id:
        flash('Você não tem permissão para remover este pet!', 'error')
        return redirect(url_for('ong_painel'))
    
    try:
        db.session.delete(pet)
        db.session.commit()
        flash('Pet removido com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover pet: {str(e)}', 'error')
    
    return redirect(url_for('ong_painel'))

# ==================== HANDLERS DE ERRO ====================

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# ==================== INICIALIZAÇÃO ====================

if __name__ == '__main__':
    app.run(debug=True)
