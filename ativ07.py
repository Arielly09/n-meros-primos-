array = [3, 1, 7, 5, 9, 2]
maior_numero = array[0]  # Começamos assumindo que o primeiro elemento é o maior

for numero in array:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número no array é: {maior_numero}")
