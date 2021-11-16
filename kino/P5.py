import os
from generador_numeros import generar_num_aletaorios


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


def exsite_directorio(directorio):
     return os.path.exists(directorio)
    

def contar_aciertos(nums_carton, nums_ganadores):
    aciertos = 0
    for c in nums_carton:
        if c in nums_ganadores:
            aciertos += 1
    return aciertos

def carton_a_lista(archivo_carton):
    lista = []
    for linea in archivo_carton:
        lista.append(int(linea[0]))
    return lista

# itera sobre los cartones y retorna un diccionario
# el diccionario tiene como clave el número de aciertos y como valor la lista de los que acertaron
def obtener_ganadores(dir_cartones, nums_ganadores):
    archivos = os.listdir(dir_cartones)
    ganadores = {6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    for nombre_archivo in archivos:
        directorio_archivo = os.path.join(dir_cartones, nombre_archivo)
        with open(directorio_archivo, "r") as archivo_carton:
            nums_carton = carton_a_lista(archivo_carton)
            aciertos = contar_aciertos(nums_carton, nums_ganadores)
            if aciertos > 0:
                ganadores[aciertos].append(nombre_archivo)
    return ganadores


def calcular_montos(porcentajes_monto_repartir, monto_total):
    montos_repartir = {}
    for clave, valor in porcentajes_monto_repartir:
        monto =  (valor/100) * monto_total
        montos_repartir[clave] = monto
    return montos_repartir        

def mostrar_ganadores(ganadores, montos_repartir):
    for clave, valor in montos_repartir:
        print('Quienes acertaron {aciertos}, que ganan {monto} son: '
              .format(aciertos=clave, monto=valor))
        for carton in  ganadores[clave]:
            print("\t - {carton}".fromat(carton=carton))
            
            
# codigo principal
    
n_concurso = 0
while True:    
    n_concurso = ingresar_codigo_concurso()
    if not exsite_directorio(os.path.join('.', 'consursos', n_concurso)):
        print("No exsiste concurso con el código ingresado, intente nuevamente")
        continue
    break

porcentajes_monto_repartir = {6: 40, 5: 20, 4: 10, 3: 5, 2: 3, 1: 1} # clave: aciertos, valor: porcentaje
dir_cartones = os.path.join('.', 'consursos', n_concurso)
monto_total = int(input("Ingrese el monto a repartir: "))

nums_ganadores = generar_num_aletaorios(1, 36, 6)
ganadores = obtener_ganadores(dir_cartones, nums_ganadores)

print(ganadores)

#montos_repartir = calcular_montos(porcentajes_monto_repartir, monto_total)


# mostrar_ganadores(ganadores, montos_repartir)





    

    
