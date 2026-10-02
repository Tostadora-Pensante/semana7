#multiplicaicon de matrices cuadradas
def multMatrices():
    matrizA = []
    matrizB = []
    matrizC = []
    while True:
        try:
            dimension = int(input("dimensiones de la matriz cuadrada: "))
            if dimension < 1:
                print("La dimension debe ser mayor a uno.")
                continue
            break
        except ValueError:
            print("Porfavor ingrese un numero positivo.")
            


    for i in range(dimension):
        matrizA.append([])
        for j in range(dimension):
            while True:
                try:
                    matrizA[i].append(int(input(f"fila {i+1}, columna {j+1}: ")))
                    break
                except ValueError:
                    print("Porfavor ingrese un numero entero valido.")
                    
    
    print("="*13)
    print("Matriz A")
    for fila in matrizA:
        print(fila)

    print("="*13)
    print("Ambas matrices tienen las mismas dimensiones")
    print("Inserte los valores de la matriz B")

    for i in range(dimension):
        matrizB.append([])
        for j in range(dimension):
            while True:
                try:
                    matrizB[i].append(int(input(f"fila {i+1}, columna {j+1}: ")))
                    break
                except ValueError:
                    print("Ingrese un numero valido.")
                    
                    
   
   
    print("="*13)

    print("Matriz B")
    for fila in matrizB:
        print(fila)

    print("="*13)

    for i in range(dimension):
        fila = []
        for j in range(dimension):
            suma = 0
            for k in range(dimension):
                suma += matrizA[i][k] * matrizB[k][j]
            fila.append(suma)
        matrizC.append(fila)

    print("Matriz A")
    for fila in matrizA:
        print(fila)
    print("="*13)
    print("Matriz B")
    for fila in matrizB:
        print(fila)
    print("="*13)
    print("La matriz resultante es:")
    for fila in matrizC:
        print(fila)
