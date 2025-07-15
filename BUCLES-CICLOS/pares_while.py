'''
IMPRIMIR LOS PRIMERO N numero pares; indicar al final cuanto suman
ANALISIS:
   ENTRADAS: n
   PROCESOS: par = contador * 2
   SALIDAS :  par
'''
#BUCLE    variable control inicia en un valor  CONTADOR
#         variable control es comparada con el valor final CONTADOR
#         variable control debe ser incrementada  CONTADOR
# todo bucle se ejecuta mientras la condicion sea VERDADERO, sale por FALSO

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