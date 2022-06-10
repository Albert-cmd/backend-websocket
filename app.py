from flask import Flask, request, Response
from flask_socketio import SocketIO, emit

import return_and_serialize
import upload_real_photo
import videocapture

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
app.debug = True


# -------------- METODOS DE WEBSOCKET ------------------------
@app.route('/')
def hello_world():  # put application's code here
    return 'im running !!!'


@socketio.on('connect')
def test_connect():
    print('cliente conectado.')


@socketio.on('disconnect')
def test_connect():
    print('cliente desconectado.')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + str(data))


# ---------------------- METODOS DE WS REST ----------------
@app.route('/get_real_img')
def get_real_img():
    serialized_real_img = return_and_serialize.capture_and_serialize_real()

    return serialized_real_img


@app.route('/get_img')
# serializamos y devolvemos la ultima imagen procesada del directorio de imagenes processed_imgs.
def return_processed_image():
    # esto hay que mandarlo a ejecutarse en otro thread.
    serialized_img = return_and_serialize.capture_and_serialize()
    # thread = multiprocessing.Process(target=return_and_serialize.capture_and_serialize(), name='serialize')
    # thread.start()
    return serialized_img


@app.route('/process_real_img', methods=['POST'])
# este metodo es un post que procesa una imagen real y la envia al servidor de AWS con el modelo de deep learning.
def process_real_img():
    print('metodo process real img.')
    img = request.form['img']
    upload_real_photo.upload(img)

    return Response(status=200)


@app.route('/get_real_img')
def return_real_img():
    serialized_real_img = return_and_serialize.capture_and_serialize_real()

    return serialized_real_img


@app.route('/run')
def run_listen_and_upload():  # pone en marcha el reconocimiento de imagenes.

    print("esto es el metodo run")
    stop = request.args.get('stop', default=False, type=bool)
    videocapture.capture_and_upload(stop)
    # hay que ejecutar el proceso en segundo plano en otro thread.
    videocapture.capture_and_upload(stop)
    return Response(status=200)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
