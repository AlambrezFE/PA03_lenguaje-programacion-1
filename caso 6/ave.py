from animal import Animal
 
 
class Ave(Animal):
 
    def __init__(self, nombre: str, especie: str, plumas: str):
        super().__init__(nombre, especie)
        self.__plumas = plumas  
 
    @property
    def plumas(self) -> str:
        return self.__plumas
 
    @plumas.setter
    def plumas(self, nuevas_plumas: str):
        if not nuevas_plumas or not isinstance(nuevas_plumas, str):
            raise ValueError("El color/tipo de plumas debe ser un texto no vacío.")
        self.__plumas = nuevas_plumas
 
    def hacer_sonido(self) -> str:
        return "emite un canto o trino"
 
    def volar(self) -> None:
        """Método propio de las aves."""
        print(f"{self.nombre} está volando.")
 
    def mostrar_info(self) -> None:
        """Extiende mostrar_info() de la clase base añadiendo las plumas."""
        super().mostrar_info()
        print(f"Plumas  : {self.plumas}")