import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # Criação do pagamento na instituição financeira

        bank_payment_id = str(uuid.uuid4())

        img = qrcode.make('hash_payment')

        # Qr Code
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make('hash_payment')
        type(img)
        img.save(f"{base_dir}static/img/qr_code_{bank_payment_id}.png")

        return {
            "bank_payment_id": str(bank_payment_id),
            "qr_code_path": f"static/img/qr_code_{bank_payment_id}.png"
        }

