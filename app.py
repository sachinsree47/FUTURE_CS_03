from flask import Flask, request, send_file, render_template, redirect, url_for
from crypto_utils import encrypt_file, decrypt_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
DECRYPTED_FOLDER = 'decrypted/'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        data = file.read()
        encrypted_data = encrypt_file(data)
        enc_filename = file.filename + '.enc'
        with open(os.path.join(UPLOAD_FOLDER, enc_filename), 'wb') as f:
            f.write(encrypted_data)
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(enc_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_file(encrypted_data)

    plain_filename = filename.replace('.enc', '')
    dec_path = os.path.join(DECRYPTED_FOLDER, plain_filename)
    with open(dec_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(dec_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

