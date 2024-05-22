import requests
from bs4 import BeautifulSoup
import os

def obtencion_img():
    url = "https://www.fravega.com/l/celulares/celulares-liberados/?djazz_ref=&djazz_srv=circular-categories&djazz_src=HOME&djazz_pos=2"
    response = requests.get(url) # realiza una solicitud GET a la url
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser') # si la respuesta es exitosa, extrae el contenido HTML de la respuesta
        imagenes = [] # lista para almacenar las urls
        resp = soup.find_all('img', src=True) # obtiene todas las etiquetas img con atributo src
        for img in resp: # recorre cada etiqueta img
            src = img['src'] # obtiene el atributo src
            if src.endswith('.jpg') or src.endswith('.png') or src.endswith('.webp'): 
                imagenes.append(src) # si las imagenes son .jpg, .png o .webp, las agrega a la lista
        return imagenes # retornamos lista



def guardar_img(lista):
    name_file = 'imagenes' # nombre del directorio donde se guardaran las imagenes
    try:
        os.mkdir(name_file) # crea el directorio
        print("Directorio %s creado" % name_file)
    except FileExistsError:
        print("El directorio %s ya existe" % name_file)
        
    for img in lista: # recorre cada url de imagen en la lista
        response = requests.get(img) # descarga la imagen desde la url
        if response.status_code == 200: # verifica si la solicitud fue exitosa
            name = img.split('/')[-1] # extrae el nombre de la imagen de la url
            ruta_comp = os.path.join(name_file, name) # combina la carpeta y el nombre del archvivo para obtener la ruta completa
            with open(ruta_comp, 'wb') as file: # abre el archivo en modo binario
                file.write(response.content) # escribe la imagen
                print("Imagen %s guardada" % name)
        else:
            print("Error al descargar la imagen %s" % name)
            

lista_img = obtencion_img()
guardar_img(lista_img)