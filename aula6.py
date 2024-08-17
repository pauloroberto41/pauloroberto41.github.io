# # 10/08/2024

# # if, elif - else

# #######################################
# linguagem = input("Qual linguagem de programação você quer aprender? ")

# if linguagem == "JavaScript":
#     print("Você pode se tornar um desenvolvedor web.")

# elif linguagem == "Python":
#     print("Você pode se tornar um Cientista de Dados")

# elif linguagem == "PHP":
#     print("Você pode se tornar um desenvolvedor backend")

# elif linguagem == "Solidity":
#     print("Você pode se tornar um desenvolvedor Blockchain")

# elif linguagem == "Java":
#     print("Você pode se tornar um desenvolvedor de aplicativos móveis")
    
# else:
#     print("A linguagem não importa, o que importa é resolver problemas.")

  
# #######################################
# linguagem = input("Qual linguagem de programação você quer aprender? ")

# if linguagem == "JavaScript":
#     print("Você pode se tornar um desenvolvedor web.")

# else:

#     if linguagem == "Python":
#         print("Você pode se tornar um Cientista de Dados")
    
#     else:
#         if linguagem == "PHP":
#             print("Você pode se tornar um desenvolvedor backend")
#         else:

#             if linguagem == "Solidity":
#                 print("Você pode se tornar um desenvolvedor Blockchain")
#             else:

#                 if linguagem == "Java":
#                     print("Você pode se tornar um desenvolvedor de aplicativos móveis")
                    
#                 else:
#                     print("A linguagem não importa, o que importa é resolver problemas.")

# #####################################
# # Saída dependerá da entrada do usuário

# linguagem = input("Qual linguagem de programação você quer aprender? ")

# match linguagem:
#     case "JavaScript":
#         print("Você pode se tornar um desenvolvedor web.")

#     case "Python":
#         print("Você pode se tornar um Cientista de Dados")

#     case "PHP":
#         print("Você pode se tornar um desenvolvedor backend")

#     case "Solidity":
#         print("Você pode se tornar um desenvolvedor Blockchain")

#     case "Java":
#         print("Você pode se tornar um desenvolvedor de aplicativos móveis")

#     case _:
#         print("A linguagem não importa, o que importa é resolver problemas.")


# notas = [8, 9, 7, 6, 1]

# soma = 0
# i = 0
# while i < len(notas):
#     soma += notas[i]
#     #soma = soma + notas[i]
#     i += 1


# media = soma / len(notas)
# print(f'A média das notas é: {media:.2f}')



# notas = [0, 0, 0, 0, 0]

# soma = 0
# x = 0



# while x < 5:
#     notas[x] = float(input(f'Nota { x + 1}: '))
#     soma += notas[x]
#     x += 1

# x = 0

# while x < 5:
#     print(f'Notas {x + 1}:{notas[x]:10.2f}')
#     x += 1


# print(f'Média:{soma / x:6.2f}')


# #Trabalhando com os índices



# numeros = [0, 0, 0, 0, 0]
# x = 0


# while x < 5:
#     numeros[x] = int(input(f'Número {x + 1}: '))
#     x += 1
# nao_sair = True

# while nao_sair:
#     escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
#     if escolhido == 0:
#         nao_sair = False
 

#     print(f'Você escolheu o número: {numeros[escolhido - 1]}')
  

soma = 0
i = 1
while(i<=3):
    if i == 2:
        i += 1
        continue

    soma += 1
    i += 1

print(soma)



