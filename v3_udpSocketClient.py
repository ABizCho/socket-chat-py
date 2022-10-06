from socket import *
      
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

while True:
    sendMsg = input("입력하세요: ")
    clientSocket.sendto(sendMsg.encode(), (serverName,serverPort))

    rcvMsg, serverAddress = clientSocket.recvfrom(2048)
    print(rcvMsg.decode())
