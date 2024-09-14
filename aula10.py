#Dicionários
lista = ['nomes', 34, 59.9, False]

contatos = { 
    'Rafaela': 9814688721,
    'Pedro': 889788547,
    'Ana': 989744474,
    'Rafael': 9814688000 
    }

#composto por um conjunto de chaves e valores.

#Consiste em relacionar uma chave a um valor específico.


#Usamos chaves {}

# exemplo. 

tabela = {

    'Alface': 0.45,
    'Batata': 1.12,
    'Tomate': 1.50,
    'Feijão': 3.45,
 
}
# lista = ['Alface', 'Batata', 'Tomate', 'Feijão'] #para comparação

# print(lista[0])
#diferente das listas, em que o índice é um número, dicionários utilizam suas chaves como índice. 

# print(tabela['Alface'])
# print(tabela['Batata'])
# print(tabela['Tomate'])
# print(tabela['Feijão'])
# print(tabela)

# tabela['Alface'] = 2.5

# print(tabela['Alface'])


tabela['Cebola'] = 1.2 

tabela['Cebola'] = 22 


# print(tabela)

#temos ordem no dicionário a partir da versão 3.7!

# print(tabela['Manga'])

#exceção de KeyError será mostrado no terminal
#para verificar se uma chave pertence ao dicionário, podemos usar o operador in:


tabela = {
    'Alface': 0.45,
    'Batata': 1.12,
    'Tomate': 1.50,
    'Feijão': 3.45,
 
}

# print('Manga' in tabela)

# print('Batata' in tabela)


#podemos obter uma lista com as chaves do dicionário, ou até mesmo uma lista de valores associados a ele:

# contatos['Romario'] = 8178754200 
# print(contatos)
# print()
# print()
# print()
# print(contatos.keys())
# print(contatos.values())

#ambos podem ser utilizados dentro de um for ou serem tranformados em lista usando a função list.

# while True:
#     produto = input('Digite o nome do produto, fim para terminar: ')
#     if produto == 'fim' :
#         break

#     if produto in tabela:
#         print(f'Preço{tabela[produto]:5.2f}')
#     else:
#         print('Produto não encontrado! ')

# print('FIM!!!')      

#para apagar uma chave, usamos o del:


del tabela['Alface']

print(tabela)
