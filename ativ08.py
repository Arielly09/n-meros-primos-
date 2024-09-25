matriz = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]
todos_positivos = True

for linha in matriz:
    for numero in linha:
        if numero < 0:
            print("Há um número negativo na matriz.")
            todos_positivos = False
            break
    if not todos_positivos:
        break

if todos_positivos:
    print("Todos os números são positivos.")
