from abc import ABC

# Observer Pattern
class Observer(ABC):

    def update(self):
        pass
#Se define la clase abstracta Observer, que define un método abstracto update(). Este método será implementado por las clases concretas que actúan como observadores.


class CartObserver(Observer):
    def __init__(self, cart):
        self.cart = cart


    def update(self):
        print("Carrito actualizado:")
        self.cart.show_items()
#Se define una clase concreta CartObserver, que actúa como observador del carrito de compras. Implementa el método update() para imprimir el mensaje "Carrito actualizado:" y mostrar los ítems del carrito.

# Singleton Pattern
class Store:
    _instance = None

    def __new__(clss):
        if clss._instance is None:
            clss._instance = super().__new__(clss)
            clss._instance.products = []
            clss._instance.observers = []
        return clss._instance
#Se define la clase Store, que implementa el patrón Singleton. Garantiza que solo haya una instancia de la tienda en toda la aplicación.

    def add_product(self, producto):
        self.products.append(producto)
        self.notify_observers()

    def get_products(self):
        return self.products

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()
#Se definen métodos para agregar productos a la tienda, obtener la lista de productos, adjuntar observadores y notificar a los observadores cuando se agregan nuevos productos.

# Strategy Pattern
class PricingStrategy(ABC):
    
    def calcular_precio(self, precio):
        pass

class NormalPricingStrategy(PricingStrategy):
    def calcular_precio(self, precio):
        return precio
#Esto permite calcular el precio de los productos.

# Polimorfismo
class Product:
    def __init__(self, nombre, descripcion, precio, strategy):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = strategy.calcular_precio(precio)
#se define la clase Product, que representa un producto en la tienda. Utiliza el polimorfismo al recibir una estrategia de precios y calcular el precio del producto teniendo en cuenta esta estrategia.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def show_items(self):
        total_precio = 0
        for producto, cantidad in self.items:
            print(f"{producto.nombre} - {producto.descripcion} - {producto.precio} x {cantidad}")
            total_precio += producto.precio * cantidad
        print(f"Precio total: {total_precio}")
#Se define la clase ShoppingCart, que representa el carrito de compras.asi se puede agregar ítems al carrito y mostrar los ítems y el precio total.

# Ejemplo de uso
if __name__ == "__main__":
    store = Store()

    # elegimos productos y los añadimos al carrito
    normal_strategy = NormalPricingStrategy()
 

    product1 = Product("Camisa", "Camisa de millonarios", 90, normal_strategy)
    product2 = Product("Pantalón", "Pantalón en lana negro", 110, normal_strategy)
    store.add_product(product1)
    store.add_product(product2)

    # Observador para el carrito 
    cart = ShoppingCart()
    cart_observer = CartObserver(cart)
    store.attach(cart_observer)

    # Añadimos productos al carrito
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    # Mostramos los productos en el carrito
    cart.show_items()
