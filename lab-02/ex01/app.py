from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher  # giữ nguyên
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher  # thêm dòng này
from cipher.playfair import PlayFairCipher  # Thêm dòng này nếu bạn tách class ra file riêng


app = Flask(__name__)

# --- Routes ---
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt_route():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vegenere = VigenereCipher()
    encrypted_text = Vegenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt_route():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vegenere = VigenereCipher()
    decrypted_text = Vegenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# --- Rail Fence Cipher Routes ---
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    rf = RailFenceCipher()
    encrypted_text = rf.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    rf = RailFenceCipher()
    decrypted_text = rf.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)