import os
from generador_numeros import generar_num_aletaorios, generar_num_cartones



def ingresar_codigo_concurso():
    while True:
        try:
            codigo = input("Ingrese el número del concurso: ")[0:3]            
            if not codigo.isnumeric() or len(codigo) != 3:        
                raise
            
            return codigo
            break
        except:
            print('\nEl código debe tener 3 numeros, intente nuevamente')   
  

# crea el directorio para el concurso
def crear_directorio_concurso(directirio):    
    if not os.path.exists(directirio):
        os.makedirs(directirio)


def escribir_carton(directorio, nombre_archivo, lista_numeros):
    archivo = os.path.join(directorio, nombre_archivo)
    archivo = open(archivo, 'a')
    for n in lista_numeros:
        archivo.write(str(n) + "\n")
    archivo.close()
    
        
def generar_archivos_cartones(dir_cartones, n_concurso, codigos_cartones, numeros_cartones, tot_cartones):
    cuenta = 0
    while cuenta < tot_cartones:        
        nombre_archivo = str(n_concurso) + str(codigos_cartones[cuenta]) + ".carton"
        escribir_carton(dir_cartones, nombre_archivo, numeros_cartones[cuenta])
        cuenta += 1
    
   
    
# código principal

tot_cartones = 100
n_concurso = ingresar_codigo_concurso()
dir_cartones = os.path.join('.', 'consursos', n_concurso)

codigos_cartones = generar_num_aletaorios(100000, 999999, tot_cartones)
numeros_cartones = generar_num_cartones(tot_cartones)


crear_directorio_concurso(dir_cartones)
generar_archivos_cartones(dir_cartones, n_concurso, codigos_cartones, numeros_cartones, tot_cartones)
  