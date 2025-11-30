#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para popular o banco de dados com dados de exemplo
"""

from app import app
from models import db, Ong, Pet
from werkzeug.security import generate_password_hash

def criar_dados_exemplo():
    """Cria ONGs e pets de exemplo"""
    
    with app.app_context():
        # Limpar dados existentes
        print("Limpando dados existentes...")
        db.drop_all()
        db.create_all()
        
        # Criar ONGs de exemplo
        print("Criando ONGs de exemplo...")
        
        ongs_exemplo = [
            {
                'tipo_pessoa': 'PJ',
                'nome': 'Patas do Bem',
                'cnpj': '12345678000195',
                'cpf': None,
                'email': 'contato@patasdobem.org.br',
                'senha': 'senha123',
                'endereco': 'Rua das Flores, 123',
                'cidade': 'São Paulo',
                'cep': '01234567',
                'telefone': '(11) 99999-1111',
                'latitude': -23.5505,
                'longitude': -46.6333
            },
            {
                'tipo_pessoa': 'PJ',
                'nome': 'Amigos dos Bichos',
                'cnpj': '98765432000187',
                'cpf': None,
                'email': 'info@amigosdosbichos.com.br',
                'senha': 'senha123',
                'endereco': 'Av. Paulista, 1000',
                'cidade': 'São Paulo',
                'cep': '01310100',
                'telefone': '(11) 88888-2222',
                'latitude': -23.5613,
                'longitude': -46.6565
            },
            {
                'tipo_pessoa': 'PF',
                'nome': 'Maria Silva',
                'cnpj': None,
                'cpf': '12345678901',
                'email': 'maria@email.com',
                'senha': 'senha123',
                'endereco': 'Rua das Acácias, 300',
                'cidade': 'São Paulo',
                'cep': '01330000',
                'telefone': '(11) 97777-5555',
                'latitude': -23.5500,
                'longitude': -46.6400
            },
            {
                'tipo_pessoa': 'PJ',
                'nome': 'Casa dos Gatos',
                'cnpj': '11111111000111',
                'cpf': None,
                'email': 'contato@casadosgatos.org',
                'senha': 'senha123',
                'endereco': 'Rua dos Gatos, 456',
                'cidade': 'Rio de Janeiro',
                'cep': '20000000',
                'telefone': '(21) 77777-3333',
                'latitude': -22.9068,
                'longitude': -43.1729
            },
            {
                'tipo_pessoa': 'PF',
                'nome': 'João Santos',
                'cnpj': None,
                'cpf': '98765432109',
                'email': 'joao@email.com',
                'senha': 'senha123',
                'endereco': 'Av. Atlântica, 500',
                'cidade': 'Rio de Janeiro',
                'cep': '22070000',
                'telefone': '(21) 96666-7777',
                'latitude': -22.9700,
                'longitude': -43.1800
            },
            {
                'tipo_pessoa': 'PJ',
                'nome': 'Refúgio Animal',
                'cnpj': '22222222000222',
                'cpf': None,
                'email': 'refugio@animal.org.br',
                'senha': 'senha123',
                'endereco': 'Rua da Esperança, 789',
                'cidade': 'Belo Horizonte',
                'cep': '30000000',
                'telefone': '(31) 66666-4444',
                'latitude': -19.9167,
                'longitude': -43.9345
            },
            {
                'tipo_pessoa': 'PF',
                'nome': 'Carlos Pereira',
                'cnpj': None,
                'cpf': '45678912345',
                'email': 'carlos@email.com',
                'senha': 'senha123',
                'endereco': 'Quadra 5 Conjunto A, 100',
                'cidade': 'Brasília - Sobradinho',
                'cep': '73040134',
                'telefone': '(61) 98888-9999',
                'latitude': -15.6528,
                'longitude': -47.7889
            },
            {
                'tipo_pessoa': 'PJ',
                'nome': 'Amigos Pets Ceará',
                'cnpj': '33333333000333',
                'cpf': None,
                'email': 'amigospets@ceara.com.br',
                'senha': 'senha123',
                'endereco': 'Rua das Palmeiras, 250',
                'cidade': 'Maracanau - CE',
                'cep': '61905120',
                'telefone': '(85) 99777-8888',
                'latitude': -3.8767,
                'longitude': -38.6256
            }
        ]
        
        ongs_criadas = []
        for ong_data in ongs_exemplo:
            ong = Ong(
                tipo_pessoa=ong_data['tipo_pessoa'],
                nome=ong_data['nome'],
                cnpj=ong_data['cnpj'],
                cpf=ong_data['cpf'],
                email=ong_data['email'],
                endereco=ong_data['endereco'],
                cidade=ong_data['cidade'],
                cep=ong_data['cep'],
                telefone=ong_data['telefone'],
                latitude=ong_data['latitude'],
                longitude=ong_data['longitude']
            )
            ong.set_password(ong_data['senha'])
            db.session.add(ong)
            ongs_criadas.append(ong)
        
        db.session.commit()
        print(f"[OK] {len(ongs_criadas)} ONGs criadas com sucesso!")
        
        # Criar pets de exemplo
        print("Criando pets de exemplo...")
        
        pets_exemplo = [
            # Patas do Bem
            {
                'nome': 'Mel',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Mel é uma cadela muito dócil e carinhosa. Foi resgatada das ruas e está procurando uma família amorosa. Adora brincar e é muito obediente.',
                'foto_url': 'https://images.unsplash.com/photo-1552053831-71594a27632d?w=400',
                'ong_index': 0
            },
            {
                'nome': 'Thor',
                'especie': 'Cachorro',
                'idade': 'Filhote',
                'porte': 'Grande',
                'descricao': 'Thor é um filhote muito brincalhão e energético. Precisa de uma família ativa que possa dar muito carinho e atenção.',
                'foto_url': 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400',
                'ong_index': 0
            },
            {
                'nome': 'Luna',
                'especie': 'Gato',
                'idade': 'Adulto',
                'porte': 'Pequeno',
                'descricao': 'Luna é uma gata muito tranquila e independente. Perfeita para quem busca um companheiro calmo e carinhoso.',
                'foto_url': 'https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=400',
                'ong_index': 0
            },
            
            # Amigos dos Bichos (PJ)
            {
                'nome': 'Rex',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Grande',
                'descricao': 'Rex é um cão muito protetor e leal. Ideal para famílias que buscam um guardião amoroso e confiável.',
                'foto_url': 'https://images.unsplash.com/photo-1547407139-3c921a71905c?w=400',
                'ong_index': 1
            },
            
            # Maria Silva (PF)
            {
                'nome': 'Frederico',
                'especie': 'Gato',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Frederico é um gato muito carinhoso. Precisa de uma nova família pois vou me mudar para o exterior.',
                'foto_url': 'https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8?w=400',
                'ong_index': 2
            },
            {
                'nome': 'Mimi',
                'especie': 'Gato',
                'idade': 'Filhote',
                'porte': 'Pequeno',
                'descricao': 'Mimi é uma gatinha muito fofa e brincalhona. Adora correr pela casa e brincar com brinquedos.',
                'foto_url': 'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400',
                'ong_index': 1
            },
            {
                'nome': 'Bolt',
                'especie': 'Cachorro',
                'idade': 'Filhote',
                'porte': 'Médio',
                'descricao': 'Bolt é um filhote muito esperto e rápido. Adora correr e brincar ao ar livre. Perfeito para famílias ativas.',
                'foto_url': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400',
                'ong_index': 1
            },
            
            # Casa dos Gatos (PJ)
            {
                'nome': 'Nala',
                'especie': 'Gato',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Nala é uma gata muito elegante e independente. Adora sonecas ao sol e carinhos suaves.',
                'foto_url': 'https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400',
                'ong_index': 3
            },
            {
                'nome': 'Simba',
                'especie': 'Gato',
                'idade': 'Filhote',
                'porte': 'Pequeno',
                'descricao': 'Simba é um gatinho muito brincalhão e curioso. Adora explorar e brincar com tudo que vê.',
                'foto_url': 'https://images.unsplash.com/photo-1596854407944-bf87f6fdd49e?w=400',
                'ong_index': 3
            },
            
            # João Santos (PF)
            {
                'nome': 'Princesa',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Pequeno',
                'descricao': 'Princesa é uma cadela muito educada e carinhosa. Infelizmente não posso mais cuidar dela.',
                'foto_url': 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400',
                'ong_index': 4
            },
            
            # Refúgio Animal (PJ - Belo Horizonte)
            {
                'nome': 'Max',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Max é um cão muito inteligente e treinado. Conhece vários comandos e é muito obediente.',
                'foto_url': 'https://images.unsplash.com/photo-1551717743-49959800b1f6?w=400',
                'ong_index': 5
            },
            {
                'nome': 'Lola',
                'especie': 'Cachorro',
                'idade': 'Filhote',
                'porte': 'Pequeno',
                'descricao': 'Lola é uma cachorrinha muito fofa e carinhosa. Adora colo e atenção. Perfeita para apartamentos.',
                'foto_url': 'https://images.unsplash.com/photo-1591160690555-5debfba289f0?w=400',
                'ong_index': 5
            },
            {
                'nome': 'Zeus',
                'especie': 'Gato',
                'idade': 'Adulto',
                'porte': 'Grande',
                'descricao': 'Zeus é um gato imponente e majestoso. Muito tranquilo e independente, perfeito para quem busca um companheiro calmo.',
                'foto_url': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=400',
                'ong_index': 5
            },
            
            # Carlos Pereira (PF - Brasília Sobradinho)
            {
                'nome': 'Toby',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Toby é um cachorro super amigável e companheiro. Estou me mudando e infelizmente não posso levá-lo. Ele adora passear e é ótimo com crianças.',
                'foto_url': 'https://images.unsplash.com/photo-1558788353-f76d92427f16?w=400',
                'ong_index': 6
            },
            {
                'nome': 'Belinha',
                'especie': 'Cachorro',
                'idade': 'Filhote',
                'porte': 'Pequeno',
                'descricao': 'Belinha é uma filhotinha muito animada! Ela é super brincalhona e carinhosa. Ideal para quem quer um companheiro alegre.',
                'foto_url': 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400',
                'ong_index': 6
            },
            
            # Amigos Pets Ceará (PJ - Maracanau)
            {
                'nome': 'Caramelo',
                'especie': 'Cachorro',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Caramelo é um vira-lata brasileiro puro! Muito esperto, carinhoso e protetor. Resgatado das ruas e procurando um lar definitivo.',
                'foto_url': 'https://images.unsplash.com/photo-1477884213360-7e9d7dcc1e48?w=400',
                'ong_index': 7
            },
            {
                'nome': 'Nina',
                'especie': 'Gato',
                'idade': 'Filhote',
                'porte': 'Pequeno',
                'descricao': 'Nina é uma gatinha super fofa e curiosa. Adora brincar com bolinhas e explorar cada cantinho da casa. Muito carinhosa!',
                'foto_url': 'https://images.unsplash.com/photo-1606214174585-fe31582dc6ee?w=400',
                'ong_index': 7
            },
            {
                'nome': 'Branco',
                'especie': 'Gato',
                'idade': 'Adulto',
                'porte': 'Médio',
                'descricao': 'Branco é um gato branquinho lindo e muito tranquilo. Perfeito para quem busca um companheiro calmo e elegante.',
                'foto_url': 'https://images.unsplash.com/photo-1495360010541-f48722b34f7d?w=400',
                'ong_index': 7
            }
        ]
        
        pets_criados = []
        for pet_data in pets_exemplo:
            pet = Pet(
                nome=pet_data['nome'],
                especie=pet_data['especie'],
                idade=pet_data['idade'],
                porte=pet_data['porte'],
                descricao=pet_data['descricao'],
                foto_url=pet_data['foto_url'],
                ong_id=ongs_criadas[pet_data['ong_index']].id
            )
            db.session.add(pet)
            pets_criados.append(pet)
        
        db.session.commit()
        print(f"[OK] {len(pets_criados)} pets criados com sucesso!")
        
        print("\n" + "="*50)
        print("*** DADOS DE EXEMPLO CRIADOS COM SUCESSO! ***")
        print("="*50)
        print(f"RESUMO:")
        print(f"   - {len(ongs_criadas)} ONGs/Pessoas cadastradas")
        print(f"   - {len(pets_criados)} pets disponiveis para adocao")
        print("\nCREDENCIAIS DE LOGIN PARA TESTE:")
        print("\n   ONGs (Pessoa Juridica):")
        print("   - contato@patasdobem.org.br / senha123")
        print("   - info@amigosdosbichos.com.br / senha123")
        print("   - contato@casadosgatos.org / senha123")
        print("   - refugio@animal.org.br / senha123")
        print("   - amigospets@ceara.com.br / senha123")
        print("\n   Pessoas Fisicas:")
        print("   - maria@email.com / senha123")
        print("   - joao@email.com / senha123")
        print("   - carlos@email.com / senha123 (Brasilia-Sobradinho)")
        print("\nACESSE: http://localhost:5000")
        print("="*50)

if __name__ == '__main__':
    criar_dados_exemplo()
