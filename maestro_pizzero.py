from pizza import Pizza
from orden import Orden

class MaestroPizzero:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes: list[Orden] = []

    def establecerNombre(self, nom: str) :
        self.__nombre = nom

    def tomarPedido(self, orden: Orden) :            
        self.__ordenes.append(orden)

    def cocinar(self):
        for orden in self.__ordenes :
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL :
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtenerPizzas() :
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)

    def entregar(self, orden: Orden) -> list[Pizza]:
        pizzas_de_la_orden = orden.obtenerPizzas()
        pizzas_entregadas = []
        
        cant_pizzas_entregadas = 1
        for pizza in pizzas_de_la_orden :
            if pizza.obtenerEstado() != Pizza.ESTADO_ENTREGADA and cant_pizzas_entregadas <= 2 :
                pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
                pizzas_entregadas.append(pizza)
                cant_pizzas_entregadas += 1
        
            
        # Compruebo si todas las pizzas estan en estado finalizado
        for i in range(len(pizzas_de_la_orden)) :
            if pizzas_de_la_orden[i].obtenerEstado() == Pizza.ESTADO_ENTREGADA :
                if i == len(pizzas_de_la_orden) - 1 :
                    orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)
                 
                
        return pizzas_entregadas


    def obtenerNombre(self) -> str :
        return self.__nombre
    
    def obtenerOrdenes(self) -> list[Orden] :
        return self.__ordenes