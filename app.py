from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"""
    <h1>Hello,Amit! This is your Cloud App.</h1>
    <p>The current time at the server is: <b>{current_time}</b></p>
    <p>Refresh this page to see it change!</p>
    """

@app.route('/status')
def status():
    return "</h1>System Status: ALL SYSTEM GO</h1>"

@app.route('/about')
def about():
    return "<h1>About Us: We are Cloud Engineers!/<h1>"
if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
