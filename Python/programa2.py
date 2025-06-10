'''
Andrey Oliveira Ferreira
04/06/2025

Programa de vendas de marmita

1) a indentação é com quatro espaços ou com tab simples?
2) pode usar mais de um print para representar o menu na questão 2/4?
3) Pode forçar o usúario a digitar corretamente (com while) a resposta? questão 2/4
'''

#exibe a mensagem de boas vindas e o menu
print("\nOlá, seja bem vindo a loja de Andrey Oliveira! \n")
print(("-" * 16) + "Cardapio disponivel" + ("-" * 16))
print('    Tamanho    |  Bife Acebolado  | Filé de Frango')
print('       P       |       R$16,00    |     R$15,00')
print('       M       |       R$18,00    |     R$17,00')
print('       G       |       R$22,00    |     R$21,00')
print(("-" * 51))

#armazena o valor das compras do usúario
acumulador = 0

#Trecho principal do progama
while True:    
    #Recebe o valor digitado pelo usúario
    sabor = input('Escolha o sabor desejado (BA/FF): ')
    if (sabor != 'BA' and sabor != 'FF'):
        print("Sabor inválido. Tente novamente")
        print()
        continue

    #Recebe o tamanho escolhido pelo usúario
    tamanho = input('Escolha o tamanho desejado (P/M/G): ')
    if (tamanho !=  'P' and tamanho != 'M' and tamanho != 'G'):
        print('Tamanho inválido. Tente novamente')
        print()
        continue

    #esse trecho decide o valor da escolha atual do usúario
    if (sabor == 'BA' and tamanho == 'P'):
        valor = 16
    elif (sabor == 'BA' and tamanho == 'M'):
        valor = 18
    elif (sabor == 'BA' and tamanho == 'G'):
        valor = 22
    elif (sabor == 'FF' and tamanho == 'P'):
        valor = 15
    elif (sabor == 'FF' and tamanho == 'M'):
        valor = 17
    elif (sabor == 'FF' and tamanho == 'G'):
        valor = 21

    #prepara para enviar uma mensagem
    if (sabor == 'BA'):
        mensagem_sabor = 'Bife Acebolado'
    else:
        mensagem_sabor = 'Filé de Frango'

    #imprime o valor atual do pedido
    print(f'Você pediu um {mensagem_sabor} no valor de: R${valor}.00\n')

    #faz a varivel externa acumular os valores da escolha do usúario
    acumulador += valor

    #pergunta ao usúario se ele quer continuar ou não o programa
    pergunta = ''
    while (pergunta != 'S' and pergunta != 'N'):
        pergunta = input('Deseja pedir mais alguma coisa? (S/N): ')
    
    #encerra ou continua o programa
    if (pergunta == 'S'):
        print()
        continue
    else:
        break

#Exibe o resultado final na tela
print(f'\nValor final do pedido: R${acumulador}.00')