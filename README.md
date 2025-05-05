

# 💸 Socket API - Sistema de Pagamentos com QR Code (PIX)

Este projeto é uma aplicação web desenvolvida com Flask que simula um sistema de pagamentos via PIX. Ele utiliza WebSockets para comunicação em tempo real com clientes e exibe um QR Code único para cada pagamento gerado.

## 🚀 Funcionalidades

- Criar pagamentos via PIX com identificação única.
- Geração de QR Code correspondente ao pagamento.
- Interface web para visualização e confirmação de pagamento.
- Comunicação em tempo real utilizando Flask-SocketIO.
- Testes com Pytest.
- Banco de dados com SQLAlchemy.

## 🧰 Tecnologias Utilizadas

- Python 3.11
- Flask
- Flask-SocketIO
- SQLAlchemy
- SQLite
- Pytest
- qrcode

## 📁 Estrutura do Projeto

```

Socket\_Api/
├── app.py                     # Arquivo principal da aplicação Flask
├── payments/
│   └── pix.py                # Lógica de criação de pagamento PIX e QR Code
├── static/
│   ├── css/                  # Arquivos de estilo
│   └── template\_img/         # Imagens estáticas da interface
├── templates/
│   ├── confirmed\_payment.html
│   ├── payment.html
│   └── 404.html
├── tests/
│   └── teste\_pix.py          # Testes unitários com Pytest
└── README.md                 # Documentação do projeto

````

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
````

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000
```

## 🧪 Rodar os Testes

```bash
cd tests
pytest -v
```
