
from empleado import Empleado
 
 
class Gerente(Empleado):
    """Representa a un gerente. Hereda todos los campos de Empleado
    y agrega el campo propio 'porcentaje_bono'."""
 
    def __init__(self, nombre: str, apellido: str, edad: int,
                 cargo: str, salario: float, porcentaje_bono: float = 0.20):
        super().__init__(nombre, apellido, edad, cargo, salario)
        self.__porcentaje_bono = porcentaje_bono 
 
    @property
    def porcentaje_bono(self) -> float:
        return self.__porcentaje_bono
 
    @porcentaje_bono.setter
    def porcentaje_bono(self, nuevo_porcentaje: float):
        if not (0 <= nuevo_porcentaje <= 1):
            raise ValueError("El porcentaje de bono debe estar entre 0 y 1.")
        self.__porcentaje_bono = nuevo_porcentaje
 
    def calcular_bono(self) -> float:
        """Calcula el bono del gerente como un porcentaje de su salario."""
        return self.salario * self.__porcentaje_bono
 
    def mostrar_info(self) -> None:
        """Extiende mostrar_info() de la clase base añadiendo el bono."""
        super().mostrar_info()
        print(f"Bono     : S/ {self.calcular_bono():.2f} "
              f"({self.__porcentaje_bono * 100:.0f}% del salario)")