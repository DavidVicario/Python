import math #matemáticas
from ejemplo_modulo import mod_horas, mod_minutos, mod_segundos, circun


#Ejercicio_1
print('Ejercicio nº 1')
##Fuerza=masa*aceleración
def fuerza(masa,aceleracion):
    return masa*aceleracion
a=float(input("Introduce la masa:\n\t"))
b=float(input("Introduce la aceleración:\n\t"))
#definiendo una función
print('La fuerza es: \n\t%.2f' %fuerza(a,b))

#utilizando una función anónima
c=lambda e,f:e*f
print('La fuerza es: \n\t%.2f' %c(a,b))


#Ejercicio_2
print('\nEjercicio nº 2')
def circulo(radio):
    return math.pi*radio**2
def cuadrado(lado):
    return lado**2
a=float(input("Introduce el radio del círculo:\n\t"))
print('El área del círculo es: \n\t%.5f\n\n' %circulo(a))
a=float(input("Introduce el lado del cuadrado:\n\t"))
print('El área del cuadrado es: \n\t%.2f\n\n' %cuadrado(a))

c=lambda e,f:e*f/2
a=float(input("Introduce la base del triángulo:\n\t"))
b=float(input("Introduce la altura del triángulo:\n\t"))
print('El área del triángulo es: \n\t%.2f\n\n' %c(a,b))


#Ejercicio_3
print('\nEjercicio nº 3')
def barn(C):
    return C/(10**(-28))
def metro(C):
    return C*(10**(-28))
a=int(input("¿Qué opción quiere realizar:\n\t1.- Tranformar Barns en m2\
\n\t2.- Transformar m2 en Barns\n"))
while a<1 or a>2:
    a=int(input("¿Qué opción quiere realizar:\n\t1.- Tranformar Barns en m2\
\n\t2.- Transformar m2 en Barns\n"))
if a==1:
    b=float(input("Introduzca la cantidad de Barns:\n\t"))
    print("%.30f m2" %metro(b))
else:
    b=float(input("Introduzca la cantidad de Barns:\n\t"))
    print("%.2f Barns" %barn(b))


#Ejercicio_4
print('\nEjercicio nº 4')
t_sum=0
# for i in range (1,3)    -> 1,2
# for i in range (1,7,2)  -> 1,3,5
# for i in range (3)      -> 0, 1, 2
# for i in range (7,1,-1) -> 7,6,5,4,3,2
for i in range(3):
    nota=int(input("Introduzca la nota del alumno %i:\n\t" %(i+1)))
    t_sum+=nota
print('La media es: %.2f' %(t_sum/(i+1)))


#Ejercicio_5
print('\nEjercicio nº 5')
def interes(tipo,per):
    return 100*(((1+tipo/per)**per)-1)
opcion=[1,2,3,4,6,12]
TNA=float(input("Introduzca la Tasa de Interés Nominal (TNA):\n\t"))
a=int(input("Elija el tipo de Capitalización:\n\t1.- Anual (1)\
\n\t2.- Semestral (2)\n\t3.- Cuatrimestral (3)\n\t4.- Trimestral (4)\n\t\
5.- Bimestral (6)\n\t6.- Mensual (12)\n"))
print ('La Tasa de Interés Efectiva Anual es:\n\t%.4f' \
%(interes(TNA,opcion[a-1])),'%')


#Ejercicio_6
print('\nEjercicio nº 6')
def grad(rad):
    return (360*rad)/(2*math.pi)
a=float(input("Introduzca radianes:\n\t"))
print("Los grados son:\n\t%.2f" %grad(a))


#Ejercicio_7
print('\nEjercicio nº 7')
num_seg=0
a=float(input("Introduce la hora:\n\t"))
num_seg+=mod_horas(a)
print(num_seg)
a=float(input("Introduce los minutos:\n\t"))
num_seg+=mod_minutos(a)
print(num_seg)
a=float(input("Introduce los segundos:\n\t"))
num_seg+=mod_segundos(a)
print(num_seg)


#Ejercicio_8
print('\nEjercicio nº 8')
def hecto(km):
    return 10*km
def deca(km):
    return 100*km
def met(km):
    return 1000*km
a=float(input("Introduczca los km:\n\t"))
print("Los Hm son:",hecto(a))
print("Los Hm son:",deca(a))
print("Los Hm son:",met(a))

#Ejercicio_9
print('\nEjercicio nº 9')
a=float(input("Introduczca la x:\n\t"))
b=float(input("Introduczca la y:\n\t"))
circun(a,b)

#Ejercicio_10
print('\nEjercicio nº 10')
def pint(ml):
    return ml/473.176473
a=float(input("Introduczca la cantidad de mililitros:\n\t"))
print("La cantidad de pintas son: %.2f" %pint(a))

#Ejercicio_11
print('\nEjercicio nº 11')
for i in range(1,10):
    print("1 *",i,"=",1*i)

#Ejercicio_12
print('\nEjercicio nº 12')
def kelvin(cent):
    return cent+273.15
273.15
def fahrenheit(cent):
    return 9*cent/5+32
a=float(input("Introduczca la Temperatura en grados centígrados:\n\t"))
print("La Temperatura en Kelvin es: ", kelvin(a))
print("La Temperatura en Kelvin es: ", fahrenheit(a))

#Ejercicio_13
print('\nEjercicio nº 13')
def distancia(p1,p2):
    t_sum=0
    for i in range(3):
        t_sum+=(p1[i]-p2[i])**2
    return pow(t_sum,0.5)
    
x1=[]
for i in range(3):
    a=int(input("Introduce el punto: "))
    x1.append(a)
print (x1)
x2=[]
for i in range(3):
    a=int(input("Introduce el punto: "))
    x2.append(a)
print (x2)
print("La distancia entre los puntos es: %.2f" %
      distancia(x1,x2))

#Ejercicio_14
print('\nEjercicio nº 14')
complejos=[]
for i in range(2):
    a=complex(input("Introduzca un número complejo (la parte compleja con j): \n\t"))
    complejos.append(a)
print(complejos[0].real,complejos[0].imag)
print(complejos[0]+complejos[1])
print(complejos[0]-complejos[1])
print(complejos[0]*complejos[1])
print(complejos[0]/complejos[1])


#Ejercicio_15
print('\nEjercicio nº 15')
a=int(input("Introduce un año: "))
if (a%400==0 or (a%4==0 and a%100!=0)):
    print("Bisiesto")
else:
    print("NO Bisiesto")
