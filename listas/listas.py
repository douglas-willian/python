# Inventario

inventario = []
resposta = 'S'

while resposta == 'S':
    inventario.append(input('Equipamento: '))
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Numero Serial: ')))
    inventario.append(input('Departamento: '))
    print('inventario', inventario)
    resposta = input('Digite \"S\" para continuar: ').upper()

for elemento in inventario:
    print('item inventario', elemento)
