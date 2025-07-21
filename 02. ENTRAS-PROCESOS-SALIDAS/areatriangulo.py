
'''
 HALLAR el area de un triangulo
'''
print('*' * 50)
print('PROGRAMA AREA DEL TRIANGULO')
print('*' * 50)
#1. reservar e inicializar variables
base = 0
altura = 0
area = 0

#2. Entradas por teclado con input
base = float(input("BASE: "))
altura = float(input("ALTURA: "))

#3. Procesos
area = base * altura / 2

#4. salidas con print
print('\n\n')
print("BASE ALTURA AREA")
print('=' * 50)
print(f"{base} \t {altura} \t {area}")
print('=' * 50)