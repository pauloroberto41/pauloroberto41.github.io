#range
"""

for v in range(10):
    print(v)

for t in range(3, 33, 3):
    print(t, end=' ')
print()




#Enumerate
#sem enumerate
L = [5, 9, 13]
x = 0

for e in L:
    x += 1
    print(f'Esse é o {x} número: {e}')



#com enumerate

L = [5, 9, 13]
for x , e in enumerate(L):
    print(f'Esse é o {x + 1} número: {e}')

"""

# Operações com Listas

L = [ 10, 6 , 2, 4]
máximo = L[0]

for e in L:
    if e > máximo:
        máximo = e

print(máximo)



"""
# Lendo e imprimindo uma lista de compras
compras = []
while True:
    produto = input("Produto:")
    if produto == "fim":
        break
    compras.append(produto)
for p in compras:
    print(p)


#Listas dentro de listas

L = ["maçãs", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra)

    
#Listas de listas

produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
print(compras)

#impressão das compras:

produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]:5.2f}")
    

"""