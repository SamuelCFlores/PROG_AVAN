from inventario_techstore import *

prod1 = Producto("Maruchan", 16, 100)
prod2 = Producto("Nesquik", 45, 50)  # bebida en polvo conocida de Nestlé :contentReference[oaicite:0]{index=0}
prod3 = Producto("Capri-Sun", 22, 80)  # bebida de jugo popular :contentReference[oaicite:1]{index=1}
prod4 = Producto("Arroz", 30, 200)
prod5 = Producto("Aceite de oliva", 120, 60)
prod6 = Producto("Café soluble", 70, 90)
prod7 = Producto("Agua sin gas", 12, 300)
prod8 = Producto("Atún en lata", 28, 120)
prod9 = Producto("Avena", 35, 110)
prod10 = Producto("Pan de caja", 25, 150)
prod11 = Producto("Huevos (docena)", 40, 100)
prod12 = Producto("Leche", 28, 180)
prod13 = Producto("Frijoles", 22, 140)
prod14 = Producto("Aceite vegetal", 50, 100)
prod15 = Producto("Sal de mesa", 10, 160)
prod16 = Producto("Pasta para sopa", 18, 130)
prod17 = Producto("Tomate enlatado", 32, 90)
prod18 = Producto("Azúcar", 24, 150)
prod19 = Producto("Refresco 2L", 28, 100)
prod20 = Producto("Leche condensada", 45, 70)

cat1 = Categoria("Alimentos")

cat1.agregar_producto(prod1)
cat1.agregar_producto(prod4)
cat1.agregar_producto(prod8)
cat1.agregar_producto(prod9)
cat1.agregar_producto(prod10)
cat1.agregar_producto(prod11)

print(f"Productos en la categoría {cat1.nombre_categoria}:")
for producto in cat1.lista:
    print(f"- {producto.nombre}")

