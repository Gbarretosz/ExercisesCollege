arquivo = './lista.txt'
with open(arquivo, 'a') as lista:
    lista.write('\nGabriel')
with open(arquivo, 'r') as lista:
    for nomes in lista:
        print(nomes, end='')