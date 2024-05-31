from collections import defaultdict, deque
import numpy as np 

# Dependencias para cada tarea
# Primero esta la tarea, luego una lista con las dependencias
tasks = [
    (1, []),
    (2, []),
    (3, []),
    (4, []),
    (5, []),
    (6, [1, 2, 3, 4, 5]),
    (7, []),
    (8, []),
    (9, [6, 7, 8]),
    (10, []),
    (11, []),
    (12, []),
    (13, []),
    (14, [10, 11, 12, 13]),
    (15, []),
    (16, []),
    (17, []),
    (18, []),
    (19, [15, 16, 17, 18]),
    (20, []),
    (21, []),
    (22, [20, 21]),
    (23, [9, 14, 19]),
    (24, [22, 23]),
    (25, [24]),
    (26, [25]),
    ]

# Pedir valores para luego imprimir:
Numero_tareas=int(input("Digite el numero de tareas: "))

# Revisar que si coincidan (Esta parte es para evitar errores)
if len(tasks)!=Numero_tareas:
    print("Error: Revisar que el numero de tareas digitado coincida con el numero de tareas en la lista")

Numero_max_estaciones=int(input("Digite el numero de maximo de estaciones: "))


# Tiempos estándar de ejecución de cada tarea
task_times = [
    9.7, 9.6, 7.7, 8.3, 8.3, 11.5, 9.6, 10, 9.4, 8.3, 7.6, 9.9, 6.8, 7.4, 7.9, 7.6, 9, 
    4.5, 6.4, 10.5, 5.3, 4.9, 7.3, 6.7, 8.7, 8.9]

#############################################

adjacency_list = defaultdict(list)
for task, dependencies in tasks:
    for dep in dependencies:
        adjacency_list[dep].append(task)

def find_all_dependencies(task, adjacency_list):
    result = []
    stack = [task]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for neighbor in adjacency_list[current]:
                result.append((task, neighbor))
                stack.append(neighbor)
    return result

all_dependencies = []
for task, dependencies in tasks:
    for dep in dependencies:
        all_dependencies.append((task, dep))
    all_dependencies.extend(find_all_dependencies(task, adjacency_list))

dict_dependencias={}
lista_set_A=[]
lista_set_B=[]

# Setear los valores iniciales para el diccionario: 
for dependency in sorted(all_dependencies):
    dict_dependencias[dependency[0]]=0

for dependency in sorted(all_dependencies):
    task_time = task_times[dependency[1] - 1]
    if dependency[0] < dependency[1]:
        agregar = str(dependency[0]) + " " + str(dependency[1])
    if dependency[1] > dependency[0]:
        agregar_2 = str(dependency[1]) + " " + str(dependency[0])
    if agregar not in lista_set_A:
        lista_set_A.append(agregar)
        lista_set_B.append(agregar_2)
        dict_dependencias[dependency[0]]=task_time+dict_dependencias[dependency[0]]
    else:
        continue

# Setear valores para este dic b
dict_b={}
for i in range(len(tasks)):
    dict_b[i+1]=0
for elemnto, dependencia in tasks:
    for dep in dependencia:
        lista_sumar=[]
        lista_sumar.append(float(task_times[dep-1])) #No es necesario, pero ya lo hice, ni modo
        try:
            suma=np.sum(lista_sumar)+dict_b[dep]
        except:
            pass
        dict_b[elemnto]=suma+dict_b[elemnto]

# Imprimir
print("Copiar todo lo de abajo")
print()
print(f'%elements set <1..{Numero_tareas}>')
print(f'%stations set <1..{Numero_max_estaciones}>')
print("%A set [2] <")
for i in range(len(lista_set_A)):
    print(lista_set_A[i])
print(">")
print("%B set[2] < ")
for i in range(len(lista_set_A)):
    print(lista_set_B[i])
print(">")
print(f'%a[elements] <')
for i in range(len(tasks)):
    print(round(dict_dependencias[i+1],1))
print(">")
print(f'%b[elements] <')
for i in range(len(tasks)):
    print(round(dict_b[i+1],1))
print(">")
print(f'%t [elements] <')
for i in range(len(task_times)):
    print(task_times[i])
print(">")