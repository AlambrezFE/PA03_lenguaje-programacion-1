
from figura_geometrica import FiguraGeometrica
 
 
class Cuadrado(FiguraGeometrica):
    """Representa un cuadrado. Hereda tipo y color de FiguraGeometrica."""
 
    def __init__(self, color: str, lado: float):
        super().__init__(tipo="Cuadrado", color=color)  # Herencia
        self.__lado = None
        self.lado = lado  

    @property
    def lado(self) -> float:
        return self.__lado
 
    @lado.setter
    def lado(self, valor: float):
        if valor <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self.__lado = valor
 
    def calcular_area(self) -> float:
        """Implementación del método abstracto: área = lado^2."""
        return self.__lado ** 2
 