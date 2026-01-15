class GestorEstados:
    def completar_tarea(self, gestor):
        # Esta función sirve para marcar una tarea como completada
        # Recibe el gestor de tareas para poder modificar la lista

        gestor.listar_tareas()

        # Si no hay tareas, no hacemos nada
        if not gestor.tareas: