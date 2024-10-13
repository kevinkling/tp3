from pizza_variedad import *

class Pizza:
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: PizzaVariedad) :
        self.__variedad = var
        self.__estado = self.ESTADO_POR_COCINAR

    def establecerVariedad(self, var: PizzaVariedad) :
        self.__variedad = var
        
    def establecerEstado(self, est: int) :
        self.__estado = est

    def obtenerVariedad(self) -> PizzaVariedad :
        return self.__variedad
    
    def obtenerEstado(self) -> int :
        return self.__estado
    
    def obtenerEstadoDescripcion(self) -> str :
        if self.__estado == self.ESTADO_POR_COCINAR:
            return "Por cocinar"
        elif self.__estado == self.ESTADO_COCINADA:
            return "Cocinada"
        elif self.__estado == self.ESTADO_ENTREGADA:
            return "Entregada"
    
    def __str__(self):
        return f"{self.__variedad.obtenerNombreVariedad()}"
    
    