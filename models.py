from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Ong(UserMixin, db.Model):
    """Modelo para representar uma ONG de resgate de animais ou Pessoa Física"""
    
    id = db.Column(db.Integer, primary_key=True)
    tipo_pessoa = db.Column(db.String(2), nullable=False, default='PJ')  # 'PF' ou 'PJ'
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=True)  # Pode ser CPF ou CNPJ
    cpf = db.Column(db.String(14), unique=True, nullable=True)  # Para pessoa física
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    endereco = db.Column(db.String(200))
    cidade = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    telefone = db.Column(db.String(15))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamento com pets
    pets = db.relationship('Pet', backref='ong', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Ong {self.nome}>'
    
    def set_password(self, password):
        """Define a senha da ONG com hash"""
        self.senha_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.senha_hash, password)
    
    def to_dict(self):
        """Converte o objeto ONG para dicionário"""
        return {
            'id': self.id,
            'tipo_pessoa': self.tipo_pessoa,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'cpf': self.cpf,
            'email': self.email,
            'endereco': self.endereco,
            'cidade': self.cidade,
            'cep': self.cep,
            'telefone': self.telefone,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None
        }
    
    def get_documento(self):
        """Retorna o documento (CPF ou CNPJ) formatado"""
        return self.cpf if self.tipo_pessoa == 'PF' else self.cnpj

class Pet(db.Model):
    """Modelo para representar um pet disponível para adoção"""
    
    # Opções para os campos de escolha
    ESPECIES = ['Cachorro', 'Gato']
    IDADES = ['Filhote', 'Adulto']
    PORTES = ['Pequeno', 'Médio', 'Grande']
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.String(20), nullable=False)
    porte = db.Column(db.String(20))
    descricao = db.Column(db.Text)
    foto_url = db.Column(db.String(200))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    adotado = db.Column(db.Boolean, default=False)
    
    # Chave estrangeira para ONG
    ong_id = db.Column(db.Integer, db.ForeignKey('ong.id'), nullable=False)
    
    def __repr__(self):
        return f'<Pet {self.nome} - {self.especie}>'
    
    def to_dict(self):
        """Converte o objeto Pet para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'especie': self.especie,
            'idade': self.idade,
            'porte': self.porte,
            'descricao': self.descricao,
            'foto_url': self.foto_url,
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None,
            'adotado': self.adotado,
            'ong_id': self.ong_id,
            'ong_nome': self.ong.nome if self.ong else None,
            'ong_cidade': self.ong.cidade if self.ong else None,
            'ong_telefone': self.ong.telefone if self.ong else None
        }
    
    @staticmethod
    def get_especies():
        """Retorna lista de espécies disponíveis"""
        return Pet.ESPECIES
    
    @staticmethod
    def get_idades():
        """Retorna lista de idades disponíveis"""
        return Pet.IDADES
    
    @staticmethod
    def get_portes():
        """Retorna lista de portes disponíveis"""
        return Pet.PORTES
