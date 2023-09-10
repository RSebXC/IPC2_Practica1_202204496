import graphviz

def mostrar_datos_estudiante():
    print("Carnet: 202204496")
    print("Nombre completo: Rodrigo Sebastian Castro Aguilar")
    print("Curso y sección: Introduccion a la Programacion y Computacion 2  - <sección>")

def crear_tablero(n, m):
    colores = {'A': 'blue', 'R': 'red', 'V': 'green', 'P': 'purple', 'N': 'orange'}
    color_nombres = {'A': 'Azul', 'R': 'Rojo', 'V': 'Verde', 'P': 'Púrpura', 'N': 'Naranja'}
    tablero = [[' ' for _ in range(m)] for _ in range(n)]
    
    nfilas = str(n)
    ncolum = str(m)

    while True:
        print("-------Colorealo--------")
        print("Seleccione un color:")
        print("A. Azul\nR. Rojo\nV. Verde\nP. Púrpura\nN. Naranja")
        color_opcion = input("Opción: ").upper()
        print("-------Guatematel------")
        if color_opcion in colores:
            color = color_opcion
            break
        else:
            print("Opción inválida. Intente de nuevo.")
    
    while True:
        try:
            print("-------Colorealo--------")
            fila = int(input("Ingrese la fila donde colocar la pieza 1 a " + nfilas +": "))
            columna = int(input("Ingrese la columna donde colocar la pieza 1 a " + ncolum +": "))
            filaR = fila - 1
            columnaR = columna - 1
            tablero[filaR][columnaR] = color
            print("-------Guatematel------")
            print("Tablero actual:")
            for fila_tablero in tablero:
                print(' '.join(fila_tablero))
            print("-------Colorealo--------")
            continuar = input("¿Desea colocar otra pieza? (S/N): ").upper()
            if continuar == 'N':
                break  # Salir del ciclo
            elif continuar == 'S':
                print("-------Colorealo--------")
                print("Seleccione un color:")
                print("A. Azul\nR. Rojo\nV. Verde\nP. Púrpura\nN. Naranja")
                color_opcion = input("Opción: ").upper()
                print("-------Guatematel------")
                if color_opcion in colores:
                    color = color_opcion
                else:
                    print("Opción inválida. Color no válido.")
            else:
                print("Opción inválida. Intente de nuevo.")
        except IndexError:
            print("Posición fuera del rango del tablero. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    
    # Contar el número de filas y columnas
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    print(f"Número de filas: {num_filas}")
    print(f"Número de columnas: {num_columnas}")
    
    
    # Generar la imagen de Graphviz
    dot = graphviz.Digraph(format='png', graph_attr={'rankdir': 'TB'})

    # Agregar el nodo inicial
    dot.node('NodoInicial', 'Colorealo Guatematel', shape='none')

    # Agregar el nodo de información de filas y columnas
    info_nodo_id = 'Info'
    info_nodo_label = f'Filas: {num_filas}\nColumnas: {num_columnas}'
    dot.node(info_nodo_id, info_nodo_label, shape='box', style='filled', fillcolor='lightgray')
    dot.edge('NodoInicial', info_nodo_id)

    # Agregar nodos de la primera fila
    for columna in range(m):
        nodo_id = f'0-{columna}'
        dot.node(nodo_id, f'Fila 1', shape='none')
        dot.edge(info_nodo_id, nodo_id)

    # Agregar nodos de las filas
    for fila in range(n):
        for columna in range(m):
            filaf = fila + 1
            columf = columna + 1
            nodo_id = f'{fila}-{columna}'  # Etiqueta del nodo en formato "fila-columna"
            color_nodo = colores[tablero[fila][columna]] if tablero[fila][columna] != ' ' else 'white'
            dot.node(nodo_id, nodo_id, style='filled', fillcolor=color_nodo, shape='circle')
            if fila > 0:
                dot.edge(f'{fila-1}-{columna}', nodo_id)

    dot.render('tablero')
    print("Imagen del tablero generada como 'tablero.png'")

# Función principal
def main():
    print("-------Colorealo--------")
    print("1-crear tablero")
    print("2-Mostrar datos del estudiante")
    print("3-salir")
    print("-------Guatematel------")
    
    opcion = input("Opción: ")
    while opcion != '3':
        if opcion == '1':
            print("-------Colorealo--------")
            ancho = int(input("Por favor ingrese el ancho del tablero: "))
            alto = int(input("Por favor ingrese el alto del tablero: "))
            print("-------Guatematel------")
            crear_tablero(ancho, alto)
        elif opcion == '2':
            print("-------Colorealo--------")
            mostrar_datos_estudiante()
            print("-------Guatematel------")
        else:
            print("Opción inválida. Por favor elija una opción válida.")
        
        print("-------Colorealo--------")
        print("1-crear tablero")
        print("2-Mostrar datos del estudiante")
        print("3-salir")
        print("-------Guatematel------")
        opcion = input("Opción: ")

    print("Saliendo del programa...")

if __name__ == "__main__":
    main()



