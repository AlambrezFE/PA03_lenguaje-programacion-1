 
import math
from figura_geometrica import FiguraGeometrica
 
 
class Circulo(FiguraGeometrica):
    """Representa un círculo. Hereda tipo y color de FiguraGeometrica."""
 
    def __init__(self, color: str, radio: float):
        super().__init__(tipo="Círculo", color=color)  # Herencia
        self.__radio = None
        self.radio = radio 
 
    @property
    def radio(self) -> float:
        return self.__radio
 
    @radio.setter
    def radio(self, valor: float):
        if valor <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.__radio = valor
 
    def calcular_area(self) -> float:
        """Implementación del método abstracto: área = π r^2."""
        return math.pi * (self.__radio ** 2)
 