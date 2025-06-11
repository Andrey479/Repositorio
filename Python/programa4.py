'''
Andrey Oliveira Ferreira
10/06/2025

Software de gerenciamento de funcionarios
perguntas:
1) pode usar uma função para validar dados? exemplo: valida_caracteres() // verifica
se o usuario digitou um caractere e não um numeral por exemplo
2) No item III, o que devo fazer se o usuário digitar um valor que não for encontrado?
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
    id_global += 1

#função reponsavel por consultar os dados dos funcionarios
def consultar_funcionarios():
    #Opções disponiveis
    print('-' * 10, 'Consultar funcionarios', '-' * 10)
    print('1 | Consultar todos')
    print('2 | Consultar por ID')
    print('3 | Consultar por setor')
    print('4 | Retornar ao menu')
    print()
    
    #Definindo dessa forma para ficar mais compacto a seção de impressão de resultados
    opcao = 0
    while (opcao < 1 or opcao > 4):
        try:
            opcao = int(input('Escolha uma opção (1, 2, 3, 4): '))
            if (opcao < 1 or opcao > 4):
                print('Digite um valor contido entre 1 e 4')
        except ValueError:
            print('Valor digitado incorreto')

    #seção de ações
    if (opcao == 1): #consulta todos
        for dicionario in lista_funcionarios:
            for chave in dicionario:
                print(f'{chave.upper()}: {dicionario[chave]}')
            print()
    elif (opcao == 2): #consulta por ID
        id_buscado = int(input('Digite o ID do funcionario: '))
        encontrou = False
        for dicionario in lista_funcionarios:
            if (dicionario['id'] == id_buscado):
                print()
                for chave in dicionario:
                    print(f'{chave.upper()}: {dicionario[chave]}')
                encontrou = True
                break
            else:
                encontrou = False
            
        if (encontrou == False):
            print('O ID informado não foi encontrado')
    elif (opcao == 3): #consulta por setor
        print('Escolha 3')
        return 3
    elif (opcao == 4): #retorna ao menu
        print('Escolha 4')
        return 4
    else: #se não for nenhuma opção
        print('Valor digitado incorreto. Tente novamente')
        










#consultar_funcionarios()



#Boas vindas ao usúario
print('Seja bem vindo ao sistema de gerenciamento de funcionarios de Andrey Oliveira')

#dados iniciais
lista_funcionarios = []
id_global = 5256701

for i in range(2):
    cadastrar_funcionario(id_global)

consultar_funcionarios()
#print(lista_funcionarios)













