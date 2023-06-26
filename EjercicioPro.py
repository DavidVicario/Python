import random

empleados = []
for i in range(1, 11):
    codigo = f"Cod-{str(i).zfill(2)}"
    nombre = f"Empleado-{str(i).zfill(2)}"
    sexo = random.choice([1, 2])
    fecha_ant = random.randint(2000, 2018)
    categoria = random.randint(1, 6)
    
    if categoria == 1:
        sueldo = 3500
    elif categoria == 2:
        sueldo = 2800
    elif categoria == 3:
        sueldo = 2200
    elif categoria == 4:
        sueldo = 1900
    elif categoria == 5:
        sueldo = 1500
    else:
        sueldo = 1200
    
    precio_hora = sueldo / (30 * 8)  # Suponiendo 30 días al mes y 8 horas al día
    
    empleados.append([codigo, nombre, sexo, fecha_ant, categoria, sueldo, precio_hora])

for empleado in empleados:
    print(empleado)



def visualizar_por_sexo_categoria(empleados, sexo, categoria):
    empleados_filtrados = [empleado for empleado in empleados if empleado[2] == sexo and empleado[4] == categoria]
    for empleado in empleados_filtrados:
        print(empleado)

def antiguedad_media(empleados, year_actual=2022):
    antiguedades = [year_actual - empleado[3] for empleado in empleados]
    antiguedad_media = sum(antiguedades) / len(antiguedades)
    return antiguedad_media


visualizar_por_sexo_categoria(empleados, 1, 3)

media = antiguedad_media(empleados)
print("Antigüedad media de los empleados:", media)
