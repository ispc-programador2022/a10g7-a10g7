from producto.py import producto #para utilizar el producto
from suma.py import suma #para utilizar la suma

def p1(a, b, c):
    p = producto(a, b)
    return suma(p, c)