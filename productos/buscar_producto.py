def fn_buscar(lista, nombre):
    esta = False
    i = 0
    l = len (nombre)
    while i < l and not esta:
        if lista[i].upper() == nombre.upper():
            esta = True
        else:
            i = i + 1
    if esta:  #si lo encuentra "esta" vale True
        return i    #retornamos la posicion donde lo halló
    else:
        return -1    #retornamos -1 si no lo encuentra
    #buscar()