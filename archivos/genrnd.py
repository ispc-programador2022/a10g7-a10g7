import random
def genrnd():
    lista_num=[]
    for x in range(50):
         num=random.randint(1,100)
         lista_num.append(int(num))
    return lista_num
