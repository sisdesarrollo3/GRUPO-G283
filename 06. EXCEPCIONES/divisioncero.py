
x = 6
y = 0
try:
    # Código que puede causar una excepción
    z = x / y
except ZeroDivisionError:
    # Manejo de la excepción
    print("¡No puedes dividir entre cero!")   

print("el programa continua") 