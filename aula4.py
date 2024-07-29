


print(1)
print(2)
print(3)




x = 1
print(x)


x= 2
print(x)


x= 3
print(x)


#while True:
    #print("loop eterno!") se tirar o comentário vira um loop eterno! 😉

    # código a ser repetido 


valor  = True
while valor:
         
    print("é verdadadeiro!")
    valor = False
  

print("Finalizado")
 
import numero_secreto 

número_oculto = numero_secreto.número_secreto
adivinhe = None
# == igualdade
# != diferente
while adivinhe != número_oculto:
    adivinhe = int(input("Adivinhe o número (1-10): "))
    if adivinhe < número_oculto:
        print("Muito baixo!")
    elif adivinhe > número_oculto:
        print("Muito alto!")

print(f"Parabéns! Você adivinhou o número {número_oculto}.")



# True escolha == '4'=> False
# False  escolha != '4 => True

# string = str = 'afdfa'
# inteiro = int => 4
#booleanos = boll => True, False
# float = decimais => 0.4

while True:
    print()
    print("Menu:")
    print('____________________')
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    print('____________________')
    escolha = input("Escolha uma opção: ")
    print('____________________')

    if escolha == '1':
        print("Você escolheu a Opção 1.")
        print('____________________')
        continue

    elif escolha == '2':
        print("Você escolheu a Opção 2.")
        print('____________________')
        continue

    elif escolha == '3':
        print("Você escolheu a Opção 3.")
        print('____________________')
        continue

    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        print('____________________')


