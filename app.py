from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Backend funcionando com Vega + Nova Era"

@app.route("/create-checkout", methods=["POST"])
def create_checkout():
    data = request.json
    # Simulação da URL do checkout Vega
    fake_checkout_url = f"https://checkout.vega.com/session/{data['order_id']}"
    return jsonify({"checkout_url": fake_checkout_url})

@app.route("/novaera-webhook", methods=["POST"])
def novaera_webhook():
    payload = request.json
    print("Webhook recebido:", payload)
    return "ok", 200

if __name__ == "__main__":
    app.run()
