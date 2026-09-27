class Animal:

    def __init__(self, nombre: str, especie: str):
        self.__nombre = nombre
        self.__especie = especie
 
# getters 
    @property
    def nombre(self) -> str:
        return self.__nombre
 
    @property
    def especie(self) -> str:
        return self.__especie

 # validacion 
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre or not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser un texto no vacío.")
        self.__nombre = nuevo_nombre
 
    @especie.setter
    def especie(self, nueva_especie: str):
        if not nueva_especie or not isinstance(nueva_especie, str):
            raise ValueError("La especie debe ser un texto no vacío.")
        self.__especie = nueva_especie
 
    # Métodos 
    def hacer_sonido(self) -> str:
        return "hace un sonido"
 
    def mostrar_info(self) -> None:
        print(f"Nombre  : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Sonido  : {self.hacer_sonido()}")