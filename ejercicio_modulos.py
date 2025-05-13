import math

# pi = 3.1416
pi = math.pi


def area_circunferencia(radio):
    area = pi * radio ** 2
    return area

def raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada

def ejecutar_codigo():
    print()
    radio = float(input("Ingrese el radio de la circunferencia: "))
    print()
    respuesta_1 = area_circunferencia(radio)
    
    numero = float(input("Ingrese un número: "))
    print()
    respuesta_2 = raiz_cuadrada(numero)
    
    print(f"El área de la circunferencia de radio {radio} = {respuesta_1}")
    print()
    print(f"La raíz cuadrada de {numero} = {respuesta_2}")
    print()
    
ejecutar_codigo()

