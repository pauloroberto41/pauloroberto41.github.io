# Aula de python básico e avançado - 15/06

# print(len('Paulo'))

# s = 100

# dados = s * 'paulo'

# print(dados)


# %s - Strings
# %f - Numeros Decimais - float
# %d - Numeros inteiros
idade = 34
# print( 'Ana tem %d anos de idade' % idade)

# print( 'Ana tem ', idade, 'anos de idade')

# print("valor do %d" % idade)

# print(f'Ana tem {idade} anos de idade') 





# nome = 'Ana'
# print( '%s tem 34 anos' % nome)
#%f - Numeros Decimais - float

# print('%0.2f' %10)
"""
"""

# format

# print('{} tem {} anos e R${} no bolso'.format(nome, idade, grana))
# print(f'{nome} tem {idade} anos e R${grana} no bolso')
# print(nome,  'tem' , idade, 'e R$', grana, 'no bolso') 

nome = 'Roberto'
idade = 43
grana = 1000
# print(f'{nome} tem {idade} e R${grana} no bolso') 


# print('{:1} tem {:3} anos e R${:20.3f} no bolso'.format(nome, idade, grana))


# print(f'{nome:20} tem {idade:20} e R${grana:50.2f} no bolso') 

# A = 0
# B = 1
# C = 2

# D = 3
# E = 4

# F = 5
# G = 6

# print(letras[0:3])

# Codigo_completo = "12451F - IPANEMA -VD"
# codigo_em_numeros = Codigo_completo[0:6]
# print("codigo_em_numeros: ", codigo_em_numeros)


# print(letras[:3])
# print(letras[3:5])
letras = 'ABCDEFG'

# print(letras[-1])
'ABCDEFG'

# A = -7
# B = -6
# C = -5

# D = -4
# E = -3

# F = -2
# G = -1



# Sequência de tempo

# dívida = 0

# compra = 100


# dívida = dívida + compra #100

# compra = 200


# dívida = dívida + compra #300

# compra = 300

# dívida = dívida + compra #600

# compra = 0

# print(dívida)

#conversão da entrada de dados

anos = int(input('Anos de trabalho: '))


print(f"Anos: {anos + 10}")

print("Anos:" , anos + 10)
