"""
Contiene la clase abstracta FiguraGeometrica, que define el
comportamiento y los atributos comunes a toda figura geométrica.
"""
 
from abc import ABC, abstractmethod
 
 
class FiguraGeometrica(ABC):
 
    def __init__(self, tipo: str, color: str):
        # Atributos privados, osea es la encapsulación
        self.__tipo = tipo
        self.__color = color
 
    # (getters)
    @property
    def tipo(self) -> str:
        return self.__tipo
 
    @property
    def color(self) -> str:
        return self.__color
 
    #Setter con validación
    @color.setter
    def color(self, nuevo_color: str):
        if not nuevo_color or not isinstance(nuevo_color, str):
            raise ValueError("El color debe ser un texto no vacío.")
        self.__color = nuevo_color
 
    #Método abstracto
    @abstractmethod
    def calcular_area(self) -> float:
        """Debe ser implementado por cada subclase."""
        pass
 
    #Método común (herencia)
    def mostrar_info(self) -> None:
       # Muestra la información de la figura y su área calculada.
        print(f"Figura   : {self.tipo}")
        print(f"Color    : {self.color}")
        print(f"Área     : {self.calcular_area():.2f}")
        print("-" * 30)