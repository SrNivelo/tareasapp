class GestorEstados:
    def completar_tarea(self, gestor):
        # Esta función sirve para marcar una tarea como completada
        # Recibe el gestor de tareas para poder modificar la lista

        gestor.listar_tareas()

        # Si no hay tareas, no hacemos nada
        if not gestor.tareas:
            return

        try:
            # Pedimos al usuario el número de la tarea que quiere completar
            num = int(input("Ingrese el número de la tarea a completar: "))

            # Verificamos que el número esté dentro del rango correcto
            if 1 <= num <= len(gestor.tareas):
                # Marcamos la tarea como completada
                gestor.tareas[num - 1]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            # Esto pasa si el usuario escribe letras en vez de números
            print("Debe ingresar un número válido.")