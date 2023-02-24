from cafeteria import *

#Tests para las bebidas
def testB1 ():
    assert addDrink("Ca") == "Se agrego bebida"

def testB2 ():
    assert addDrink("C") == "No se puede agregar la bebida"

def testB3 ():
    assert addDrink("abcdefghijklmno") == "Se agrego bebida"

def testB4 ():
    assert addDrink("abcdefghijklmnop") == "No se puede agregar la bebida"

def testB5 ():
    assert addDrink("Red Cola") == "Se agrego bebida"

def testB6 ():
    assert addDrink("adkjasde ajsdiwe widjwjd") == "No se puede agregar la bebida"

def testB7 ():
    assert addDrink("") == "No se puede agregar la bebida"

def testB8 ():
    assert addDrink("Red Cola3") == "No se puede agregar la bebida"

def testB9 ():
    assert addDrink("Red Cola 3") == "No se puede agregar la bebida"

#Tests para tamaños
def testT1 ():
    assert addSizes([1,2,3,4,5]) == "Se agregaron los tamaños"

def testT2 ():
    assert addSizes([1,2,0,4,5]) == "Se ingreso un tamaño no valido"

def testT3 ():
    assert addSizes([1,2,3,49,5]) == "Se ingreso un tamaño no valido"

def testT4 ():
    assert addSizes([1,48]) == "Se agregaron los tamaños"

def testT5 ():
    assert addSizes([1,2,3,4,5,6]) == "Se exedio de numero de tamaños"

def testT6 ():
    assert addSizes([1,2,4,3,5]) == "Los tamaños no estan de forma ascendente"

def testT7 ():
    assert addSizes([1,2,3,5,4,6]) == "Se exedio de numero de tamaños"

def testT8 ():
    assert addSizes([1, 2, "a"]) == "Uno de los valores para el tamaño no es un entero"

def testT9 ():
    assert addSizes([]) == "Debe de intruducir minimo un tamaño"

def testT10 ():
    assert addSizes([1,19.5,34]) == "Uno de los valores para el tamaño no es un entero"

#Tests para linea completa
def testA1 ():
    assert add("Red Cola, 1, 2, 3") == "Se agrego bebida\nSe agregaron los tamaños"

def testA2 ():
    assert add("R, 1, 2, 3") == "No se puede agregar la bebida"

def testA3 ():
    assert add("abcdefghijklmnop, 1, 2, 3") == "No se puede agregar la bebida"

def testA4 ():
    assert add("R, 1, a, 3") == "No se puede agregar la bebida"

def testA5 ():
    assert add("Red Cola, 1, 2, 0, 4, 5") == "Se agrego bebida\nSe ingreso un tamaño no valido"

def testA6 ():
    assert add("Red Cola, 1, 2, 49, 4, 5") == "Se agrego bebida\nSe ingreso un tamaño no valido"

def testA7 ():
    assert add("Red Cola, 1, 48") == "Se agrego bebida\nSe agregaron los tamaños"

def testA8 ():
    assert add("Red Cola, 1, 2, 4, 3") == "Se agrego bebida\nLos tamaños no estan de forma ascendente"

def testA9 ():
    assert add("Red Cola, 1, 2, 3, 4, 5, 6") == "Se agrego bebida\nSe exedio de numero de tamaños"

def testA10 ():
    assert add("Red Cola, 1, 2, a, 3") == "Se agrego bebida\nUno de los valores para el tamaño no es un entero"

def testA11 ():
    assert add("Red Cola") == "Se agrego bebida\nDebe de intruducir minimo un tamaño"

def testA12 ():
    assert add(", 1, 2, 3") == "No se puede agregar la bebida"

def testA13 ():
    assert add("Red Cola, 1 2, 3") == "Se agrego bebida\nUno de los valores para el tamaño no es un entero"

def testA14 ():
    assert add("Red3Cola, 1, 2, 3") == "No se puede agregar la bebida"

def testA15 ():
    assert add("Red 3 Cola, 1, 2, 3") == "No se puede agregar la bebida"

def testA16 ():
    assert add("1, 2, 3, Red Cola") == "No se puede agregar la bebida"

def testA17 ():
    assert add("Red Cola,1,2,3") == "Se agrego bebida\nSe agregaron los tamaños"