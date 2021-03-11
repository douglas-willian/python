def perguntar():
    return input('O que deseja realizar?\n' +
                 '<I> - Para Inserir um usuario\n' +
                 '<P> - Para Pesquisar um usuario\n' +
                 '<E> - Para Excluir um usuario\n' +
                 '<L> - Para Listar um usuario: ').upper()


def inserir(dicionario):
    login = input('Digite o login: ').upper()
    dicionario[login] = [input('Digite o nome: ').upper(),
                         input(
        'Digite a ultima data de acesso: '),
        input(
        'Qual a ultima estação acessada: ').upper()
    ]
    salvar(dicionario)


def pesquisar(dicionario, login):
    lista = dicionario.get(login)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(dicionario, login):
    usuario = dicionario.get(login.upper())
    if usuario != None:
        del dicionario[login.upper()]
        print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados:", valor)

def salvar(dicionario):
    with open('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ':' + str(valor))

def lerDB(db):
    with open(str(db) + '.txt', 'r') as arquivo:
        for linha in arquivo.readlines():
            print(linha)