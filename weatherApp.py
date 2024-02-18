from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='/home/debasis/mysite/templates')

api_key = 'a5457a4587a8a0f123d4b9fa587b2a50'
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('look.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    response = requests.get(weather_api_url, params=params)
    weather_data = json.loads(response.text)

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return render_template('result.html', city=city, temperature=temperature, description=description)
    else:
        return render_template('error.html', error_message=f"Unable to fetch weather data for {city}")

if __name__ == '__main__':
    app.run(port = 5002)






