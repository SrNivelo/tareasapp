class GestorTareas:
    def __init__(self):
        # Aquí se va a guardar la lista de tareas
        # Cada tarea será un diccionario con descripción y estado
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Esta función sirve para agregar una nueva tarea a la lista
        # Siempre se agrega como "no completada"
        self.tareas.append({
            "descripcion": descripcion,
            "completada": False
        })
        print("Tarea agregada correctamente.")

    def listar_tareas(self):
        # Esta función muestra todas las tareas que existen

        if not self.tareas:
            # Si no hay tareas en la lista, avisa al usuario
            print("No hay tareas registradas.")
            return

        print("\nLISTA DE TAREAS:")
        # Recorremos la lista de tareas y las mostramos una por una
        for i, tarea in enumerate(self.tareas):
            # Si la tarea está completada mostramos un símbolo distinto
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i+1}. {tarea['descripcion']} [{estado}]")