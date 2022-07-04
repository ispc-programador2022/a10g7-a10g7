from genrnd import genrnd
from producto import producto

prod_permutaciones=[]

def suma_random(genrnd):
    lista = genrnd()
    for i in range(50):
        for j in range(50):
            if(i!=j):
                n=producto(lista[i],lista[j])
                prod_permutaciones.append(n)
    print(prod_permutaciones)
