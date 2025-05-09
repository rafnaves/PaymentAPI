from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)



@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if 'value' not in data:
        return jsonify({"message": "Valor Invalido"}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment()
    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]

    qr_code_path = data_payment_pix["qr_code_path"]
    qr_code_filename = qr_code_path.split("/")[-1]
    new_payment.qr_code = qr_code_filename


    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        "message": "O pagamento foi criado",
        "payment": new_payment.to_dict()
    })


@app.route('/payments/pix/qr_code/<file_name>', methods=["GET"])
def get_image(file_name):
    return send_file(f"static/img/{file_name}", mimetype='image/png')


@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()

    if "bank_payment_id" not in data and "value" not in data:
        return jsonify({"message": "Invalid payment data"}), 400

    payment = Payment.query.filter_by(bank_payment_id=data.get("bank_payment_id")).first()

    if not payment or payment.paid:
        return jsonify({"message": "Payment not found"}), 404

    if data.get("value") != payment.value:
        return jsonify({"message": "Invalid payment data"}), 400

    payment.paid = True
    db.session.commit()

    socketio.emit('admin-update', f"Pagamento {payment.id} confirmado no valor de R$ {payment.value}")
    
    socketio.emit(f"payment-confirmed-{payment.id}")
    
    return jsonify({"message": "Payment confirmed"})


@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id)

    # Primeiro verifica se não encontrou
    if not payment:
        return render_template('404.html'), 404

    # Só acessa atributos se existir
    if payment.paid:
         return render_template('confirmed_payment.html',
                                payment_id=payment.id,
                                value=payment.value) 

    return render_template('payment.html', 
                           payment_id=payment.id, 
                           value=payment.value, 
                           host="http://127.0.0.1:5000",
                           qr_code=payment.qr_code)

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# Web Sockets
@socketio.on('connect')
def handle_connect():
    print("Cliente Conectado ao server")

@socketio.on('diconnect')
def handle_disconnect():
    print("Client has diconnected")

@socketio.on('message')
def handle_message(msg):
    print('Mensagem recebida:', msg)
    socketio.send(msg)  # envia de volta para todos conectados

@socketio.on('admin-message')
def handle_admin_message(msg):
    print("Mensagem recebida no painel admin:", msg)
    socketio.emit('admin-update', msg)


if __name__ == '__main__':
    socketio.run(app, debug=True)


