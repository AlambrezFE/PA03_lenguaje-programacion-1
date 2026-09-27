from animal import Animal
 
 
class Mamifero(Animal):
 
    def __init__(self, nombre: str, especie: str, pelo: str):
        super().__init__(nombre, especie)  
        self.__pelo = pelo 
 
    @property
    def pelo(self) -> str:
        return self.__pelo
 
    @pelo.setter
    def pelo(self, nuevo_pelo: str):
        if not nuevo_pelo or not isinstance(nuevo_pelo, str):
            raise ValueError("El tipo de pelo debe ser un texto no vacío.")
        self.__pelo = nuevo_pelo
 
    def hacer_sonido(self) -> str:
        """Sobrescribe (override) el método de la clase base."""
        return "emite un rugido o gruñido"
 
    def amamantar(self) -> None:
        """Método propio de los mamíferos."""
        print(f"{self.nombre} está amamantando a sus crías.")
 
    def mostrar_info(self) -> None:
        """Extiende mostrar_info() de la clase base añadiendo el pelo."""
        super().mostrar_info()
        print(f"Pelo    : {self.pelo}")
 