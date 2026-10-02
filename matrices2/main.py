from escalarmatriz import escaledMatriz
from multmatriz import calculadoraMatriz
from sumaMatriz import sumMatrices 
from multiplicandoMatrices import multMatrices 
from diagonalAzul import mostrarAzul 

def pausar():
    input("Presione Enter para continuar...")


def menu():
    while True:
        print("="*13)
        print("Actividades con matrices")
        print("1. Escalar una Matriz 2x2")
        print("2. Calcular una Matriz 2x2")
        print("3. Sumar dos matrices 3x3")
        print("4. Multiplicar dos matrices 2x2")
        print("5. Mostrar diagonal en azul")
        print("0. Salir")
        try:
            opcion = int(input("Seleccione una opción (0-5): "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue
        if opcion < 0 or opcion > 5:
            print("Opción inválida. Por favor, seleccione un número entre 0 y 5.")
            continue
        if opcion == 0:
            print("Saliendo del programa...")
            break
        if opcion == 1:
            escaledMatriz()
        elif opcion == 2:
            calculadoraMatriz()
        elif opcion == 3:
            sumMatrices()
        elif opcion == 4:
            multMatrices()
        elif opcion == 5:
            try:
                n = int(input("dimensiones de la matriz cuadrada: "))
                mostrarAzul(n)
            except ValueError:
                print("Error:Ingrese un número entero porfavor.")
        pausar()

menu()