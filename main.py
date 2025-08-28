import random
import os

print("WELCOME TO THE POSSIBLE PASSWORD GENERATOR")

list_afectons_user = []

# Pedir palabras al usuario
def afections_user():
    while True:
        respuesta = input("Escribe palabras o números relacionados; EJ: cumpleaños, num favorito, etc (escribe 'exit' para terminar): ")
        if respuesta.lower() == "exit":
            break
        list_afectons_user.append(respuesta)
    return list_afectons_user

respuestas = afections_user()
print("Las palabras que ingresaste son:", respuestas)

# Separar números de palabras
numeros = [x for x in respuestas if x.isdigit()]
palabras = [x for x in respuestas if not x.isdigit()]

# Configuración: cuántas contraseñas generar
num_contraseñas = int(input("¿Cuántas combinaciones quieres generar?: "))

# Ruta del archivo en el escritorio
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "contraseñas.txt")

# Función para generar una contraseña aleatoria
def generar_contraseña(palabras, numeros):
    # Elegir cuántas palabras usar (mínimo 1)
    cantidad = random.randint(1, len(palabras)) if palabras else 0
    seleccion = random.sample(palabras, cantidad) if palabras else []
    
    combinacion = "".join(seleccion)
    
    # Aleatoriamente poner la primera letra en mayúscula
    if combinacion and random.choice([True, False]):
        combinacion = combinacion.capitalize()
    
    # Aleatoriamente agregar un número de la lista al principio o final
    if numeros:
        num = random.choice(numeros)
        if random.choice([True, False]):
            combinacion = num + combinacion
        else:
            combinacion = combinacion + num
    
    return combinacion

# Generar todas las contraseñas
contraseñas = [generar_contraseña(palabras, numeros) for _ in range(num_contraseñas)]

# Guardar en archivo
with open(desktop_path, "w", encoding="utf-8") as f:
    for c in contraseñas:
        f.write(c + "\n")

print(f"{num_contraseñas} contraseñas generadas y guardadas en {desktop_path}")
