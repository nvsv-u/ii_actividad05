from random import randint

# genera los codigos de los cartones o los números del carton, según de donde de llame
def generar_num_aletaorios(minimo, maximo, cantidad):
    lista = []
    cuenta = 0    
    while cuenta < cantidad:        
        repetido = False        
        aleatorio = randint(minimo, maximo)        
        # comprobar repetido        
        for codigo in lista:
            if aleatorio == codigo:
                repetido = True
                break
        # si no se repite agregar a la lista    
        if not repetido:
            lista.append(aleatorio)
            cuenta += 1            
    return lista


# genera un lista con los numeros de los cartones
# utiliza la función generar_num_aletaorios para cada carton
# la lógica es simila a generar_num_aletaorios,
def generar_num_cartones(tot_cartones):    
    numeros_cartones = []
    cuenta = 0
    while cuenta < tot_cartones:        
        repetido = False        
        nuevo_carton = generar_num_aletaorios(1, 36, 6)       
        # comprobar repetido        
        for carton in numeros_cartones:
            if nuevo_carton == carton:
                repetido = True
                break
        # si no se repite agregar a la lista    
        if not repetido:
            numeros_cartones.append(nuevo_carton)
            cuenta += 1            
    return numeros_cartones
