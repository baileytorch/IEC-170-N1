# Sistema de conversión de temperatura entre distintas escalas, Celsius, Fehrenheit y Kelvin.
# 1.- Construir Menu
# 2.- Definir funciones de conversión
# 3.- Pedir datos al usuario
# 4.- Realizar conversión
# 5.- Mostrar Resultado

# ºC K = T+273.15	
# °C °F = (T*1.8)+32
# K °C = T-273.15
# K °F = (T-273.15)*9/5+32
# ºF °C = (T-32)/1.8	
# °F K = (T-32)+273.15

def cargar_menu():
    print("[1] Convertir °C a K.")
    print("[2] Convertir °C a °F.")
    print("[3] Convertir K a °C.")
    print("[4] Convertir K a °F.")
    print("[5] Convertir °F a °C.")
    print("[6] Convertir °F a K.")
    print("[0] Salir.")
    
def convertir_celsius_kelvin(temperatura_inicial):
    temperatura = temperatura_inicial + 273.15
    return temperatura

def convertir_celsius_fahrenheit(temperatura_inicial):
    temperatura = (temperatura_inicial * 1.8) + 32
    return temperatura

def convertir_kelvin_celsius(temperatura_inicial):
    temperatura = temperatura_inicial - 273.15
    return temperatura

def convertir_kelvin_fahrenheit(temperatura_inicial):
    temperatura = convertir_kelvin_celsius(temperatura_inicial) * 9/5 + 32
    return temperatura

def convertir_fahrenheit_celsius(temperatura_inicial):
    temperatura = (temperatura_inicial - 32) / 1.8
    return temperatura

def convertir_fahrenheit_kelvin(temperatura_inicial):
    temperatura = convertir_fahrenheit_celsius(temperatura_inicial) + 273.15
    return temperatura

def programa_principal():
    print()
    print("Súper Conversor de Temperaturas!!")
    print("=================================")
    
    while True:
        cargar_menu()
        opcion = input("Selecciones su opción [0-6]")
        temperatura_usuario = input("Ingrese su Temperatura Inicial: ")
        
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "0":
            print("Chao chao loh vimoh!")
            break
        else:
            print("Opción Inválida")
            return