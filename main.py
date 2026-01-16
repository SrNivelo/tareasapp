from tareas import GestorTareas
from estado import GestorEstados
from menu import Menu

def main():
    # Creamos los objetos principales del programa
    gestor = GestorTareas()
    estado = GestorEstados()
    menu = Menu()

    # Bucle principal del programa (se repite hasta que el usuario salga)
    while True:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Pedimos la descripción y la mandamos al gestor de tareas
            desc = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(desc)

        elif opcion == "2":
            # Mostramos todas las tareas
            gestor.listar_tareas()

        elif opcion == "3":
            # Llamamos al gestor de estados para completar una tarea
            estado.completar_tarea(gestor)

        elif opcion == "4":
            # Salimos del programa
            print("Saliendo del programa...")
            break

        else:
            # Por si el usuario escribe cualquier cosa
            print("Opción inválida, intente de nuevo.")

# Esto hace que el programa empiece desde aquí
if __name__ == "__main__":
    main()