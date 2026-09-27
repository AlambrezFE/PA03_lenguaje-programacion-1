
from mamifero import Mamifero
from ave import Ave

def obtener_texto(mensaje):
#validacion de datos
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("Error: El campo no puede estar vacío. Inténtalo de nuevo.\n")
        elif entrada.isnumeric():
            print("Error: El texto no puede contener solo números. Ingresa palabras válidas.\n")
        else:
            return entrada
 
def main():
    print("=== Registro del Mamífero ===")
    nombre_m = obtener_texto("Introduce el nombre del mamífero: ")
    especie_m = obtener_texto("Introduce la especie: ")
    pelo_m = obtener_texto("Describe cómo es su pelo: ")

    print("\n=== Registro del Ave ===")
    nombre_a = obtener_texto("Introduce el nombre del ave: ")
    especie_a = obtener_texto("Introduce la especie: ")
    plumas_a = obtener_texto("Describe cómo son sus plumas : ")

    # Creación de objetos de cada subclase con los datos introducidos
    leon = Mamifero(nombre=nombre_m, especie=especie_m, pelo=pelo_m)
    loro = Ave(nombre=nombre_a, especie=especie_a, plumas=plumas_a)
 
    animales = [leon, loro]
 
    print("\n=== Información de los animalitos ===\n")
    for animal in animales:
        animal.mostrar_info()
        print("-" * 30)
        
    # modelo para imprimir lineas debajo de cada animal
    print("\n=== Oraciones propias de cada subclase ===\n")
    leon.amamantar()
    loro.volar()
 
if __name__ == "__main__":
    main()