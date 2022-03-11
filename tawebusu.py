import json
import requests
from pprint import pprint

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos")
pendientes = json.loads(response.text)



#imprime el json cargado

#pprint(pendientes)


pendientes_por_usuario = {}

#lleva un conteo de los pendientes
#que ha completado cada usuario
pendientes_por_usuario= {}
# Lleva un conteo de los pendientes
# que ha completado cada usuario
for pendiente in pendientes:
    if pendiente["completed"]:
        if pendiente["userId"] in pendientes_por_usuario:
            pendientes_por_usuario[pendiente["userId"]] += 1
        else:
            pendientes_por_usuario[pendiente["userId"]] = 1

# prdena por id  los usuarios
items_ordenados = sorted(pendientes_por_usuario.items(), key = lambda x: x[1], reverse = True)
maximas_tareas_completadas = items_ordenados[0][1]


usuarios = []
for usuario, num_tareas_completas in items_ordenados:
    if num_tareas_completas == maximas_tareas_completadas:
        usuarios.append(str(usuario))
    else:
        break

usuarios_con_max = " y ".join(usuarios)
print("los usuarios", usuarios_con_max)
print("han completado", maximas_tareas_completadas, "tareas")


def filtro(pendiente):
    esta_completa = pendiente["completed"]
    esta_en_el_maximo_conteo = str(pendiente["userId"]) in usuarios
    return esta_completa and esta_en_el_maximo_conteo

with open("json/tareas_filtradas.json", "w") as archivo_salida:
    tareas_filtradas = list(filter(filtro, pendientes))
    json.dump(tareas_filtradas, archivo_salida, indent=2)
