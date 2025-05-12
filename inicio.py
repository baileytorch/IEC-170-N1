#Sistema de gestion de inventario para una tienda
#autor: Manuel Sanchez
"""
version MAJOR.MINOR.PATCH
EJEMPLO v2.4.1

MAJOR: (version mayor): Se incrementa cuando se hacen cambios grandes (generalmente incomptaibles)
    con la version anterior.
MINOR: (version menor): Se incrementa cuando se agregan uevas funcionalidades al sistema, pero 
    sin romper la compatibilidad.
PATCH: (parche o revisión): Se incrementa, cuando se corrigen errores en el sistema, o mejoran 
    funcionalidades 

"""
#Historial 
#       15/04/2025 Inicio del desarrollo v1.0.0
#       22/04/2025 Agrega opción 5 Modificar Cantidad v1.1.0
#       22/04/2025 Mejora las funcionalidades de 3 y 4 al buscar con while v1.1.1
#       29/04/2025 Cambio de paradigma, inicio el trabajo con funciones v2.0.0
#       05/05/2025 Se reemplaza el buscar y mostrar producto por funciones y se 
#                  agregar control de keyboardInterrupt v2.0.1
#       


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

def fn_mostrar_producto(prod, precio, stock):
    """
    `uso`: muestra un producto del inventario;
    `entrada`: nombre, precio y cantidad del producto;
    `retorna`: nada;
    """
    print(f"Producto: {prod}") 
    print("Precio: %5.2f" % precio) 
    print(f"Stock: {stock}")
    print("=====================================")  
    #mostrar_producto()


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

#PROGRAMA PRINCIPAL (PP)
# listas para administrar los productos
try:
    version = "v2.0.1"
    lnombre = ["Plumon", "Borrador", "Pizarra"]
    lprecio = [1280.0, 3500.0, 13500.0]
    lstock = [20,8, 10]

    salir = False
    while not salir:
        print(f" *** Menú {version} ***")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("Opcion: ")
        #****** Agrega producto 
        if (op == "1"):  
            nom = input("Nombre del producto: ")    
            lnombre.append( nom ) 
            precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: ") )
            lprecio.append( precio ) 
            canti = fn_get_num_valido("Cantidad del producto: ") #int(input("Cantidad del producto: ") )
            lstock.append( int(canti)) 
            print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")
        #****** Listar producto 
        if (op == "2"):  
            largo = len (lnombre)
            for i in range(largo):
                fn_mostrar_producto(lnombre[i], lprecio[i], lstock[i])
        #****** Buscar por Nombre
        if (op == "3"):  
            nom = input("Nombre del producto a buscar: ")    
            pos = fn_buscar(lnombre, nom)
            if pos == -1:
                print(f"El producto {nom} no está en el inventario")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
        #****** Eliminar por Nombre
        if (op == "4"):
            nom = input("Nombre del producto a Eliminar: ")    
            pos = fn_buscar(lnombre, nom)
            if pos != -1: #indica que el producto si está
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Seguro que desea eliminar [si/no]: ")
                if resp.upper() == "SI": # nos evitamos el si-Si-sI
                    del lnombre[pos]            # borramos la posicion donde hallamos el producto
                    del lprecio[pos]
                    del lstock[pos]
                    print(f"Producto {nom} eliminado!!.")
                else:
                    print(f"Producto {nom} no se ha eliminado.")
            else:
                print(f"El producto {nom} no está en el inventario")
            #****** Modificar Cantidad
        if (op == "5"):
            nom = input("Nombre del producto a Modificar: ")   
            pos = fn_buscar(lnombre,nom) 
            if pos == -1: # o sea, no está
                print(f"El producto {nom} no está en el inventario")
            else:    # si efectivamente esta
                fn_mostrar_producto(lnombre[pos], lprecio[pos],lstock[pos])
                resp = input("Seguro que desea modificar [si/no]: ")
                if resp.upper() == "SI": # nos evitamos el si-Si-sI
                    cant = fn_get_num_valido("Ingrese nueva cantidad: ") #int(  input("Ingrese nueva cantidad: ") )
                    lstock[pos] = int(cant)
                    print(f"Stock de {nom} modificado!!.")
                else:
                    print(f"Producto {nom} no se ha modificado.")
        if (op == "6"):
            salir = True
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")