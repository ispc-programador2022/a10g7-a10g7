from genrnd import genrnd
from suma import suma

suma_permutaciones=[]

def suma_random(genrnd):
    lista = genrnd()
    for i in range(50):
        for j in range(50):
            if(i!=j):
                n=suma(lista[i],lista[j])
                suma_permutaciones.append(n)
    print(suma_permutaciones)
