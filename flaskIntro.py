from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, SmartNinja!"

if __name__ == '__main__':
    app.run()