array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma_impares = 0

for numero in array:
    if numero % 2 != 0:
        soma_impares += numero

print(f"A soma dos números ímpares é: {soma_impares}")
