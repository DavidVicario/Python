
#Ejercicio 1
'''Escribe un codigo que implemente el siguiente comportamiento:
"Si la compra es superior a 100€ se aplica un descuento del 5% si se paga al
contado, pero si el pago es con targeta solo se aplica el 2%". Asegurate de que
el importe de la compra es un número válido antes de proceder a los cálculos.
(Pista: Usa try para comprobar que es posible convertir la entrada a float.'''

def calculoDescuento(opc):
    if opc == '1':
        return 0.05
    else:
        return 0.02

def ejercicio1():
    compra = input("Introduzca el valor de la compra: ") #Siempre es string
    try:
        compra = float(compra)
        print("OPCIONES: ")
        print("1.- Contado")
        print("2.*- Tarjeta")
        opcion = input("Seleccione opción: ")

        print("Se aplica descuento de %.2f" % calculoDescuento(opcion))
        print("Hay que pagar: ", compra * (1 - calculoDescuento(opcion)))
    except:
        print("No ha introducido un valor númerico")

ejercicio1()
    
#Ejercicio 2
'''Una universidad acaba de modificar su sistema de representación de la
calificación de los alumnos, que como es sabido son valores entre 0 y 10. A
partir de ahora, se calificarán como “A” las notas mayores o iguales a 8,5,“B”
las mayores o iguales a 6,5, “C” las calificaciones mayores o iguales a 5, “D”
las calificaciones mayores o iguales a 3,5, y “F” todas las demás. Programa una función que
reciba una calificación numérica y retorne la letra con la nueva calificación.
Asegúrate de que la calificación introducida es válida (idea: programa una
función lo suficientemente genérica que se pueda luego reutilizar en programas
que necesiten una validación similar).'''



def ejercicio2():
    nota = input("Introduzca la nota del alumno: ")
    try:
        nota = float(nota)
        if nota < 3.5:
            print("La calificacion es : ", "F")
        elif nota < 5:
            print("La calificacion es : ", "D")
        elif nota < 6.5:
            print("La calificacion es : ", "E")
        elif nota < 8.5:
            print("La calificacion es : ", "B")
        else:
            print("La calificacion es : ", "A")
        
    except:
        print("No ha introducido un valor númerico")

ejercicio2()

#Ejercicio 3
'''Escribe un algoritmo que tras leer tres enteros los escriba en pantalla en
orden creciente. Como siempre, valida las entradas. '''

def ejercicio3():
    lista = [3,5,2]
    lista.sort()  #Ordena listas ascendente
    print(lista)

ejercicio3()

#Ejercicio 4
'''Codifica un subprograma que reciba un número entero, y si es entre 1 y 12
escriba un mensaje por pantalla indicando el mes a que dicho número corresponde. En caso contrario deberá
mostrar un mensaje de error.'''

def ejercicio4():
    lista = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
             'Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    mes = int(input("Introduzca el mes: "))
    
    while (mes < 1 or mes > 12):
        mes = int(input("Introduzca el mes (Entre 1 y 12): "))
        print(lista[mes-1])

ejercicio4()

#Ejercicio 5
'''Escribe un programa que, después de preguntar cuántos números se van a
introducir, pida esos números (enteros o reales) y devuelva su media aritmética,
el mayor y el menor. El programa debe controlar que la cantidad de números es
mayor de 2 y en caso contrario ha de mostrar un mensaje de error.'''

def ejercicio5():
    lista = []
    numeros=int(input("Introduzca cuántos números va a introducir: "))
    
    if numeros > 2:
        for i in range(numeros):
            lista.append(float(input('Introduzca el %iº número: ' % ( i + 1))))
            
        print (lista)
    else:
        print("ERROR")

ejercicio5()

#Ejercicio 6
'''Escribir una función que sume dos listas de igual longitud y retorne otra
lista que contenga la suma de las originales elemento a elemento.'''

def ejercicio6():
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista3 = []
    
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
        
    print(lista3)

ejercicio6()

#Ejercicio 7
'''Modifique el ejercicio anterior permitiendo que las listas sean desiguales.
Los elementos sobrantes de la lista más larga se añadirán al final de la lista
resultante.'''

def ejercicio7():
    lista1 = [1,2,3,8,9]  #len(lista1)=5
    lista2 = [4,5,6,7,8,10]    #len(lista2)=4
    lista3 = []
    
    for i in range(min(len(lista1), len(lista2))):
        lista3.append(lista1[i] + lista2[i]) #0,1,2,3
        
    if len(lista1) > len(lista2):
        for i in range(len(lista2), len(lista1)):
            lista3.append(lista1[i])       #4
            
    if len(lista2) > len(lista1):
        for i in range(len(lista1), len(lista2)):
            lista3.append(lista2[i])
            
    print(lista3)
    
ejercicio7()

#Ejercicio 8
'''Distribuir los 20 datos enteros en dos listas de tal manera que se vayan
generando dos secuencias ordenadas, una creciente y otra decreciente.'''

def ejercicio8():
    lista = []
    listaAsc = []
    listaDes = []
    
    for i in range(4):
        lista.append(int(input("Introduzca número: ")))
        
    print(lista)
    
    listaAsc = lista
    listaAsc.sort()  #ordenar ascendente
    print(listaAsc)
    
    listaDes = lista
    listaDes.sort(reverse=True)  #ordenar descendente
    print(listaDes)

ejercicio8()

#Ejercicio 9
'''Crear una lista de enteros, inicializarlos según valores aleatorios en el
rango 1-20 y computar la media de los valores, el valor más alto y el más bajo
(todo ello utilizando listas).''' 

import random

def media(med):
    return sum(med)/len(med)
    
def ejercicio9():
    lista = []
    for i in range (20):
        lista.append(random.randint(1, 20))

    print(lista)

    print("La media es: ", media(lista))
    print("El mas alto es: ", max(lista))
    print("El mas bajo es: ", min(lista))

'''def ejercicio9():
    lista = []
    for i in range (10)
    num = ramdom.randint(1,20)
    lista.append(num)
media = sum(lista)/len(lista)
maximo = max(lista)
minimo = min (lista)'''
    
ejercicio9()

#ejercicio10
'''Introducir una palabra (sarabaras) y ver si es palindroma'''

def palindromo(cadena):
    cInicio = 0
    cFinal = len(cadena) - 1
    while cadena[cInicio] == cadena[cFinal]:
        if cInicio >= cFinal:
            return True
        cInicio += 1
        cFinal -= 1
    return False
    
def ejercicio10():
    cadena = input("Introduzca una palabra: ")

    resul = palindromo(cadena)

    if resul:
        print("Esta palabra es palindroma")
    else:
        print("Esta palabra NO es palindroma")

ejercicio10()

#ejercicio11
'''Introducir una frase por teclado en minúscula y que salga la
primera letra de cada palabra en mayúscula'''

def ejercicio11():
    cadena = input("Introduzca una frase: ")

    #mayus = cadena.upper()
    #minus = cadena.lower()
    #cambio = cadena.swapcase()
    firt = cadena.title()

    #print("En mayúsculas: ", mayus)
    #print("En minúsculas: ", minus)
    #print("Cambia mayúsculas por minúsculas y viceversa: ", cambio)
    print("La primera letra en mayúsculas: ", firt)
    
ejercicio11()
