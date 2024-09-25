array = [1, 2, 3, 2, 4, 2, 5]
valor_procurado = 2
contagem = 0

for numero in array:
    if numero == valor_procurado:
        contagem += 1

print(f"O valor {valor_procurado} aparece {contagem} vezes no array.")
