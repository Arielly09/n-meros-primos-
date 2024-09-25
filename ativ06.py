numeros = [3, 5, 7, -2, 8, -1]
numero_negativo = None

for numero in numeros:
    if numero < 0:
        numero_negativo = numero
        print(f"Primeiro número negativo encontrado: {numero_negativo}")
        break

if numero_negativo is None:
    print("Não há números negativos na lista.")
