# Cliq CRM

> Cliq CRM é a plataforma simples e ágil para organizar leads e fechar mais vendas.

![Dashboard Screenshot](https://via.placeholder.com/900x450.png?text=Cliq+CRM+Dashboard)

---

## 📚 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Começando](#-começando)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [⚖️ Licença](#️-licença)
- [📧 Contato](#-contato)

---

## 📖 Sobre o Projeto

O **Cliq CRM** foi desenvolvido para ser uma ferramenta de gestão de relacionamento com o cliente (CRM) focada na simplicidade e agilidade. Ele ajuda equipes de vendas e profissionais autônomos a organizar seus contatos, acompanhar o progresso das negociações e, finalmente, fechar mais negócios.

A plataforma conta com um dashboard intuitivo, funcionalidades de CRUD (Criar, Ler, Atualizar, Deletar) para os registros e um inovador **assistente com Inteligência Artificial** para otimizar tarefas e fornecer insights.

---

## ✨ Funcionalidades

- **Gestão de Leads e Clientes**: Adicione, visualize, atualize e remova registros de clientes de forma organizada.
- **Dashboard Intuitivo**: Um painel de controle centralizado para uma visão geral do status dos seus leads.
- **Assistente com IA**: Um chatbot inteligente (`ai_agent`) integrado para auxiliar os usuários a encontrar informações e executar tarefas.
- **Autenticação de Usuários**: Sistema seguro de registro e login para proteger os dados.
- **API RESTful**: Endpoints (`/crm/serializers.py`) para permitir a integração do Cliq CRM com outras ferramentas e serviços.
- **Importação de Dados**: Ferramenta para importar registros em massa a partir de planilhas Excel (`/crm/utils/import_records.py`).
- **Interface Responsiva**: Design construído com Bootstrap, totalmente adaptável a desktops, tablets e smartphones.

---

## 🛠️ Tecnologias Utilizadas

A stack principal do projeto inclui:

| Categoria | Tecnologia |
|-----------|----------------------------------------------------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) |
| **Banco de Dados** | _(Ex: PostgreSQL, MySQL, SQLite)_ |
| **Ferramentas** | ![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) |

---

## 📂 Estrutura do Projeto

A estrutura de diretórios foi organizada de forma modular para separar as responsabilidades da aplicação.

```
cliq-crm/
├── .gitignore
├── ai_agent/             # App Django para o assistente de IA
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── assistant.py
│   ├── models.py
│   ├── tools.py
│   ├── urls.py
│   └── views.py
├── core/                 # App Django para configurações centrais do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── crm/                  # App Django principal do CRM
│   ├── migrations/
│   ├── utils/            # Scripts utilitários (ex: importação)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
├── manage.py             # Script de gerenciamento do Django
├── requirements.txt      # Dependências Python do projeto
├── secrets/
│   └── .env.example      # Arquivo de exemplo para variáveis de ambiente
├── static/               # Arquivos estáticos (CSS, JS, Imagens)
│   ├── css/
│   ├── js/
│   └── fonts/
├── templates/            # Templates HTML do projeto
│   ├── ai_agent/
│   ├── components/
│   ├── crm/
│   └── base.html
└── utils/
    └── markdown_to_html.py # Utilitários gerais
```

---

## 🚀 Começando

Para executar o projeto localmente, siga os passos abaixo.

### Pré-requisitos

- Python 3.8+
- Um gerenciador de pacotes como `pip`
- Git

### Instalação

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/matheusfabiao/cliq-crm.git
    cd cliq-crm
    ```

2.  **Crie e ative um ambiente virtual**
    ```bash
    # Para Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente**
    Copie o arquivo de exemplo e preencha com suas chaves e configurações.
    ```bash
    cp secrets/.env.example secrets/.env
    ```
    Depois, edite o arquivo `.env` com os valores corretos (chave secreta, configurações de banco de dados, chaves de API, etc.).

5.  **Aplique as migrações do banco de dados**
    ```bash
    python manage.py migrate
    ```

6.  **(Opcional) Crie um superusuário**
    Para acessar a área administrativa do Django.
    ```bash
    python manage.py createsuperuser
    ```

7.  **Execute o servidor de desenvolvimento**
    ```bash
    python manage.py runserver
    ```

Agora você pode acessar a aplicação em `http://127.0.0.1:8000`.

---

## ⚖️ Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📧 Contato

Matheus Fabião - [matheusfabiao.dev@gmail.com](mailto:matheusfabiao.dev@gmail.com)

Link do Projeto: [https://github.com/matheusfabiao/cliq-crm](https://github.com/matheusfabiao/cliq-crm)