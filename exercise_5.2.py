contador = 0
suma = 0
minimo = 0
maximo = 0
primerNumero = True
while True:
    try:
        numero = input("Ingrese un número: ")
        if (numero == "salir"):
            break
        else:
            contador = contador + 1
            suma = suma + int(numero)
            if (primerNumero):
                minimo = int(numero)
                maximo = minimo
                primerNumero = False
            else:
                if (int(numero) > maximo): 
                    maximo = int(numero)
                if (int(numero) < minimo):
                    minimo = int(numero)
    except:
        print("Debe ingresar un valor numérico")
        contador = contador - 1
        continue
print("Contador:", contador)
print("Suma:", suma)
print("Promedio:", suma/contador)
print("Mínimo:", minimo)
print("Máximo:", maximo)