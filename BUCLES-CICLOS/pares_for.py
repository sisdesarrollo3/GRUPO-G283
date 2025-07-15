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

#BUCLE    variable control inicia en un valor
#         variable control es comparada con el valor final
#         variable control debe ser incrementada
# todo bucle se ejecuta mientras la condicion sea VERDADERO, sale por FALSO    
for contador in range (1, n+1, 1):
    par = contador * 2
    print(par)    #salida en tiempo parcial
    suma += par

#salida en tiempo total
print (f"SUMATORIA DE PARES: {suma}")