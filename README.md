Gestor de Tareas en Consola – Python
## Descripción del proyecto

Este proyecto es un programa en Python que se ejecuta en consola y permite al usuario gestionar una lista de tareas de manera sencilla. El usuario puede agregar nuevas tareas, ver la lista de tareas existentes y marcar tareas como completadas mediante un menú interactivo.

El objetivo del proyecto, además de la funcionalidad del programa, es aplicar correctamente el trabajo colaborativo utilizando Git y el uso de ramas para el control de versiones.

## Funcionalidad del programa

El programa ofrece las siguientes opciones:

Agregar tarea:
Permite al usuario escribir una descripción y guardar una nueva tarea en el sistema. Las tareas se guardan inicialmente como no completadas.

Listar tareas:
Muestra en pantalla todas las tareas registradas, indicando cuáles están pendientes y cuáles ya han sido completadas.

Completar tarea:
Permite al usuario seleccionar una tarea de la lista y marcarla como completada.

Salir:
Finaliza la ejecución del programa.

Todo el funcionamiento se controla desde un menú principal que se repite hasta que el usuario decide salir.

## Forma de ejecución

Para ejecutar el programa se debe usar el siguiente comando en la consola:

python main.py

# Estructura del proyecto

El proyecto está organizado en varios archivos:

main.py: Contiene el flujo principal del programa.

tareas.py: Contiene la clase encargada de gestionar las tareas (agregar y listar).

estados.py: Contiene la clase encargada de marcar tareas como completadas.

menu.py: Contiene la clase que muestra el menú en pantalla.

## Flujo de trabajo con ramas (Git)

Para el desarrollo del proyecto se utilizó un flujo de trabajo basado en ramas, donde cada integrante del grupo trabajó de forma independiente en una parte del sistema.

Se crearon las siguientes ramas:

rama-nivelo-tareas:
En esta rama se desarrolló la clase encargada de la gestión de tareas (tareas.py), incluyendo la creación y el listado de tareas.

rama-parra-estado:
En esta rama se desarrolló la clase encargada de cambiar el estado de las tareas (estados.py), permitiendo marcarlas como completadas.

rama-pinto-menu:
En esta rama se desarrolló la clase encargada de mostrar el menú del programa (menu.py).

Cada integrante:

- Clonó el repositorio principal.

- Creó su propia rama.

- Implementó su parte del sistema en un archivo independiente.

- Realizó commits con los cambios realizados en su rama.

- Subió su rama al repositorio remoto.

Posteriormente, el líder del proyecto:

- Revisó cada rama.

- Integró (merge) los cambios de cada rama en la rama principal main.

- Unificó todo el funcionamiento en el archivo main.py.

De esta manera, el proyecto final quedó completamente integrado en la rama principal, manteniendo un historial claro del trabajo realizado por cada integrante.

## Trabajo en equipo

Cada integrante del grupo fue responsable de una parte específica del sistema, lo que permitió:

- Evitar conflictos en el código.

- Mantener el proyecto organizado.

- Aplicar correctamente el uso de Git y ramas.

- Tener un historial de cambios claro y ordenado.