from flask import Flask, request, render_template
from rachel6 import process
from flask.helpers import send_file

app = Flask(__name__)

@app.route('/excel_pengolahan')
def file_():
    temp = "static/untukalgo.xlsx"
    return send_file(temp, as_attachment=True)

@app.route('/', methods=['POST', 'GET'])
def proyek():
    if request.method == 'GET':
        return render_template('isi.html')
    if request.method == 'POST':
        grafik =request.files['inputkedalaman']
        tampilan = process((grafik))
        return render_template('proyek.html', datasuhu=str(tampilan))

if __name__=="__main__":
    app.run()

