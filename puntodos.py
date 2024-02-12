import math
radio= int(input("Ingrese el radio del circulo: "))
tipo= input("En centimetros, metros o cual unidad de medida: ")
area = (math.pi) * (radio**2)

print("El Area es:", area, tipo)