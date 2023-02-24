def addDrink(drink):
    if len(drink) >= 2 and len(drink) <= 15:
        print("Dentro del primer if")
        strDrink = drink.split()
        print(strDrink)

        for drk in strDrink:
            if drk.isalpha() == False:
                return "No se puede agregar la bebida"
        
        return "Se agrego bebida"

    
    return "No se puede agregar la bebida"

def addSizes(sizes):
    if len(sizes) < 1:
        return "Debe de intruducir minimo un tamaño"
    elif len(sizes) <= 5:
        lastSize = 0
        for size in sizes:
            try:
                size = float(size)
            except ValueError:
                return "Uno de los valores para el tamaño no es un entero"

            intSize = int(size)
            if size - intSize != 0:
                return "Uno de los valores para el tamaño no es un entero"
            
            if size < 1 or size > 48: 
                return "Se ingreso un tamaño no valido"
            elif lastSize < size:
                lastSize = size
            else:
                return "Los tamaños no estan de forma ascendente"

        return "Se agregaron los tamaños"
    else:
        return "Se exedio de numero de tamaños"

def add(str):
    lst = str.split(",")
    strDrink = addDrink(lst[0])

    if strDrink == "Se agrego bebida":
        lst.pop(0)
        return strDrink + "\n" +  addSizes(lst)
    else:
        return strDrink

#add(input())

