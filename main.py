from flask import Flask, render_template, url_for, redirect
from flask import send_from_directory

app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/home')
def index():
    return redirect(url_for('static', filename='main.html'))


data_slice = {
    'lastUpdate': '2023-09-09T13:40:51.389Z', 
    'value': [
            {'currency':'RUNE/USDT', 'datetime': '2023-09-09T13:40:50.812Z', 'asks': [1.573, 950.5], 'bids': [1.572, 5558.3]}, 
            {'currency':'ZEN/USDT','datetime': '2023-09-09T13:40:51.113Z', 'asks': [7.27, 82.14], 'bids': [7.26, 2334.12]}, 
            {'currency':'SNX/USDT','datetime': '2023-09-09T13:40:51.213Z', 'asks': [2.15, 392.1], 'bids': [2.148, 23.1]}, 
            {'currency':'AAVE/USDT','datetime': '2023-09-09T13:40:51.013Z', 'asks': [56.09, 19.312], 'bids': [56.08, 0.959]}
            ]
        }


@app.route('/data')
def data():
    return data_slice


if __name__ == '__main__':
    app.run(debug=True)
