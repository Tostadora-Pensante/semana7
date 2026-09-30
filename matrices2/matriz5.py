"""
dada una matriz de identidad nxn
mostrar en color azul solo la diagonal de 1
"""
n = int(input("dimensiones de la matriz cuadrada: "))
def mostrarAzul(n):
    azul = "\033[94m"
    reset = "\033[0m" 
    
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(f"{azul}1{reset}")
            else:
                fila.append("0")
        print(" ".join(fila))

mostrarAzul(n)
