# 💸 Socket API - Sistema de Pagamentos com QR Code (PIX)

Este projeto é uma aplicação web desenvolvida com Flask que simula um sistema de pagamentos via PIX. Ele utiliza WebSockets para comunicação em tempo real e exibe um QR Code único para cada pagamento gerado.

## 🚀 Funcionalidades

- ✅ Criar pagamentos via PIX com identificação única.
- ✅ Geração automática de QR Code para o pagamento.
- ✅ Interface web para visualização e confirmação de pagamento.
- ✅ Comunicação em tempo real com clientes usando Flask-SocketIO.
- ✅ Chat em tempo real com WebSocket.
- ✅ Notificações de confirmação de pagamento em tempo real.
- ✅ Banco de dados local com SQLite e SQLAlchemy.
- ✅ Testes automatizados com Pytest.

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
├── app.py                      # Aplicação principal
├── payments/
│   └── pix.py                  # Geração de pagamento e QR Code
├── repository/
│   └── database.py             # Configuração do banco de dados
├── db\_models/
│   └── payment.py              # Modelo da tabela Payment
├── static/
│   ├── css/                    # Arquivos de estilo
│   └── img/                    # QR Codes gerados
├── templates/
│   ├── confirmed\_payment.html  # Página de sucesso após pagamento
│   ├── payment.html            # Página com QR Code para pagamento
│   ├── index.html              # Interface de chat em tempo real
│   └── 404.html                # Página de erro
├── tests/
│   └── teste\_pix.py            # Testes unitários com Pytest
└── README.md                   # Documentação do projeto

````

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000/index     # Interface de chat
http://127.0.0.1:5000/payments/pix/1  # Exemplo de página de pagamento
```

## 💬 Chat em Tempo Real

O projeto inclui um chat funcional com WebSockets, acessível pela rota `/index`. As mensagens são compartilhadas entre todos os clientes conectados. Além disso, eventos administrativos como confirmações de pagamento são enviadas em tempo real para a interface.

## 🧪 Rodar os Testes

```bash
cd tests
pytest -v
```

---

Projeto criado para fins educacionais e demonstração de integração entre Flask, WebSocket e pagamentos simulados via PIX.

```

---
