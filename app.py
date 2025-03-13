from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# ======= CAESAR CIPHER =======
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# ======= VIGENÈRE CIPHER =======
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/encrypt", methods=['POST']) 
def vigenere_encrypt():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    vigenere = VigenereCipher()
    encrypt_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/decrypt", methods=['POST']) 
def vigenere_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyCipher']
    vigenere = VigenereCipher()
    decrypt_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"

# ======= PLAYFAIR CIPHER =======
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/encrypt", methods=['POST']) 
def playfair_encrypt():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key) 
    encrypt_text = playfair.playfair_encrypt(text, matrix)  
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/decrypt", methods=['POST'])  
def playfair_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)  
    decrypt_text = playfair.playfair_decrypt(text, matrix) 
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"

# ======= RAIL FENCE CIPHER =======
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/encrypt", methods=['POST']) 
def railfence_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    rail = RailFenceCipher()
    encrypt_text = rail.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/decrypt", methods=['POST']) 
def railfence_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyCipher'])
    rail = RailFenceCipher()
    decrypt_text = rail.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"

# ======= TRANSPOSITION CIPHER =======
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/encrypt", methods=['POST']) 
def transposition_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    transposition = TranspositionCipher()
    encrypt_text = transposition.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"

@app.route("/decrypt", methods=['POST']) 
def transposition_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyCipher'])
    transposition = TranspositionCipher()
    decrypt_text = transposition.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
