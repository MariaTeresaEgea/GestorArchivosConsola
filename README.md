# Gestor de Archivos en Consola

Una aplicación de consola en Python para gestionar archivos y carpetas de forma sencilla. Permite listar, crear, eliminar, renombrar archivos y carpetas, escribir contenido, navegar entre directorios y más.

---

## Funcionalidades

- Listar contenido del directorio actual (archivos y carpetas)
- Crear un nuevo directorio
- Crear un archivo de texto
- Crear un archivo dentro de una carpeta
- Escribir texto en un archivo existente
- Eliminar archivos o carpetas (solo vacías)
- Renombrar archivos o carpetas
- Mostrar información del archivo o carpeta (tamaño, tipo, fecha de modificación)
- Navegar hacia el directorio padre
- Entrar en una carpeta
- Mostrar tamaño total del directorio actual
- Historial de comandos ejecutados en la sesión
- Demo de colores usando Colorama

---

## Requisitos

- Python 3.7 o superior
- Librería Colorama (`pip install colorama`)

---

## Cómo ejecutar

1. Clonar el repositorio:

Entrar en la carpeta del proyecto:

Copiar código
cd nombre-del-proyecto

Instalar Colorama (si no está instalada):

Copiar código
pip install colorama

Ejecutar el programa:

Copiar código
python gestor_archivos.py

Seguir las instrucciones del menú en consola.

Estructura del proyecto
Copiar código
gestor_archivos/
├─ gestor_archivos.py
├─ README.md
└─ ... (otras carpetas o archivos si los hay)

Notas
La aplicación maneja errores comunes (archivos inexistentes, nombres repetidos, permisos).
La navegación dentro de carpetas afecta al directorio actual mostrado en el menú.
El historial permite revisar todas las acciones realizadas durante la sesión.
La demo de colores permite verificar que los mensajes se muestran correctamente en la terminal.

Recomendaciones
Ejecuta el programa en la terminal de VS Code para ver correctamente los colores.
Antes de crear un archivo en una carpeta, asegúrate de que la carpeta exista.
Usa el historial de comandos para comprobar todas las acciones realizadas durante la sesión.
