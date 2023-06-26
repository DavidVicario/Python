#Ejercicio 1
def fuerza (masa, aceleracion):
    return masa*aceleracion

#Ejercicio 2
def circulo (radio):
    '''import math
    math.pi'''
    from math import pi    
    print('El area del circulo es ' + str(pi*radio**2))

def cuadrado(lado):
    return lado**2

def triangulo (base, altura):
    return base*altura/2

#Ejercicio 3
def b_m (barn):
    return barn*10**(-20)

def m_b (m2):
    return m2*10**20

#Ejercicio 4
def media(nota1,nota2,nota3):
    print('La nota media es %.2f' % ((a+b+c)/3))

#Ejercicio 5
def tiea(TNA,m):
    return ((1+TNA/m)**m)-1
    
print('Ejercicio 1')

a=float(input('Introduzca el valor de la masa: '))
b=float(input('Introduzca el valor de la aceleracion: '))
print('La fuerza es: ',fuerza(a,b))

print('Ejercicio 2')

a=float(input('Intruduzca el valor del radia: '))
circulo(a)
a=float(input('Intruduzca el valor del lado: '))
print('El area del cuadrado es %.2f' % cuadrado(a))
a=float(input('Intruduzca el valor de la base: '))
a=float(input('Intruduzca el valor de la altura: '))
print('Elarea del triangulo es:', triangulo(a,b))

print('Ejercicio 3')

a=float(input('Intruduzca los barn: '))
print('El valor de m2 es ' + str (b_m(a)))
a=float(input('Intruduzca los m2: '))
print('El valor de barn es', m_b(a))

print('Ejercicio 4')

a=float(input('Intruduzca la nota del primer alumno: '))
b=float(input('Intruduzca la nota del segundo alumno: '))
c=float(input('Intruduzca la nota del tercero alumno: '))
print('La media de la nota es', media(a,b,c))

print('Ejercicio 5')

a=float(input('Intruduzca TNA: '))
b=float(input('Intruduzca m: '))
print('El valor del TIEA es',tiea(a,b))










