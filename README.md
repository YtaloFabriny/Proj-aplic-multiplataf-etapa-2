# PetEncontra - Plataforma de Adoção de Pets

Uma plataforma web completa para conectar pets em busca de um lar com pessoas dispostas a adotar. Desenvolvida com Python Flask, permite que ONGs de resgate se cadastrem e listem pets para adoção, enquanto o público geral pode encontrar pets próximos com sistema de filtros avançados e busca por proximidade geográfica.

## 🚀 Características

- **Sistema de ONGs**: Cadastro e login seguro para organizações de resgate
- **Gestão de Pets**: CRUD completo para gerenciar pets disponíveis para adoção
- **Filtros Avançados**: Busca por espécie, idade, porte e proximidade geográfica
- **Geolocalização**: Encontre pets próximos usando a localização do usuário
- **Interface Responsiva**: Design moderno com Bootstrap 5
- **Segurança**: Hash de senhas, validação de dados e proteção CSRF

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.9+, Flask, Flask-SQLAlchemy, Flask-Login
- **Banco de Dados**: SQLite (desenvolvimento)
- **Frontend**: HTML5, CSS3, JavaScript ES6+, Bootstrap 5
- **Geolocalização**: Browser Geolocation API + Geopy (Python)
- **Segurança**: Werkzeug Security, Flask-WTF

## 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone ou baixe o projeto**:
   ```bash
   cd site_animais
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   
   # No Windows:
   venv\Scripts\activate
   
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=sua_chave_secreta_super_segura_aqui
   DATABASE_URL=sqlite:///petencontra.db
   ```

5. **Execute a aplicação**:
   ```bash
   python app.py
   ```

6. **Acesse no navegador**:
   Abra [http://localhost:5000](http://localhost:5000)

## 📁 Estrutura do Projeto

```
petencontra/
├── app.py                 # Aplicação principal Flask
├── models.py             # Modelos do banco de dados (Ong, Pet)
├── config.py             # Configurações da aplicação
├── requirements.txt      # Dependências Python
├── README.md            # Este arquivo
├── static/
│   ├── css/
│   │   └── style.css    # Estilos customizados
│   └── js/
│       └── main.js      # JavaScript principal
├── templates/
│   ├── base.html        # Template base
│   ├── index.html       # Página inicial
│   ├── ong_cadastro.html # Cadastro de ONG
│   ├── ong_login.html   # Login de ONG
│   ├── ong_painel.html  # Painel da ONG
│   ├── adicionar_pet.html # Adicionar pet
│   ├── editar_pet.html  # Editar pet
│   ├── pet_detalhes.html # Detalhes do pet
│   ├── 404.html         # Página de erro 404
│   └── 500.html         # Página de erro 500
└── validation/          # Documentação de validação com público-alvo
    ├── validation_report.md      # Relatório completo de validação
    ├── target_audience.md        # Definição do público-alvo
    ├── evidence/                 # Evidências fotográficas/vídeo
    └── feedback/                 # Feedback coletado dos participantes
```

## 🎯 Funcionalidades

### Para o Público Geral
- ✅ Visualizar galeria de pets disponíveis para adoção
- ✅ Filtrar pets por espécie, idade e porte
- ✅ Buscar pets próximos usando geolocalização
- ✅ Ver detalhes completos de cada pet
- ✅ Entrar em contato com a ONG responsável

### Para ONGs
- ✅ Cadastrar organização com dados completos
- ✅ Login seguro no sistema
- ✅ Painel de controle para gerenciar pets
- ✅ Adicionar novos pets com fotos e descrições
- ✅ Editar informações dos pets existentes
- ✅ Remover pets do sistema
- ✅ Visualizar estatísticas de adoções

## 🔐 Segurança

- **Senhas**: Armazenadas com hash usando Werkzeug Security
- **Sessões**: Gerenciadas com Flask-Login
- **Validação**: Dados validados com Flask-WTF
- **CSRF**: Proteção contra ataques CSRF
- **Sanitização**: Entrada de dados sanitizada

## 🌍 Geolocalização

A aplicação utiliza:
- **Frontend**: Browser Geolocation API para obter coordenadas do usuário
- **Backend**: Biblioteca Geopy para calcular distâncias entre coordenadas
- **Geocoding**: Conversão automática de endereços em coordenadas (Ong cadastro)

## 📱 Responsividade

Interface totalmente responsiva que funciona em:
- 💻 Desktop
- 📱 Smartphones
- 📱 Tablets

## ✅ Validação com Público-Alvo

O projeto PetEncontra passou por um processo de validação com público-alvo para garantir que a plataforma atenda às necessidades reais dos usuários. A validação foi realizada com representantes dos dois principais grupos de usuários: **ONGs de resgate** e **pessoas interessadas em adotar pets**.

### Resumo da Validação

A validação incluiu:
- **Testes de usabilidade** com ONGs reais de resgate de animais
- **Avaliação da interface** por potenciais adotantes
- **Feedback sobre funcionalidades** principais (busca, filtros, geolocalização)
- **Análise de experiência do usuário** em diferentes dispositivos

### Resultados Principais

- ✅ Interface intuitiva e fácil de navegar
- ✅ Sistema de filtros atende às necessidades de busca
- ✅ Funcionalidade de geolocalização bem recebida
- ✅ Painel de ONG facilita o gerenciamento de pets
- 🔄 Melhorias sugeridas documentadas para próximas versões

### Documentação Completa

A documentação completa da validação está disponível na pasta `validation/`:

- **[Relatório de Validação](validation/validation_report.md)**: Relatório detalhado com metodologia, resultados e conclusões
- **[Definição do Público-Alvo](validation/target_audience.md)**: Perfil detalhado dos grupos de usuários validados
- **[Evidências](validation/evidence/)**: Registros fotográficos e vídeos das sessões de validação (com autorização dos participantes)
- **[Feedback Coletado](validation/feedback/)**: Feedback detalhado e análises qualitativas dos participantes

> **Nota**: As evidências fotográficas e vídeos foram coletadas com autorização expressa dos participantes, respeitando a privacidade e os termos de uso.

## 🚀 Deploy

Para produção, considere:
1. Usar um banco de dados mais robusto (PostgreSQL)
2. Configurar um servidor web (Nginx + Gunicorn)
3. Usar HTTPS
4. Configurar variáveis de ambiente adequadas
5. Implementar backup do banco de dados

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:
1. Verifique se seguiu todos os passos de instalação
2. Confirme se todas as dependências foram instaladas
3. Verifique se o arquivo `.env` está configurado corretamente
4. Abra uma issue no repositório

## 🎉 Agradecimentos

- Bootstrap 5 pela interface moderna
- Flask pela simplicidade e poder
- Comunidade Python pelo suporte
- Todas as ONGs que lutam pelos direitos dos animais

---

**Feito com ❤️ para os animais que precisam de um lar!**
