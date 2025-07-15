'''
IMPRIMIR LOS PRIMERO N numero pares; indicar al final cuanto suman
ANALISIS:
   ENTRADAS: n
   PROCESOS: par = contador * 2
   SALIDAS :  par
'''

par = 0
n = 0
suma = 0

n = int(input("CUANTOS PARES: "))

contador = 1
while (contador <= n):
    par = contador * 2
    print(par)
    suma = suma + par
    contador = contador + 1

#salida en tiempo total
print (f"SUMATORIA DE PARES: {suma}")