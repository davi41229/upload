from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__ , template_folder="front")
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload') # constante do endereço para armazenar a imagem

# ROTA PRINCIPAL
@app.route('/')
def home():
    return render_template("home.html")

# ROTA PARA UPLOAD
@app.route("/upload", methods=['POST'])
def upload():
    try:
        file = request.files['image']
        savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(savePath)
        return render_template('home.html')
    except Exception as error:
        print("Erro:", error)

# ROTA PARA PEGAR IMAGEM
@app.route('/image/<filename>')
def image(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + ".png")
    return send_file(file, mimetype="image/png")
   

if __name__ == "__main__":
    app.run(debug=True, port=(4560))
