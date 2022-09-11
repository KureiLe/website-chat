from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "fhkjdshfsadkfhsdfhjklqfhjdkshflkjadfhajkdfhjksadjhfkaslfhakhdjk"
socket = SocketIO(app, cors_allowed_origins=['https://uselessweb.herokuapp.com/'])

@socket.on("message")
def handle_message(message):
    if message != "someone connected!":
        send(message, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socket.run(app, debug=True)