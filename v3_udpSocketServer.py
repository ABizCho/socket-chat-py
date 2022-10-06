from socket import *

serverName='localhost'
serverPort = 12000
serverSocket =socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("This server is ready to receive")

while True:
    
    rcvMsg, clientAddr = serverSocket.recvfrom(2048)
    print('Received >> '+ rcvMsg.decode())
    
    sendMsg = input("입력하세요: ")#
    serverSocket.sendto(sendMsg.encode(), clientAddr)
