'''
Andrey Oliveira Ferreira
05/06/2025

Programa de venda de camisetas
'''

#função que faz o usuário escolher o modelo de camisa.
def escolha_modelo():
    #Trecho principal que repete se o usuario errar a resposta
    while True:
        try:
            #Exibe as opções disponiveis para o usúario.
            print('              Descrição                | Valor únitario')
            print('Camiseta Manga Curta Simples (MCS)     |     R$1,80')
            print('Camiseta Manga Longa Simples (MLS)     |     R$2,10')
            print('Camiseta Manga Curta Com Estampa (MCE) |     R$2,90')
            print('Camiseta Manga Longa Com Estampa (MLE) |     R$3,20')
            print()

            #insere o modelo e retorna o valor de cada opção,
            modelo = input('Insira o modelo desejado (MCS/MLS/MCE/MLE): ')
            if (modelo == 'MCS'):
                return 1.80
            elif (modelo == 'MLS'):
                return 2.10
            elif (modelo == 'MCE'):
                return 2.90
            elif (modelo == 'MLE'):
                return 3.20
            else:
                print('Opção invalida. Tente novamente...')
                print()
                continue
        except ValueError:
            print('Valor inválido, tente novamente')

#Função que recebe a quantidade de camisas e retorna um desconto especifico
def num_camisetas():
    #trecho principal da função que repete se o usuario errar a resposta
    while True:
        try:
            quantidade = int(input('Quantas camisetas você deseja?: '))
            #retorna 1 porque se for 0 dá erro no final do programa
            if(quantidade < 1):
                print('Não aceitamos valores negativos ou nulos')
            elif (quantidade < 20):
                return quantidade
            elif (quantidade >= 20 and quantidade < 200):
                return quantidade * (95/100)
            elif (quantidade >= 200 and quantidade < 2000):
                return quantidade * (93/100)
            elif (quantidade >= 2000 and quantidade <= 20000):
                return quantidade * (88/100)
            else:
                print('Infelizmente não aceitamos pedidos acima de 20000.')
                print()
                continue
        except ValueError:
            print( 'Opa. Valor não aceito. Tente novamente')

#Essa função define o valor do custo do frete dependendo da escolha do usuário
def frete():
    #Exibe as opções disponiveis
    print(' ' * 12, 'Opções de frete')
    print('(0) | Retirar na fábrica       | GRÁTIS')
    print('(1) | Frete por transportadora | R$100,00')
    print('(2) | Frete por Sedex          | R$200,00')
    print()

    #Trecho que recebe a opção e retorna o valor escolhido, repete se o usuario escrever errado
    while True:
        try:
            opcao = int(input("Qual opção deseja escolher?(0/1/2): "))
            if (opcao == 0):
                return 0
            elif (opcao == 1):
                return 100
            elif (opcao == 2):
                return 200
            else:
                print('Opss. Valor invalido. Tente novamente...')
        except ValueError:
            print('Opss. Valor invalido. Tente novamente...')

#Mensagem de boas vindas
print('\nOlá, seja bem vindo a loja de camisetas. Meu nome é Andrey Oliveira\n')

#Programa principal com alguns espaços para melhorar a visualização do resultado
modelo = escolha_modelo()
print()
quantidade = num_camisetas()
print()
valor_frete = frete()
print()
total = (modelo * quantidade) + valor_frete

print('Informações do pedido')
print('Modelo: R$%.2f * quantidade com desconto: %d + frete: R$%.2f' % (modelo, quantidade, valor_frete))
print('Total a pagar: R$%.2f' % total)