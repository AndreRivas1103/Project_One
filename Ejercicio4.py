def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(imput("ingrese un numero "))
resultado= par_o_impar(numero)
print("El numero ", numero, "es ", resultado)