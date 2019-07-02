from flask import Flask, request, render_template
import requests

# Creating the object of flask
app = Flask(__name__)

# To get the Zip code
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')

    code = request.form['code']
    r=requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+ code + ",in&appid=172a15a75ae6f45a8a7bea6adc47fe3a")
    json=r.json()
    temp=float(json['main']['temp'])
    return render_template('temperature.html', temp=temp, name=json['name'])

if __name__ == '__main__':
    app.run(debug=True)