nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))

if idade >= 65:
  print('O paciente ' + nome + ' POSSUI atendimento prioritário!')
else:
  print('O paciente ' + nome + ' NÃO possui atendimento prioritário!')