# 🚀 Instruções de Instalação - PetEncontra

## Passo a Passo para Executar o Projeto

### 1. Instalar Dependências
Execute o seguinte comando no terminal (na pasta do projeto):
```bash
pip install -r requirements.txt
```

Se houver problemas de conexão, tente:
```bash
pip install --timeout 60 -r requirements.txt
```

Ou instale as dependências uma por uma:
```bash
pip install Flask==2.3.3
pip install Flask-SQLAlchemy==3.0.5
pip install Flask-Login==0.6.3
pip install Flask-WTF==1.1.1
pip install WTForms==3.0.1
pip install Werkzeug==2.3.7
pip install geopy==2.4.0
pip install python-dotenv==1.0.0
pip install email-validator==2.0.0
```

### 2. Configurar Variáveis de Ambiente
1. Copie o arquivo `env_example.txt` para `.env`
2. Edite o arquivo `.env` e configure sua chave secreta:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=minha_chave_secreta_muito_segura_123456
DATABASE_URL=sqlite:///petencontra.db
```

### 3. Executar a Aplicação
```bash
python app.py
```

### 4. Acessar no Navegador
Abra seu navegador e acesse: http://localhost:5000

## 🎯 Como Usar

### Para Testar o Sistema:

1. **Cadastrar uma ONG**:
   - Acesse "Cadastrar ONG" no menu
   - Preencha os dados da ONG
   - Faça login com email e senha

2. **Adicionar Pets**:
   - No painel da ONG, clique em "Adicionar Pet"
   - Preencha as informações do pet
   - Adicione uma foto (URL)

3. **Visualizar na Página Principal**:
   - Volte à página inicial
   - Veja os pets cadastrados
   - Teste os filtros

4. **Busca por Proximidade**:
   - Clique em "Encontrar pets perto de mim"
   - Permita acesso à localização
   - Veja pets ordenados por distância

## 🔧 Resolução de Problemas

### Erro de Conexão com PyPI
Se houver timeout na instalação:
```bash
pip install --timeout 120 --retries 3 -r requirements.txt
```

### Erro de Permissão
No Windows, execute como administrador ou use:
```bash
pip install --user -r requirements.txt
```

### Erro de Módulo não Encontrado
Certifique-se de estar na pasta correta e que o Python está instalado:
```bash
python --version
```

### Banco de Dados
O banco SQLite será criado automaticamente na primeira execução.

## 📱 Funcionalidades Principais

- ✅ **Página Inicial**: Galeria de pets com filtros
- ✅ **Cadastro ONG**: Formulário completo com validação
- ✅ **Login Seguro**: Sistema de autenticação
- ✅ **Painel ONG**: Gestão completa de pets
- ✅ **Busca por Proximidade**: Geolocalização funcional
- ✅ **Design Responsivo**: Funciona em mobile e desktop
- ✅ **Validação de Dados**: Formulários seguros
- ✅ **Interface Moderna**: Bootstrap 5 + CSS customizado

## 🎨 Personalização

Para personalizar a aparência:
- Edite `static/css/style.css` para cores e estilos
- Modifique os templates em `templates/` para layout
- Ajuste `static/js/main.js` para funcionalidades JavaScript

## 📞 Suporte

Se encontrar problemas:
1. Verifique se seguiu todos os passos
2. Confirme se todas as dependências foram instaladas
3. Verifique se o arquivo `.env` existe e está configurado
4. Execute `python app.py` e veja as mensagens de erro

**Boa sorte com seu projeto PetEncontra! 🐾**
