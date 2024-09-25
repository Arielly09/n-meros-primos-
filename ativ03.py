matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numero_procurado = 5
encontrado = False

for linha in matriz:
    for numero in linha:
        if numero == numero_procurado:
            print(f"Número {numero_procurado} encontrado!")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"Número {numero_procurado} não está na matriz.")
