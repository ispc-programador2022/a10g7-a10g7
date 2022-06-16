#defino función ing2i
def ing2i():
    while True:
            int1 = input("Ingrese su primer numero entero:")
            int2 = input("Ingrese su segundo numero entero: ")
            try:
                int1=int(int1)
                int2=int(int2)
                return[int1,int2]
            except ValueError:
                print("Entrada no valida. Escribe un numero entero")
                continue
