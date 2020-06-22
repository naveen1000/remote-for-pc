from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import keyboard
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Its connected'})

@socketio.on('message')
def value_changed(message):
    print(message)
    keyboard.send(message)
    #emit('update value', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
