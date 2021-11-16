import argparse
import os
    
def contar_palabra(palabra_buscar, nombre_archivo):
    cuenta = 0
    with open(nombre_archivo, "r") as archivo:            
        for linea in archivo:
            palabras = linea.split(" ")
            for p in palabras:
                if p.lower() == palabra_buscar:
                    cuenta += 1
    return cuenta
    

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre del archivo a utilizar")
args = parser.parse_args()

palabra_buscar = 'el'

if args.file and os.path.exists(args.file):
    nombre_archivo = args.file
    
    print('Se buscará la palabra "el" en el archivo:', nombre_archivo)    
    repeticiones = contar_palabra(palabra_buscar, nombre_archivo)    
    print('La palabra "el" se repite {repeticiones} veces en el archivo {archivo}'.format(repeticiones=repeticiones,archivo=nombre_archivo))
            
else:
    print("No existe el archivo de nombre", args.file)
    