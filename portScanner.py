import socket
from datetime import datetime

ip = input("digite o ip para varrer as portas: ")
t1 = datetime.now() #tempo quando começou a varredura
open_ports = []

def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET = conexao ip, socket.SOCK_STREAM = protocolo TCP
        sock.connect((ip,port)) #socket tenta conectar o ip a uma porta
        sock.settimeout(2) # limite de tempo suportado
        return True
    except:
        return False

for port in range(1,65535):
    result=portscan(port)
    if result:
        print("porta {} OPEN".format(port))
        open_ports.append(port)
    else:
        print("porta {} CLOSED".format(port))


t2 = datetime.now() #tempo quando a varredura acabou
total = t2-t1
print(f"portas abertas: {open_ports}")
print(f"tempo total de varredura: {total}")