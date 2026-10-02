#Este programa pide los datos de una matriz 2x2 y los multiplica
def calculadoraMatriz(): 
    print ("Calculadora de Matriz cuadrada :v")
    print("Ingrese los valores en la matriz.")
    matriz=[]

    for fila in range (1):
        matriz.append([])
        for columna in range(1):
            while True:
                try:
                    valor = int(input(f"Fila: {fila+1}, Columna: {columna+1}: "))
                    break
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número entero.")
            matriz[fila].append(valor)

    for fila in matriz:
        print(fila)

    while True:
        try:
            k = int(input("Ahora dime el escalar para multiplicar a la matriz: "))
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    matrizB = []
    for i in range(len(matriz)):
        matrizB.append([])
        for j in range(len(matriz)):
            matrizB[i].append(k * matriz[i][j])

    print("="*13)
    print("Escalar", k)
    for fila in matrizB:
        print(fila)