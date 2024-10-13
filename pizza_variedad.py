class PizzaVariedad:
    def __init__(self, nomVar: str, pre: float):
        self.__nombreVariedad = nomVar
        self.__precio = pre 
        
    def establecerNombreVariedad(self, nomVar: str) :
        self.__nombreVariedad = nomVar
        
    def establecerPrecio(self, pre: float) :
        self.__precio = pre
        
    def obtenerNombreVariedad(self) -> str :
        return self.__nombreVariedad
    
    def obtenerPrecio(self) -> float :
        return self.__precio
    
    def __str__(self) -> str:
        return f"Variedad: {self.__nombreVariedad}, Precio: {self.__precio}"