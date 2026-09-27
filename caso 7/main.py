from empleado import Empleado
from gerente import Gerente



def main():
    print("=== Configuración del Empleado ===")
    nombre_emp = input("Introduce el nombre del empleado: ")
    apellido_emp = input("Introduce el apellido del empleado: ")
    edad_emp = int(input("Introduce la edad del empleado: "))
    cargo_emp = input("Introduce el cargo del empleado: ")
    salario_emp = float(input("Introduce el salario del empleado en S/ (ej. 2500.00): "))

    print("\n=== Configuración del Gerente ===")
    nombre_ger = input("Introduce el nombre del gerente: ")
    apellido_ger = input("Introduce el apellido del gerente: ")
    edad_ger = int(input("Introduce la edad del gerente: "))
    cargo_ger = input("Introduce el cargo del gerente: ")
    salario_ger = float(input("Introduce el salario del gerente en S/ (ej. 6000.00): "))
    bono_ger = float(input("Introduce el porcentaje de bono (ej. 0.25 para 25%): "))

    # Creación de objetos con los datos ingresados
    empleado = Empleado(
        nombre=nombre_emp,
        apellido=apellido_emp,
        edad=edad_emp,
        cargo=cargo_emp,
        salario=salario_emp
    )

    gerente = Gerente(
        nombre=nombre_ger,
        apellido=apellido_ger,
        edad=edad_ger,
        cargo=cargo_ger,
        salario=salario_ger,
        porcentaje_bono=bono_ger
    )

    print("\n=== Información del Empleado ===\n")
    empleado.mostrar_info()

    print("\n=== Información del Gerente ===\n")
    gerente.mostrar_info()

    print("\n=== Cálculo del bono del Gerente ===\n")
    print(f"El bono de {gerente.nombre} {gerente.apellido} es: "
          f"S/ {gerente.calcular_bono():.2f}")


if __name__ == "__main__":
    main()