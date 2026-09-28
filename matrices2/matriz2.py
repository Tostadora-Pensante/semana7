#Este programa pide los datos de una matriz 2x2 y los multiplica
print ("Calculadora de Matriz 3x3 :v")
print("Ingrese los valores en la matriz.")
matriz=[]

for fila in range (3):
    matriz.append([])
    for columna in range(3):
        valor = int(input(f"Fila: {fila+1}, Columna: {columna+1}: "))
        matriz[fila].append(valor)




for fila in matriz:
    print(fila)
k = int(input("Ahora dime el escalar para multiplicar a la matriz: "))

matrizB = []
for i in range(len(matriz)):
    matrizB.append([])
    for j in range(len(matriz)):
        matrizB[i].append(k * matriz[i][j])

print("="*13)
print("Escalar", k)
for fila in matrizB:
    print(fila)