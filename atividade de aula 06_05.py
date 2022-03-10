palavra = "faculdade impacta curso de redes RC1A"
tamanho = len(palavra)
i = 0


print("usando while")
while i < tamanho:
        print(palavra[i])
        i = i + 2

print("usando for")
for i in range(0, tamanho, 2):
        print(palavra[i])
