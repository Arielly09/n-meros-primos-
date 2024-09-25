numeros = [1, 2, 3, 4, 5, 6, 7, 8]
contagem_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        contagem_pares += 1

if contagem_pares > 0:
    print(f"Número de pares: {contagem_pares}")
else:
    print("Não há números pares.")
