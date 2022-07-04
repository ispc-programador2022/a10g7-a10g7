from genrnd import genrnd
from suma import suma

def media(genrnd):
    lista = genrnd()
    n = 0
    for i in range(50):
        n=suma(n,lista[i])
    media=n/50
    print(media)
