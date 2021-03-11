with open('primeiro_arquivo.txt', 'r') as arquivo: # a = append, adiciona dado no arquivo, r = read, w = write, substitui/cria novo arquivo, x = exclusivo, enquanto vc estiver usando ninguem mais pode usar
    # arquivo.write('\nHakuna Matata')
    # conteudo = arquivo.read()
    # print(conteudo)
    for linha in arquivo.readlines():
        print(linha)