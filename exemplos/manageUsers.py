from funcoes import *

usuarios = {
    'asd': 1,
    'DOUG': ['DOUGLAS', '12/12/12', 'PRINT'], 
    'DOUG_RX': ['WILL', '11/11/11', 'PRINT']
}

opcao = perguntar()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)

        opcao = perguntar()

    if opcao == 'P':
        usuario = input('Digite o login do usuario: ')
        print(pesquisar(usuarios, usuario))

        opcao = perguntar()

    if opcao == 'E':
        usuario = input('Digite o login do usuario para excluir: ')
        excluir(usuarios, usuario)

        opcao = perguntar()

    if opcao == 'L':
        listar(usuarios)

        opcao = perguntar()
