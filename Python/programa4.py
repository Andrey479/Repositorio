'''
Andrey Oliveira Ferreira
10/06/2025

Software de gerenciamento de funcionarios
'''
#função que valida o nome do usuario
def valida_nome():
    while True:
        try:
            nome = input('Qual é o nome?: ').upper().strip()
            if not nome:
                print('Digite algo, não mantenha vazio...')
                continue
            elif nome.isalpha():
                return nome
            else:
                print('Numerais e simbolos não são aceitos')
        except:
            print('\nAlgo deu errado')

print(valida_nome())

#Essa função recee os dados do usúario
def cadastrar_funcionario(id):
    global id_global
    global lista_funcionarios
    nome = valida_nome()
    setor = input('Qual é o setor?: ').upper().strip()
    salario = float(input('Qual é o salário?: '))
    dados = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_funcionarios.append(dados.copy())
    id_global += 1

#Boas vindas ao usúario
print('Seja bem vindo ao sistema de gerenciamento de funcionarios de Andrey Oliveira')

#dados iniciais
lista_funcionarios = []
id_global = 5256701



#for i in range(0,2):
 #   cadastrar_funcionario(id_global)

print(lista_funcionarios)













