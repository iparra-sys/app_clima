from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🗝️ Reemplaza con tu propia API key de OpenWeather
API_KEY = "a3e9e61144646e5a7b686c3a68ca350f".strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es'
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = f"Error {response.status_code}: {response.text}"
        else:
            error = "Por favor, ingresa una ciudad."

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
