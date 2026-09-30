#multiplicaicon de matrices cuadradas
matrizA = []
matrizB = []
matrizC = []

print("Ingrese los valores de la matriz_1: ")

for fila in range(2):
    matrizA.append([])
    for colum in range(2):
        valor = (int(input(f"fila {fila+1}, {colum+1}: ")))
        matrizA[fila].append(valor)
for fila in matrizA:
    print(fila)

print("Ingrese los valores de la matriz_2: ")

for fila in range(2):
    matrizB.append([])
    for colum in range(2):
        valor = (int(input(f"fila {fila+1}, {colum+1}: ")))
        matrizB[fila].append(valor)
for fila in matrizB:
    print(fila)


for i in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizA)):
        matrizC[i].append(matrizA[i][j] *  matrizB[i][j])

print("La multipliacion de estas matrices resulta en:  ")
for fila in matrizC:
    print(fila)