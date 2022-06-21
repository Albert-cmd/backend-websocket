import os
import glob
import base64
import io
from PIL import Image


def capture_and_serialize():
    # limpiamos los json
    directory = "./processed_imgs"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".json")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)  # cogemos la ultima imagen del directorio de imagenes procesadas.
    if len(os.listdir('./processed_imgs')) == 0:
        print('directorio vacio')
        return 'directorio_vacio'

    directorio = glob.glob('processed_imgs/*.jpeg')  # * solo coge los jpeg del directorio
    ultima_imagen = max(directorio, key=os.path.getctime)  # la serializamos en bytes base 64.
    with open(ultima_imagen, "rb") as image:
        i = image.read();
        imagenResul = bytearray(i)
    encoded_img = base64.b64encode(imagenResul)
    # os.remove(ultima_imagen)  # la eliminamos una vez la devolvemos. sino se acumulan.

    return encoded_img


def get_processed_img_path():
    # limpiamos los json
    directory = "./processed_imgs"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".json")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)  # cogemos la ultima imagen del directorio de imagenes procesadas.
    if len(os.listdir('./processed_imgs')) == 0:
        print('directorio vacio')
        return 'directorio_vacio'

    directorio = glob.glob('processed_imgs/*.jpeg')  # * solo coge los jpeg del directorio
    ultima_imagen = max(directorio, key=os.path.getctime)  # la serializamos en bytes base 64.

    # os.remove(ultima_imagen)  # la eliminamos una vez la devolvemos. sino se acumulan.
    img_path = os.path.realpath(ultima_imagen)
    return img_path


def capture_and_serialize_real():
    # limpiamos los json
    directory = "./processed_plane_imgs"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".json")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)  # cogemos la ultima imagen del directorio de imagenes procesadas.
    if len(os.listdir('./processed_plane_imgs')) == 0:
        print('directorio vacio')
        return 'directorio_vacio'

    directorio = glob.glob('processed_plane_imgs/*.jpeg')  # * solo coge los jpeg del directorio
    ultima_imagen = max(directorio, key=os.path.getctime)  # la serializamos en bytes base 64.
    with open(ultima_imagen, "rb") as image:
        i = image.read();
        imagenResul = bytearray(i)
    print('----------------------------- IMAGEN RESUL -------------------------------')
    print(imagenResul)
    encoded_img = base64.b64encode(imagenResul)
    print(encoded_img)
    # os.remove(ultima_imagen)  # la eliminamos una vez la devolvemos. sino se acumulan.

    return encoded_img
