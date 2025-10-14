
import os
import time
from colorama import Fore, Style, init
init (autoreset=True)


def mostrar_menu(): # creamos el menú principal
    print("\n" + "="*60)
    print(Fore.CYAN + "GESTOR DE ARCHIVOS EN CONSOLA".center(60))
    print("="*60)
    print(f"Directorio actual: {Fore.YELLOW}{os.getcwd()}")
    print("="*60)
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo")
    print("7. Entrar en carpeta")
    print("8. Cambiar al directorio padre")
    print("9. Renombrar archivo o carpeta")
    print("10. Mostrar tamaño total del directorio actual")
    print("11. Mostrar historial de comandos")
    print("12. Salir")
    print("="*60)

def listar_contenido(): # Función para listar el contenido del directorio
    print("\nContenido del directorio actual:\n")
    try:
        for elem in os.listdir():
            if os.path.isdir(elem):
                print(Fore.BLUE + f"[CARPETA] {elem}")
            else:
                print(Fore.GREEN + f"[ARCHIVO] {elem}")
        historial.append("Se listó el contenido del directorio actual")
    except Exception as e:
        print(Fore.RED + f"❌ Error al listar contenido: {e}")

def ir_directorio_padre(): # navegar hacia atrás
    try:
        os.chdir("..")
        print(Fore.CYAN + f"📂 Has vuelto a: {os.getcwd()}")

    except Exception as e:
        print(Fore.RED + f"❌ No se pudo cambiar de directorio: {e}")
        historial.append("Se cambió al directorio padre")
def crear_directorio(): # Verificar si ya existe antes de crearlo
    nombre = input("Introduce el nombre del nuevo directorio: ")
    if os.path.exists(nombre):
        print("❌ Ya existe un archivo o carpeta con ese nombre.")
    else:
        try:
            os.mkdir(nombre)
            print("✅ Directorio creado correctamente.")
            historial.append(f"Se creó el directorio '{nombre}'")
        except Exception as e:
            print(f"⚠️ Error al crear el directorio: {e}")

def crear_archivo(): # permite introducir  nombre y contenido inicial
    nombre = input("Introduce el nombre del nuevo archivo (con .txt): ")
    if os.path.exists(nombre):
        print("❌ Ya existe un archivo con ese nombre.")
        return
    try:
        contenido = input("Escribe el contenido inicial: ")
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(contenido)
        print("✅ Archivo creado correctamente.")
        historial.append(f"Se creó el archivo '{nombre}'")
    except Exception as e:
        print(f"⚠️ Error al crear el archivo: {e}")

def renombrar_elemento():
    nombre = input("Introduce el nombre actual del archivo o carpeta: ")
    if not os.path.exists(nombre):
        print(Fore.RED + "❌ Ese archivo o carpeta no existe.")
        return

    nuevo_nombre = input("Introduce el nuevo nombre: ")
    if os.path.exists(nuevo_nombre):
        print(Fore.RED + "❌ Ya existe un elemento con ese nombre.")
        return

    try:
        os.rename(nombre, nuevo_nombre)
        print(Fore.GREEN + f"✅ '{nombre}' se ha renombrado a '{nuevo_nombre}'.")
        historial.append(f"Se renombró '{nombre}' a '{nuevo_nombre}'")
    except Exception as e:
        print(Fore.RED + f"❌ Error al renombrar: {e}")

def escribir_en_archivo(): # Permite escribiren archivo existente
    nombre = input("Nombre del archivo donde escribir: ")
    if not os.path.exists(nombre):
        print("❌ El archivo no existe.")
        return
    try:
        texto = input("Escribe el texto a añadir: ")
        with open(nombre, "a", encoding="utf-8") as f:
            f.write("\n" + texto)
        print("✅ Texto añadido correctamente.")
        historial.append(f"Se añadió texto al archivo '{nombre}'")
    except Exception as e:
        print(f"⚠️ Error al escribir en el archivo: {e}")

def eliminar_elemento(): #usamos las diferentes funciones para  eliminar, según  seaarchivos o carpetas
    nombre = input("Nombre del archivo o carpeta a eliminar: ")
    if not os.path.exists(nombre):
        print("❌ No existe ese archivo o carpeta.")
        return
    try:
        if os.path.isdir(nombre):
            os.rmdir(nombre)  # solo elimina carpetas vacías
            print("✅ Carpeta eliminada.")
        else:
            os.remove(nombre)
            print("✅ Archivo eliminado.")
        historial.append(f"Se eliminó '{nombre}'")
    except Exception as e:
        print(f"⚠️ Error al eliminar: {e}")

def mostrar_informacion(): # mostrar el tamaño, tipo y fecha de modificación
    nombre = input("Nombre del archivo o carpeta: ")
    if not os.path.exists(nombre):
        print("❌ No existe.")
        return
    try:
        tam = os.path.getsize(nombre)
        fecha_mod = time.ctime(os.path.getmtime(nombre))
        tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"
        print("\n--- INFORMACIÓN ---")
        print("Nombre:", nombre)
        print("Tipo:", tipo)
        print("Tamaño:", tam, "bytes")
        print("Última modificación:", fecha_mod)
        historial.append(f"Se mostró información de '{nombre}'")
    except Exception as e:
        print(f"⚠️ Error al obtener información: {e}")

def mostrar_tamaño_total():
    total = 0
    try:
        for elem in os.listdir():
            if os.path.isfile(elem):
                total += os.path.getsize(elem)
        print(Fore.YELLOW + f"📦 Tamaño total del directorio actual: {total} bytes ({round(total/1024, 2)} KB)")
        historial.append("Se mostró el tamaño total del directorio")
    except Exception as e:
        print(Fore.RED + f"❌ Error al calcular el tamaño total: {e}")

def entrar_en_carpeta():
    """Permite entrar en una carpeta existente."""
    carpeta = input("Introduce el nombre de la carpeta a abrir: ")
    if not os.path.exists(carpeta) or not os.path.isdir(carpeta):
        print(Fore.RED + "❌ Esa carpeta no existe.")
        return
    try:
        os.chdir(carpeta)
        print(Fore.CYAN + f"📂 Has entrado en la carpeta: {os.getcwd()}")
        historial.append(f"Se entró en la carpeta '{carpeta}'")
    except Exception as e:
        print(Fore.RED + f"❌ No se pudo entrar en la carpeta: {e}")

historial = []


historial.append("Se listó el contenido del directorio actual")

def mostrar_historial():
    print("\n📜 HISTORIAL DE COMANDOS:")
    for i, accion in enumerate(historial, 1):
        print(f"{i}. {accion}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            crear_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == "4":
            escribir_en_archivo()
        elif opcion == "5":
            eliminar_elemento()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "7":
            entrar_en_carpeta()
        elif opcion == "8":
            ir_directorio_padre()
        elif opcion == "9":
            renombrar_elemento()
        elif opcion == "10":
            mostrar_tamaño_total()
        elif opcion == "11":
            mostrar_historial()
        elif opcion == "12":
            print(Fore.CYAN + "👋 Saliendo del programa...")
            break
        else:
            print(Fore.RED + "❌ Opción no válida. Intenta de nuevo")

if __name__ == "__main__":
    main()