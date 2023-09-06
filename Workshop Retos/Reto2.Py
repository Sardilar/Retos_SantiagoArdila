Productos = {
    1: {"id": 123, "nombre": "libreta", "precio": 12.500, "id_Cat": 1},
    2: {"id": 345, "nombre": "jabon", "precio": 10.500, "id_Cat": 2},
}

Categorias = {
    1: {"id": 1, "nombre": "utiles escolares"},
    2: {"id": 2, "nombre": "aseo"},
}

def obtener_producto_con_categoria(Productos, Categorias, ProductoID):
    Producto = Productos.get(ProductoID)
    if Producto:
        CategoriaID = Producto["id_Cat"]
        Categoria = Categorias.get(CategoriaID)
        if Categoria:
            return {
                "nombre_producto": Producto["nombre"],
                "nombre_categoria": Categoria["nombre"],
            }
    return None

for ProductoID in Productos:
    resultado = obtener_producto_con_categoria(Productos, Categorias, ProductoID)
    if resultado:
        print(f"Nombre del producto: {resultado['nombre_producto']}")
        print(f"Nombre de la categoría: {resultado['nombre_categoria']}")
        print("-" * 30)
    else:
        print(f"El producto con ID {ProductoID} no se encontró o la categoría asociada no existe.")

