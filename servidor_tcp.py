from socket import *

servidor = 'localhost'
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print('Aguardando cliente...')

while True:
  try:
    con, cliente = obj_socket.accept()
    print('Conectado com: ', cliente)
    # while True:
    msg_recebida = con.recv(1024)
    print('Recebemos: ', msg_recebida)
    msg_enviada = bytearray('Olah cliente', 'utf-8')
    con.send(msg_enviada)
  except:
    print('finalizando')
    con.close()
    break
  con.close()
