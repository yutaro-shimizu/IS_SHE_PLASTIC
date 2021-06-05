import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect, secure_filename, send_from_directory

from ML import detect

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['filename']
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded',filename=filename))
    return render_template('index.html')

@app.route('/display/<path:filename>')
def uploaded(filename):
    #call ML.py and get result
    result = detect(filename)
    if result:
        return render_template('success.html', user_image=filename)
    return render_template('fail.html')

@app.route('/test')
def test():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)