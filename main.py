from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "fhkjdshfsadkfhsdfhjklqfhjdkshflkjadfhajkdfhjksadjhfkaslfhakhdjk"
socket = SocketIO(app)

clients = 0

@socket.on("message")
def handle_message(dataRecieved):
    global clients

    if dataRecieved["type"] == "connect": 
        clients += 1
        socket.send({"type": "user", "users": clients}, broadcast=True)

    if dataRecieved["type"] == "form_submit":
        socket.send(dataRecieved, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socket.run(app, host="192.168.0.13", port=1209, debug=True)