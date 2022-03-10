def cria_matriz(m, n, valor):
    matriz = []
    for i in range(m):
        linha = [valor] * n
        matriz.append(linha)
    return matriz
def imprime_matriz(a):
    lin_a = len(a)
    col_a = len(a[0])
    for i in range(0, col_a):
        for j in range(0, col_a):
            print('%7.2f'% a[i][j],end)
        print()
        

def soma_matriz(a,b):
    lin_a = len(a)
    col_a = len(a)
