def mostrar_menu():
    """Muestra el menú principal."""
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')


def ingresar_valoracion():
    """Permite al usuario ingresar una puntuación y un comentario."""
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'Puntuación: {point} Comentario: {comment}'
                
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                
                print("Puntuación y comentario guardados correctamente.")
                break
            else:
                print('Indíquelo en una escala de 1 a 5')
        else:
            print('Por favor, introduzca la puntuación en números')


def mostrar_resultados():
    """Muestra los resultados guardados hasta el momento."""
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print("Resultados hasta la fecha:\n", contenido)
            else:
                print("No hay resultados disponibles aún.")
    except FileNotFoundError:
        print("No hay resultados disponibles aún.")


def procesar_opcion():
    """Procesa la opción elegida por el usuario en el menú."""
    while True:
        mostrar_menu()
        opcion = input()
        
        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                ingresar_valoracion()
            elif opcion == 2:
                mostrar_resultados()
            elif opcion == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')