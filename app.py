from flask import Flask, render_template, request
from weather_analyzer import get_weather_status

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_city = request.form.get('start_city')
        end_city = request.form.get('end_city')

        start_weather = get_weather_status(start_city)
        end_weather = get_weather_status(end_city)

        return render_template('result.html', start_weather=start_weather, end_weather=end_weather)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
