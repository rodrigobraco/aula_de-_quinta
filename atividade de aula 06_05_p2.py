def ocorrencias(lst, x):
	qtd_ocorrencias = 0
	tamanho = len(lst)

        for i in range(0, tamanho):
                if lst[i] == x:
                        qtd_ocorrencias = qtd_ocorrencias + 1
	return qtd_ocorrencias
lista = [8, 9, 10, 6, 5, 3, 8, 7, 8, 3, 8]
resposta= ocorrencias(lista, 8)
print("Foram encontradas", resposta, "ocorrencias!")
