def radicacion(a, b):
    if b % 2 == 0:
        if a < 0:
            print("No se puede calcular pues la base es menor que 0")
        else:
            return a**(1/b)
    else:
        return a**(1/b)
