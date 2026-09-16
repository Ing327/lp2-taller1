"""
Rutas (vistas) de la Tienda Virtual.
"""

import json
import os

from flask import Blueprint, render_template, abort

# Blueprint principal
main = Blueprint("main", __name__)

# Ruta al archivo productos.json
RUTA_PRODUCTOS = os.path.join(
    os.path.dirname(__file__),
    "data",
    "productos.json"
)


def cargar_productos():
    """
    Lee productos.json y retorna la lista de productos.
    """

    with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    return productos


def buscar_producto_por_sku(sku):
    """
    Busca un producto por su SKU.
    """

    productos = cargar_productos()

    for producto in productos:
        if producto["sku"] == sku:
            return producto

    return None


@main.route("/")
def index():
    """
    Página principal: muestra el catálogo completo.
    """

    productos = cargar_productos()

    return render_template(
        "index.html",
        productos=productos
    )


@main.route("/producto/<sku>")
def detalle(sku):
    """
    Página de detalle de un producto específico.
    """

    producto = buscar_producto_por_sku(sku)

    if producto is None:
        abort(404)

    return render_template(
        "detalle.html",
        producto=producto
    )