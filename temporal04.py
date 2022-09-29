while True:
    vegetal = input("Ingrese el tipo de vegetal: ")
    if (vegetal == "salir"):
        break
    else:
        if (vegetal == "hortaliza"):
            print("Ejemplo: Maíz")
        elif (vegetal == "frutal"):
            print("Ejemplo: Mango")
        elif (vegetal == "ornamental"):
            print("Ejemplo: Rosal")
        else:
            print("No definido")