def agregar_tarea(*tareas):
    Atareas = open('tareas.txt','a')
    for i in tareas:
        Atareas.write(i + "\n")

def listar_tareas():
    indice = 1
    with open('tareas.txt','r') as Atareas:
        print("---------------------TAREAS PENDIENTES--------------------")
        for i in Atareas:
            print(f" {indice}.{i.strip()} ")

            indice+=1
        print("----------------------------------------------------------")
    #se reinicia el contador
    indice = 1
    with open('tareas_completadas.txt','r') as Btareas:
        print("--------------------TAREAS COMPLETADAS--------------------")
        for e in Btareas:
            print(f" {indice}.{e.strip()} ")

            indice+=1
        print("----------------------------------------------------------")


def marcar_completada():
    Atareas = open('tareas.txt','r+')

    lineas = Atareas.readlines()
    tarea = int(input("Inserte el indice/numero de la tarea que completó: "))
    Btareas = open('tareas_completadas.txt', 'a')
    Btareas.write( lineas[tarea-1] )  
    del( lineas[tarea-1])
    Atareas.seek(0)
    Atareas.writelines(lineas)


numero_tareas= int(input("Numero de tareas a agregar: "))

for i in range(numero_tareas):
    agregar_tarea(input("Escribe el titulo y descripcion de la tarea: "))

listar_tareas()
marcar_completada()