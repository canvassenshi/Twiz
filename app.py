from flask import Flask, url_for, render_template, request, redirect
from flask_socketio import SocketIO, send


app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)

@app.route("/")
def signUp():
    return render_template("getuser.html")

@app.route("/index")
def message():
    username = request.args.get("username")
    if username:
        return render_template("index.html", username = username)


if __name__ == "__main__":
    app.run()

