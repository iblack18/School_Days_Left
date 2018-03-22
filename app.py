from flask import Flask, render_template, redirect, request
import days_left
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', days=days_left.days(datetime.datetime.today()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
