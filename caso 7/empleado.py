class Empleado:
 
    def __init__(self, nombre: str, apellido: str, edad: int,
                 cargo: str, salario: float):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__cargo = cargo
        self.__salario = salario
 
    @property
    def nombre(self) -> str:
        return self.__nombre
 
    @property
    def apellido(self) -> str:
        return self.__apellido
 
    @property
    def edad(self) -> int:
        return self.__edad
 
    @property
    def cargo(self) -> str:
        return self.__cargo
 
    @property
    def salario(self) -> float:
        return self.__salario
 

    @edad.setter
    def edad(self, nueva_edad: int):
        if nueva_edad <= 0:
            raise ValueError("La edad debe ser un número positivo.")
        self.__edad = nueva_edad
 
    @salario.setter
    def salario(self, nuevo_salario: float):
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = nuevo_salario
 

    def mostrar_info(self) -> None:
        """Imprime la información del empleado.
        Las subclases pueden extenderla (herencia)."""
        print(f"Nombre   : {self.nombre} {self.apellido}")
        print(f"Edad     : {self.edad} años")
        print(f"Cargo    : {self.cargo}")
        print(f"Salario  : S/ {self.salario:.2f}")