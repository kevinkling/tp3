from pizza import * 

class Mozo:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__pizzas: list[Pizza] = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPizzas(self, pizzas: list[Pizza]):
        pizzasTomadas = len(self.__pizzas)
        pizzasATomar = len(pizzas)
        if (pizzasATomar - pizzasTomadas) < 0:
            print(self.__nombre + ": El mozo puede tomar un máximo de 2 pizzas!")
        else:
            for pizza in pizzas:
                print(self.__nombre + ": tomando una de " + str(pizza.obtenerVariedad()) + " para ser entregada")
                self.__pizzas.append(pizza)
    
    def servirPizzas(self) -> None:
        for pizza in self.__pizzas:
            print(self.__nombre + ": Sirviendo pizza de " + str(pizza.obtenerVariedad()))
        self.__pizzas = []

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerPizzas(self) -> list[Pizza]:
        return self.__pizzas
    
    def obtenerEstadoLibre(self) -> bool:
        return len(self.__pizzas) == 0

    def __str__(self) -> str:
        return self.__nombre