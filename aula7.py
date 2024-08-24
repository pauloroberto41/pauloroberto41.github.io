#Repetições aninhadas

"""
tabuada = 1

while tabuada <= 10:
    número = 1
    while número <= 10:
        print(f'{tabuada} x {número} = { tabuada * número}')
        número += 1
    tabuada += 1
    print( )

x = 0
y = 0
z = 0

while x <= 10:
    while y < 10:
        while z < 10:
            print(x, y, z)
            z += 1
        print(x, y, z)
        y += 1
    print(x, y, z)
    x += 1  





dados_da_lista = ['azul', 100, 87.9, False]

print(dados_da_lista[0])

lista_alterada = dados_da_lista[0] = True

print(dados_da_lista)

nome = ['Abacate','laranja' ]


# print(nome[0][1])
# print(nome[1][0])


muda_letra = nome[0] = 'c'
print(nome)


cores = ['azul', 'verde', 'amarela', 'vermelha']

frutas= ['blueberry ', 'limão', 'carambola', 'framboesa']

index_fruta = 0
index_cor = 0

for cor in cores:
    for fruta in frutas: 
        if index_fruta ==  index_cor:
            print(f'A cor da fruta {fruta } é {cor}.')
        index_cor += 1
    index_fruta += 1
    index_cor = 0

            

"""
"""

# Listas

números = [1, 2, 3]



# Cópia e fatiamento de listas

números_copiados = números

print(números)
print(números_copiados)


números_copiados[0] = 6

print(números)
print(números_copiados) 
"""




# Explicação:
"""
    Quando alteramos o valor de números_copiados[0] = 6, estamos, na verdade, modificando a lista original números. Isso acontece porque números_copiados não é uma nova lista, mas sim um "apelido" para a lista números. Em termos mais técnicos, ambos os nomes (números e números_copiados) estão apontando para o mesmo endereço na memória.

    Para visualizar melhor, vamos usar um exemplo de C++. No C++, temos o conceito de ponteiros, que são endereços de memória onde os dados são armazenados. Imagine que dentro da variável números[0], temos um endereço de memória, algo como 0x454x54x54. Ao criar um "apelido" de números para números_copiados, estamos apenas mudando o nome, mas o endereço de memória continua o mesmo, 0x454x54x54.

    Então, quando você altera o valor de números_copiados[0], você está modificando o valor que está armazenado nesse endereço de memória. Como números e números_copiados apontam para o mesmo local, qualquer mudança feita em um será refletida no outro.

    Esse conceito é essencial para entender como referências funcionam em Python e em outras linguagens que utilizam referências ou ponteiros para gerenciar a memória.


"""

#fatiamentos slices



dados = [1,2,3,4, 6, 7, 8]

print (dados[0:3])

print (dados[0:6])

print (dados[:3])
print (dados[2:])

print (dados[-3: -1])

print (dados[0: 10: 3])

print (dados[::-1])


