'''
Andrey Oliveira Ferreira
10/06/2025

Software de gerenciamento de funcionario
#remover a função valida dados e deixar direto no programa
'''
#função que valida o nome do usuario
def valida_caracteres(tipo):
    while True:
        try:
            #Aqui decide o tipo de dado a receber dependendo da natureza dele
            if (tipo == 'nome'):
                informacao = input('Qual é o nome?: ').upper().strip()
            elif (tipo == 'setor'):
                informacao = input('Qual é o setor?: ').upper().strip()

            #Tratamento de dados
            if not informacao:
                print('Digite algo, não mantenha vazio...')
                continue
            elif informacao.isnumeric():
                print('Numerais e simbolos não são aceitos')
            else:
                return informacao
        except:
            print('\nAlgo deu errado')

#Funcão responsavel por cadastrar o usuario
def cadastrar_funcionario(id):
    global id_global
    global lista_funcionarios
    nome = valida_caracteres('nome')
    setor = valida_caracteres('setor')
    salario = float(input('Qual é o salário?: '))
    dados = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_funcionarios.append(dados.copy())
    dados.clear()
    print(dados)
    id_global += 1

#função reponsavel por consultar os dados dos funcionarios
def consultar_funcionarios():
    while True:
        print()
        print('-' * 10, 'Consultar funcionarios', '-' * 10)
        print('1 | Consultar todos')
        print('2 | Consultar por ID')
        print('3 | Consultar por setor')
        print('4 | Retornar ao menu')
        print()

        try:
            opcao = int(input('Escolha uma opção (1|2|3|4): '))
            
           #consulta todos
            if (opcao == 1): 
                print()
                for dicionario in lista_funcionarios:
                    for chave in dicionario:
                        print(f'{chave.upper()}: {dicionario[chave]}')
                    print()
            #consulta por ID 
            elif (opcao == 2): 
                encontrou = False
                id_buscado = int(input('Digite o ID do funcionario: '))
                for dicionario in lista_funcionarios:
                    if (dicionario['id'] == id_buscado):
                        encontrou = True
                        print()
                        for chave in dicionario:
                            print(f'{chave.upper()}: {dicionario[chave]}')
                if not encontrou:
                    print('O ID informado não foi encontrado')
            #consulta por setor
            elif (opcao == 3): 
                print('Setores disponiveis: ', end='')
                for dicionario in lista_funcionarios:
                    print(f'{dicionario['setor']} | ', end='')
                print()

                setor_buscado = valida_caracteres('setor')
                encontrou = False
                print()

                for dicionario in lista_funcionarios:
                    if (setor_buscado == dicionario['setor']):
                        encontrou = True
                        for chave in dicionario:
                            print(f'{chave.upper()}: {dicionario[chave]}')
                        print()

                if not encontrou:
                    print('Não encontramos o setor mencionado')
            #retorna ao menu
            elif (opcao == 4): 
                return
            #exceções
            else: 
                print('Opção inválida')
                continue
        except ValueError:
            print('Valor inválido.')

#Boas vindas ao usúario
print('\nSeja bem vindo ao sistema de gerenciamento de funcionarios de Andrey Oliveira\n')

#dados iniciais
lista_funcionarios = []
id_global = 5256701

for i in range(2):
    cadastrar_funcionario(id_global)
    print()

#consultar_funcionarios()