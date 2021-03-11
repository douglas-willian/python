import json

base_dados = []
dicionario = {}
index = 1

with open('iris.data', 'r') as dataset:
    for registro in dataset.readlines():
        base_dados.append(registro.split(','))
        dicionario[index] = registro.split(',')
        index += 1

# print(base_dados)
print(base_dados[0][0])

with open('bd.json', 'w') as arquivo_json:
    json.dump(dicionario, arquivo_json)

with open('bd.json', 'r') as arquivo_json:
    dicionario = json.load(arquivo_json)
    for chave, dados in dicionario.items():
        print(chave + ' | ' + str(dados))
