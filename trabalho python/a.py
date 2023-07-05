#Mensagem de boas vindas
print('------------------------------------------------------------------------------------------')
print("Olá, seja bem vindo(a)! Meu nome é Maria Eduarda, sou um programa de cálculo de descontos.")
print('------------------------------------------------------------------------------------------')

#Variaveis
valor_produto = float(input("Digite o valor do produto: "))
quantidade_produto = float(input("Qual a quantidade desejada do produto? "))

#Quando a quantidade for menor que 200 o desconto será de 0%
if quantidade_produto <200:
    desconto = 0
#Quando a quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%
elif quantidade_produto >=200 and quantidade_produto <1000:
    desconto = 0.05 
#Quando a quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
elif quantidade_produto >= 1000 and quantidade_produto <2000:
    desconto= 0.1
#Quando a quantidade for igual ou maior que 2000 o desconto será de 15%
else:
    desconto= 0.15

#Calculo de desconto
total_desconto= desconto * valor_produto * quantidade_produto
#Calculo do total sem desconto
total_sem_desconto= valor_produto * quantidade_produto
#Calculo do total com desconto
total_com_desconto= total_sem_desconto - total_desconto

print (f"O valor total da sua compra é de R${total_sem_desconto}")
print(f"O desconto total é de {desconto}%")
print(f"O valor total da sua compra é de R${total_com_desconto}")
print('---------------------------------------------------------------------------------')
print('                      Obrigado por utilizar o programa!')
print('---------------------------------------------------------------------------------')



