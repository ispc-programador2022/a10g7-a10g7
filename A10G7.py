#import funciones
from archivos.welcome import welcome
from archivos.ing2i import ing2i
from archivos.ing2s import ing2s
from archivos.producto import producto
from archivos.cociente import cociente
#mensaje de bienvenida
print(welcome())
#numeros enteros y strings
int_import=ing2i()
strings_import=ing2s()
#muestro lo ingresado
print('Los numeros enteros ingresados son:', int_import[0],'y',int_import[1])
print('Los strings ingresados son:',strings_import[0],'y',  strings_import[1])
