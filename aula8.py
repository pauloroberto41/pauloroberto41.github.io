# Listas


informaçoes_de_filmes = ['Inception', 2010, True, 2.28]

#indexação
# print(nomes[1])
# print(nomes[1][2])
# print(nomes[1] + ' gosta de ver ' + informaçoes_de_filmes[0] +'!')


# nomes.append('Roberto')
# print(nomes)
# nomes[1] = "Marcelo"
# nomes.pop()
# print (nomes)
# nomes.pop()
# print (nomes)
# nomes.pop()
# print (nomes)



quantidades = [ 10, 30, 50, 20, 6.99 ]
# print(sum(quantidades))

nomes = [ 'Ana', 'Luíza', 'x', 'Nadir', 'Carlos' ]


# print(max(nomes))

# print(max(quantidades))


# print(min(nomes))
# print(min(quantidades))

# print(sorted(quantidades))


# print(sorted(nomes))

# print(sorted(nomes, reverse = True), )
# print(sorted(quantidades, reverse = True), )



#string são imutáveis

palavra = 'gato'
# palavra[2] = 'l'

#print(palavra[:2] )

# palavra_nova = palavra[:2] + 'l' + palavra[3:]
# print(palavra_nova)



#Tuplas

#Tuplas são imutáveis

# coordenadas = ('48°51"30.1"N', '2°17"40.0"E')


# coordenadas[0] = '00°46"12.9"N' #erro

# print(coordenadas)

# pontos = (7,8,9,8,7,10,7)

# letras = ('7','8','9','8.0','7',False,'7')

# print(pontos.count(8.0))
# print(pontos.count(7))
# print(pontos.count(10))
# print(pontos.count(0))


# print(letras.count(True))
# print(letras.count("7"))
# print(letras.count("10"))
# print(letras.count('0'))


#descompactação de tuplas
# aniversário = (1, 'Abril', 2000, '00:00')

# dia, mes, ano, hora = aniversário


# print(dia)
# print(mes)
# print(hora)

#Operador * descompactador de tuplas, util para comprimento desconhecido. 
pontuação = ('A',"B",68,39,47,80)

ganhador, *restante = pontuação
print(ganhador)
print(restante)

"""

#Conjuntos que diferentes de listas e tuplas são coleções desordenadas e são criados com chaves {}

visitantes = {'Eduardo', 'Paulo', 'Marcos', 'Camila'}

print(visitantes)
#print(visitantes[0]) #erro, pois os conjuntos são desornados, diferente das listas e das tuplas. Mas porque são desordenados? print novamente...


#Conjuntos não podem ter duplicatas, o que é util para os desenvolvedores, para garantir que os intens na coleção sejam únicos. Por exemplo em um app de uma mídia social amigos não podem ser duplicados. 


amigos = {"Fernanda", 'Fabricio', 'Eduarda', 'Carla', 'Carla', 'Fernanda'}
print(amigos)
#print(len(amigos))

estatus_do_carro = {'Audi', 'Q5', 2008, 4.0}
print(estatus_do_carro)

#conjuntos são mutáveis, ou seja, podemos adicionar e remover itens, dele.  usando add() e remove()
amigos.add('Roberto')
amigos.remove('Eduarda')

# amigos.remove('André')

# amigos.append('André') # não funciona pois é desordenados
amigos.clear()
print(amigos) #retorna um set() vazio.


set1 ={"maçã", 'banana'}
set2 ={"goiaba", 'banana'}
combinar = set.union(set2)


print(combinar) #retorna um set() vazio.

unico = set.difference(set2)

# resumindo:

        mutaveis    ordenadas     index  duplicadas
Listas     ok         ok          ok       ok

                   
Tuplas     não         ok           ok       ok

                   
Sets        ok         não         não      não
"""




