import platform
import getpass
from datetime import datetime

# print('Nome maquina..........', platform.node())
# print('arquitetura...........', platform.architecture())
# print('sistema operacional...', platform.system())
# print('versao do SO..........', platform.release())
# print('processador...........', platform.processor())
# print('versao do python......', platform.python_version())

# print('\n',datetime.now())
print(getpass.getuser())
print(getpass.getpass('Digite sua senha: '))