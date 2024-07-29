# Aula de python básico e avançado - 22/06


#Condições if, else, Estruturas aninhadas e elif. 

#Condição if
#

"""
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:

    print("O primeiro valor é o maior!")

elif b > a:
    print("O segundo valor é o maior!")

else:
    print("Os valores são iguais!")


print("Final do programa!")
"""
# idade = int(input("Digite a idade do seu carro: "))

# if idade <= 3:
#     print("Seu carro é novo")

# if idade > 3:
#     print("Seu carro é velho")





# Cálculo de imposto de Renda
salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
   

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f'Salário: R${salário:10.2f} Imposto a pagar: R$ {imposto:6.2f}')






"Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.Nesse caso, exiba o valor da multa, combrando R$ 5 por km acima de 80 km/h."


"Escreva um programa que leia três números e que imprima o maior e o menor."

"Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, calcule um aumento de 15%."