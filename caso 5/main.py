 
from circulo import Circulo
from cuadrado import Cuadrado
 
def obtener_numero_positivo(mensaje):
    """
    Solicita un número al usuario y valida que sea positivo y numérico.
    """
    while True:
        entrada = input(mensaje)
        try:
            # Utilizamos float
            valor = float(entrada)
            if valor <= 0:
                print("Error: Debes introducir un número mayor que cero.\n")
            else:
                return valor
        except ValueError:
            print("Error: Entrada inválida. Por favor, introduce solo números.\n")

def obtener_texto(mensaje):

    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("Error: Este campo no puede estar vacío.\n")
        else:
            return entrada

def main():
    print("=== Configuración del Círculo ===")
    color_circulo = obtener_texto("Introduce el color del círculo: ")
    radio_circulo = obtener_numero_positivo("Introduce el radio del círculo: ")

    print("\n=== Configuración del Cuadrado ===")
    color_cuadrado = obtener_texto("Introduce el color del cuadrado: ")
    lado_cuadrado = obtener_numero_positivo("Introduce el lado del cuadrado: ")

    # imputs
    figuras = [
        Circulo(color=color_circulo, radio=radio_circulo),
        Cuadrado(color=color_cuadrado, lado=lado_cuadrado),
    ]
 
    print("\n=== Cálculo de áreas de figuras geométricas ===\n")
    for figura in figuras:
        figura.mostrar_info()
 
if __name__ == "__main__":
    main()