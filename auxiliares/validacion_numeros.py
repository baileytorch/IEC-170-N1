def fn_get_num_valido(mensaje):
    """
    funcion para validar el ingreso de un valor numérico.
    No termina hasta que el valor ingresado es válido
    """
    validos = ["0","1","2","3","4","5","6","7","8","9","-","."]
    malopos = False
    repite = True
    num = 0
    while repite:
        num = input( mensaje )
        l = len( num ) #obtener el largo
        malochar = False
        malog = False
        contg = 0
        contp = 0
        for i in range( l ):
            if not num[i] in validos:
                malochar = True
            if num[i] == "-":
                contg = contg+1
            if num[i] == ".":
                contp = contp+1
        malopos = contg == 1 and  num[0] != "-"
        malog = contg > 1
        malop = contp > 1
        if malochar or malog or malopos or malop:
            repite = True
            print("La entrada no es válida")
        else:
            repite = False
    numero = float(num)
    return(numero)
    #fn_get_valida_num