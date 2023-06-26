import math


def calcular_distancia(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(3)]))


def opcion1():
    print("Has elegido la opción 1")
    alumnos = {}

    # Pedir el nombre y la nota de cada alumno
    for i in range(3):
        nombre = input(f"Introduce el nombre del alumno {i + 1}: ")
        nota = float(input(f"Introduce la nota del alumno {i + 1}: "))

        # Validar que la nota esté entre 0 y 10
        while nota < 0 or nota > 10:
            print("Error: la nota debe estar entre 0 y 10")
            nota = float(input(f"Introduce la nota del alumno {i + 1}: "))

        # Agregar el alumno y su nota al diccionario
        alumnos[nombre] = nota

    # Buscar la nota máxima entre los alumnos
    nota_maxima = max(alumnos.values())
    
    # Calcular la media de las notas
    suma_notas = sum(alumnos.values())
    media_notas = suma_notas / len(alumnos)
    
    # Imprimir los alumnos que tienen la nota máxima
    print("Alumnos con la nota máxima: ")
    for nombre, nota in alumnos.items():
        if nota == nota_maxima:
            print(nombre)

    # Imprimir la media de las notas
    print(f"La media de las notas es: {media_notas:.2f}")

def opcion2():
    print("Has elegido la opción 2")
    numeros_complejos = []

    for i in range(3):
        num = complex(input("Ingrese el número complejo {} en formato a+bj: ".format(i + 1)))
        numeros_complejos.append(num)

    for numero in numeros_complejos:
        print("Parte real:", numero.real)
        print("Parte imaginaria:", numero.imag)


def opcion3():
    # Pedimos las coordenadas del primer punto
    x1, y1, z1 = map(float,
                     input("Introduce las coordenadas del primer punto en formato (x,y,z) Ej(1,2,3): ").strip('()').split(','))
    # Pedimos las coordenadas del segundo punto
    x2, y2, z2 = map(float,
                     input("Introduce las coordenadas del segundo punto en formato [x,y,z] Ej[8,2,4]: ").strip('[]').split(','))
    # Creamos las tuplas y listas correspondientes
    p1 = (x1, y1, z1)
    p2 = [x2, y2, z2]
    # Calculamos la distancia y la mostramos por pantalla
    distancia = calcular_distancia(p1, p2)
    print("La distancia entre los puntos es:", distancia)


opciones = [(1, "Opción 1"), (2, "Opción 2"), (3, "Opción 3"), (0, "Salir")]

while True:
    print("=== MENÚ ===")
    for opcion in opciones:
        print("{}. {}".format(opcion[0], opcion[1]))

    seleccion = int(input("Elige una opción: "))

    if seleccion == 1:
        opcion1()
    elif seleccion == 2:
        opcion2()
    elif seleccion == 3:
        opcion3()

    elif seleccion == 0:
        break
    else:
        print("INTRODUCE UN NUMERO ENTRE 0 Y 1.")
