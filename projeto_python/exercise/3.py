mercado = open('listaMercado.txt', 'w')
itens = ['--Itens adicionados--' '\nLaranja' '\nManteiga' '\nAchocolatado' '\n']
mercado.writelines(itens)
mercado.close()
print(itens)

item = './listaMercado.txt'
Sim = '1'
Nao = '2'
adicionar = str(input('Deseja adicionar algum item? \n1-Sim \n2-Não\n->'))
itemadd = str(input('Digite o nome do item: '))

if adicionar == Sim:
    with open(item, 'a') as mercado:
        mercado.write(itemadd)

with open(item, 'r') as mercado:
    for itens in mercado:
        print(itens, end='')

