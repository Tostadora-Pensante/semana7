#Suma de matrices
"""Leer dos matrices 3x3 y sumar en una matriz"""
def sumMatrices():
    print ("Calculadora de Matriz 3x3 :v")
    print("="*13)
    print("Ingrese los valores en la matriz 1:")
    matriz=[]
    
    for fila in range (3):
        matriz.append([])
        for columna in range(3):
            while True:
                try:
                    valor = int(input(f"Fila: {fila+1}, Columna: {columna+1}: "))
                    break
                except ValueError:
                    print("Ingrese un numero valido.")
                    
                matriz[fila].append(valor)

    print("="*13)
    print("Ingrese los valores de la segunda matriz:")
    matrizB = []

    for fila in range (3):
        matrizB.append([])
        for columna in range(3):
            while True:
                try:
                    valor = int(input(f"Fila: {fila+1}, Columna: {columna+1}: "))
                    break
                except ValueError:
                    print("Porfavor ingrese un numero valido.")
                
            matrizB[fila].append(valor)
  
    
    
    matrizC = []
    for i in range(len(matriz)):
        matrizC.append([])
        for j in range(len(matriz)):
            matrizC[i].append(matriz[i][j] + matrizB[i][j])

    print("="*13)
    print("Sumar")
    print("="*13)
    print("Matriz 1")
    for fila in matriz:
        print(fila)
    print("="*13)
    print("Matriz 2")
    for fila in matrizB:
        print(fila)
    print("="*13)
    print("Resultado de la suma")
    for fila in matrizC:
        print(fila)