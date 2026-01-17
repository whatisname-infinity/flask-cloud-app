from flask import Flask, render_template
import datetime
from datetime import timedelta
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    now_utc = datetime.datetime.now()
    now_ist = now_utc + timedelta(hours=5, minutes=30)
    current_time = now_ist.strftime("%H:%M:%S")
    cpu_percent = psutil.cpu_percent(interval=None)
    mem_percent = psutil.virtual_memory().percent
    return render_template('index.html',user_name="Amit", server_time=current_time,cpu=cpu_percent,mem=mem_percent)

@app.route('/status')
def status():
    return "</h1>System Status: ALL SYSTEM GO</h1>"

@app.route('/about')
def about():
    return "<h1>About Us: We are Cloud Engineers!/<h1>"
if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
