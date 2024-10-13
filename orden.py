from pizza import * 

class Orden ():
    # Atr de clase
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
    # Atr de instancia - Constructores
    def __init__(self, nro: int, pizzas: list[Pizza]) -> None:
        self.__nroOrden = nro
        self.__pizzas = pizzas
        self.__estadoOrden = self.ESTADO_INICIAL
        
    # Comandos
    def establecerNroOrden(self, nro: int) -> None:
        self.__nroOrden = nro
    
    def establecerPizzas(self, pizzas: list[Pizza]) -> None:
        self.__pizzas = pizzas
    
    def establecerEstadoOrden(self, est: int) -> None:
        self.__estadoOrden = est
    
    # Consultas
    def obtenerNroOrden(self) -> int:
        return self.__nroOrden
    
    def obtenerPizzas(self) -> list[Pizza]:
        return self.__pizzas
    
    def obtenerEstadoOrden(self) -> int:
        return self.__estadoOrden
    
    def obtenerEstadoOrdenDescripcion(self) -> str :
        """ Metodo para  """
        if self.__estadoOrden == self.ESTADO_INICIAL:
            return "Estado inicial"
        elif self.__estadoOrden == self.ESTADO_PARA_ENTREGAR:
            return "Lista para entregar"
        elif self.__estadoOrden == self.ESTADO_ENTREGADA:
            return "Entregada ✅"
    
    def calcularTotal(self) -> float:
        """ La consulta calcularTotal debe calcular el costo total de la orden. Esto debe
        hacerse recorriendo los objetos de tipo Pizza ligados a dicha orden y
        acumulando el costo que tiene cada variedad de pizza. """
        
        total = 0.0
        for pizza in self.__pizzas :
            total += pizza.obtenerVariedad().obtenerPrecio()
        
        return total
    
    def __str__(self) -> str:
        rta = f"ORDEN N {self.__nroOrden}. Estado: {self.obtenerEstadoOrdenDescripcion()} \n Pizzas en esta orden :"
        for pizza in self.__pizzas:
            rta += f"\n * {pizza}. Estado: {pizza.obtenerEstadoDescripcion()}"
        return rta