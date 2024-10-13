from orden import *
from pizza import *
from pizza_variedad import *
from mozo import *
from maestro_pizzero import *
from utils import *
from random import shuffle

class TesterPizzeria:
    
    def main(self):
        Utils.limpiar_consola()
        maestro_pizzero = MaestroPizzero("Gallardo")
        
        # Creo los mozos 
        mozo1 = Mozo("Pablo")
        mozo2 = Mozo("Juan")
        mozos = [mozo1, mozo2]
        
        var_muzza = PizzaVariedad("Muzzarella", 4500)
        var_calabresa = PizzaVariedad("Calabresa", 6000)
        var_panceta_verdeo = PizzaVariedad("Panceta y Verdeo", 5500)
        var_especial = PizzaVariedad("Especial", 7000)
        var_caballo = PizzaVariedad("Caballo", 7900)
        
        pizza1 = Pizza(var_muzza)
        pizza2 = Pizza(var_calabresa)
        pizza3 = Pizza(var_caballo)
        pizza4 = Pizza(var_panceta_verdeo)
        pizza5 = Pizza(var_muzza)
        pizza6 = Pizza(var_caballo)
        pizza7 = Pizza(var_caballo)
        pizza8 = Pizza(var_panceta_verdeo)
        
        # Creo dos ordenes
        pizzas_orden_1 = [pizza1, pizza2, pizza3]
        pizzas_orden_2 = [pizza4, pizza5]
        orden_mesa_1 = Orden(11111, pizzas_orden_1)
        orden_mesa_2 = Orden(11112, pizzas_orden_2)
        
        # Le mando las dos ordenes al maestro pizzero
        maestro_pizzero.tomarPedido(orden_mesa_1)
        maestro_pizzero.tomarPedido(orden_mesa_2)
        
        # Imprimo las ordenes del maestro pizzero, tambien imprimo su estado
        print(f"ORDENES DEL MAESTRO PIZZERO {maestro_pizzero.obtenerNombre().upper()}")
        for orden in maestro_pizzero.obtenerOrdenes() :
            print(orden)
        print(Utils.sepearador_decorativo_consola())
        
        # Mando a cocinar todas las ordenes que tiene el maestro pizzero
        print("Cocinando..."); maestro_pizzero.cocinar()
        print(Utils.sepearador_decorativo_consola())
        
        # Despues de cocinar imprimo las ordenes del maestro pizzero, tambien imprimo su estado 
        print(f"ORDENES DEL MAESTRO PIZZERO {maestro_pizzero.obtenerNombre().upper()}")
        for orden in maestro_pizzero.obtenerOrdenes() :
            print(orden)
        print(Utils.sepearador_decorativo_consola())
        
        # Agrego una nueva orden
        maestro_pizzero.tomarPedido(Orden(11113, [pizza6, pizza7, pizza8]))
        print(f"ORDENES DEL MAESTRO PIZZERO {maestro_pizzero.obtenerNombre().upper()}")
        for orden in maestro_pizzero.obtenerOrdenes() :
            print(orden)
        print(Utils.sepearador_decorativo_consola())

        # Por cada orden lista para entregar, se la mando al maestro pizzero que la entrege
        for orden in maestro_pizzero.obtenerOrdenes() :
            if orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR :
                # Hago esto para elegir un mozo al azar y que no siempre use el mismo mozo para todas las ordenes
                shuffle(mozos)  # Mezcla la lista de mozos
                mozo_seleccionado = mozos[0]  # Selecciona el primer mozo de la lista mezclada
                
                while orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR :
                    mozo_seleccionado.tomarPizzas(maestro_pizzero.entregar(orden))
                    mozo_seleccionado.servirPizzas()
                
                print(f"El total de la orden es: {orden.calcularTotal()} \n")
        print(Utils.sepearador_decorativo_consola())
            
        # Imprimo 
        print(f"ORDENES DEL MAESTRO PIZZERO {maestro_pizzero.obtenerNombre().upper()}")
        for orden in maestro_pizzero.obtenerOrdenes() :
            print(orden)
        print(Utils.sepearador_decorativo_consola())

        
        # Mando a cocinar todas las ordenes que tiene el maestro pizzero
        print("Cocinando...."); maestro_pizzero.cocinar()
        print(Utils.sepearador_decorativo_consola())
        
        # Por cada orden lista para entregar, se la mando al maestro pizzero que la entrege
        for orden in maestro_pizzero.obtenerOrdenes() :
            if orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR :
                # Hago esto para elegir un mozo al azar y que no siempre use el mismo mozo para todas las ordenes
                shuffle(mozos)  # Mezcla la lista de mozos
                mozo_seleccionado = mozos[0]  # Selecciona el primer mozo de la lista mezclada
                
                while orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR :
                    mozo_seleccionado.tomarPizzas(maestro_pizzero.entregar(orden))
                    mozo_seleccionado.servirPizzas()
                
                print(f"El total de la orden es: {orden.calcularTotal()} \n")
        print(Utils.sepearador_decorativo_consola())
            
        # Imprimo 
        print(f"ORDENES DEL MAESTRO PIZZERO {maestro_pizzero.obtenerNombre().upper()}")
        for orden in maestro_pizzero.obtenerOrdenes() :
            print(orden)
        print(Utils.sepearador_decorativo_consola())
            
            
    
    
if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()