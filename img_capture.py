import requests
import upload


def captura_imagen():
    # la captura de imagen para usarla con la camara IP habria que cambiar el cam.read por un get que le pida
    # una captura a la camara. en este momento funciona con la camara conectada.
    # http://192.168.1.108/CGI/command/snap?channel=0
    # aqui pedimos captura a la camara por red.
    try:
        r = requests.get('http://192.168.1.71:6688/snapshot/PROFILE_000')
        file = open("unprocessed_imgs/captura_camara.jpeg", "wb")
        file.write(r.content)
        file.close()
        upload.upload('unprocessed_imgs/captura_camara.jpeg')
    except Exception as e:
        print("error en la captura")
# captura_imagen()