#Sistema de gerenciamento de funcionarios
#permite cadastrar, consultar e remover funcionarios

def cadastrar_funcionario(id):
    global lista_funcionarios
    print(f'ID do funcionario: {id}')
    nome = input('Qual é o nome?: ').upper().strip()
    setor = input('Qual é o setor?: ').upper().strip()
    salario = float(input('Qual é o salário?: '))
    dados = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_funcionarios.append(dados.copy())

def consultar_funcionarios():
    #repete até que o usuario digite 4
    while True:
        print()
        print('-' * 10, 'Consultar funcionarios', '-' * 10)
        print('1 | Consultar todos')
        print('2 | Consultar por ID')
        print('3 | Consultar por setor')
        print('4 | Retornar ao menu')
        print()

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
            id_buscado = int(input('Digite o ID do funcionario: '))
            for dicionario in lista_funcionarios:
                if (dicionario['id'] == id_buscado):
                    print()
                    for chave in dicionario:
                        print(f'{chave.upper()}: {dicionario[chave]}')
        #consulta por setor
        elif (opcao == 3): 
            #pergunta o setor
            setor_buscado = input('Qual é o setor?: ').upper().strip()
            print()
            for dicionario in lista_funcionarios:
                if (setor_buscado == dicionario['setor']):
                    for chave in dicionario:
                        print(f'{chave.upper()}: {dicionario[chave]}')
                    print()            
        elif (opcao == 4): 
            return #retorna ao menu
        else: 
            print('Opção inválida') #exceções
            continue

def remover_funcionario():
    while True:
        id_procurado = int(input('Qual o ID do funcionario que deseja remover?: '))
        encontrou = False #variavel responsavel por continuar ou pausar o progama
        for dicionario in lista_funcionarios:
            if (id_procurado == dicionario['id']):
                lista_funcionarios.remove(dicionario)
                encontrou = True
        if not encontrou:
            print('Id inválido')
            continue
        else:
            break

#dados iniciais
lista_funcionarios = []
id_global = 5256701

#Programa principal
print('\nSeja bem vindo ao sistema de gerenciamento de funcionarios de Andrey Oliveira\n')
while True:
    print('Escolha uma opção')
    print('1 | Cadastrar funcionario')
    print('2 | Consultar funcionario')
    print('3 | Remover funcionario')
    print('4 | Encerra programa')
    
    opcao = int(input('>> '))
    if (opcao == 1):
        cadastrar_funcionario(id_global)
        id_global += 1
        print()
    elif (opcao == 2):
        consultar_funcionarios()
        print()
    elif (opcao == 3):
        remover_funcionario()
        print()
    elif (opcao == 4):
        break
    else:
        print('Opção inválida')
        print()
        continue