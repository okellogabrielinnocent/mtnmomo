from flask import Flask
from dotenv import load_dotenv
import os
from mtnmomo.collection import Collection

load_dotenv()

app = Flask(__name__)

client = Collection({
        "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
        "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
        "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY","f71b158f75324b49bfcd20abd622b3ff"),
    })

@app.route("/")
def request_to_pay():
    pay_request=client.requestToPay(
    mobile="256772123456", amount="600", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")
    # print("===================>",pay_request)
    return pay_request

@app.route("/transactionstatus")
def get_transaction_status():
    get_request_transaction=client.getTransactionStatus('14f71511-114b-4426-ac6d-dc865b795cd3')
    return get_request_transaction

@app.route("/balance")
def get_balance():
    get_balance=client.getBalance()
    return get_balance

@app.route("/transaction")
def get_transaction():
    get_transaction=client.getTransaction()
    return get_transaction
    
if __name__ == "__main__":
    app.run(debug=True)