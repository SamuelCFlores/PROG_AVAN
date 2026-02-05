class Producto:
    def __init__(self,nom, prec, stok):
        self.nombre = nom
        self.precio = prec
        self.stock = stok
    
    def aplicar_descuento(self, porcentaje):
       self.precio*=(1-porcentaje)
       print(f"El nuevo precio con descuento es: {self.precio}")

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad) < 0:
            print("No hay suficiente stock disponible.")
        else:
            self.stock += cantidad
            print(f"El stock actualizado de {self.nombre} es: {self.stock}")

class Categoria:
    def __init__(self, nom_cat):
        self.nombre_categoria = nom_cat
        self.lista = []
    
    def agregar_producto(self, producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} ha sido agregado a la categoría {self.nombre_categoria}.")

    def valor_total(self):
        pass

        
    
    