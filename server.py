from flask import Flask
from flask_socketio import SocketIO, send, emit
from color import Color
from player import Player


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

# unusedPlayers = set()
# players = set()

@app.route('/')
def index():
    return 'Index Page'

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('received message' + str(json))

@socketio.on('start')
def handle_start(data):
    print(data)
    emit("begin", broadcast=True)

# @app.route('/newPlayer')
# def newPlayer():
#     global test
#     player = Player(Color.RED)
#     return str()
    
