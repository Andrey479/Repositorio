'''
Andrey Oliveira Ferreira
02/06/2025

Programa que calcula o juros para um empresa de cartão de crédito
'''
#dá boas vindas ao usúario
print("Seja bem vindo, meu nome é Andrey Oliveira e estou aqui para te ajudar")

#recebe as informações para analise: o valor e quantidade de parcelas
valorDoPedido = float(input("Qual o valor do pedido?: "))
quantidadeParcelas = int(input("Quantas parcelas deseja dividir?: ")) 

#Esse trecho analisa quanto de juros cada parcela vai ter
if (quantidadeParcelas < 4):
    juros = 0
elif (quantidadeParcelas >= 4 and quantidadeParcelas < 6):
    juros = 4/100
elif (quantidadeParcelas >= 6 and quantidadeParcelas < 9):
    juros = 8/100
elif (quantidadeParcelas >= 9 and quantidadeParcelas < 13):
    juros = 16/100
else:
    juros = 32/100

#esse trecho calcula o valor da parcela e o valor total parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#exibe o resultado final para o usuario
print("O valor das parcelas será de: R$%.2f" % valorDaParcela)
print("O valor total parcelado será de: R$%.2f" % valorTotalParcelado)

