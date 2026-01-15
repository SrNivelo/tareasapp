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
