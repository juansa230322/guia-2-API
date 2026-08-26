from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from decimal import Decimal

app = FastAPI(
    title="API de Productos",
    description="API REST para administrar productos de una empresa.",
    version="1.0.0"
)


class Producto(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, description="Nombre obligatorio")
    categoria: str
    precio: Decimal = Field(..., gt=0, description="Precio mayor que cero")
    stock: int = Field(..., ge=0, description="Stock no negativo")


productos = [
    Producto(id=1, nombre="Laptop Lenovo", categoria="Tecnología",
             precio=2500000, stock=10),
    Producto(id=2, nombre="Mouse inalámbrico", categoria="Accesorios",
             precio=85000, stock=25)
]


@app.get("/productos", response_model=list[Producto],
         summary="Consultar todos los productos")
def obtener_productos():
    return productos


@app.get("/productos/{id}", response_model=Producto,
         summary="Consultar un producto por ID")
def obtener_producto(id: int):
    for producto in productos:
        if producto.id == id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.post("/productos", response_model=Producto, status_code=201,
          summary="Registrar un producto")
def crear_producto(producto: Producto):
    for producto_existente in productos:
        if producto_existente.id == producto.id:
            raise HTTPException(status_code=400,
                                detail="El ID del producto ya existe")
    productos.append(producto)
    return producto


@app.put("/productos/{id}", response_model=Producto,
         summary="Actualizar un producto")
def actualizar_producto(id: int, producto_actualizado: Producto):
    for indice, producto in enumerate(productos):
        if producto.id == id:
            if producto_actualizado.id != id:
                for producto_existente in productos:
                    if producto_existente.id == producto_actualizado.id:
                        raise HTTPException(
                            status_code=400,
                            detail="El nuevo ID ya existe"
                        )
            productos[indice] = producto_actualizado
            return producto_actualizado

    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.delete("/productos/{id}", summary="Eliminar un producto")
def eliminar_producto(id: int):
    for indice, producto in enumerate(productos):
        if producto.id == id:
            productos.pop(indice)
            return {
                "mensaje": "Producto eliminado correctamente",
                "id": id
            }

    raise HTTPException(status_code=404, detail="Producto no encontrado")
