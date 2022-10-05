##### 2. 클라이언트 소켓 세팅

from socket import *

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM) 
clientSock.connect(('127.0.0.1', port)) # client -> server 접속 위해선 connect() 메서드 사용
    # connect메서드엔 동일하게 어드레스 패밀리(ip-호스트 주소, 포트) 가 튜플로 인자로서 들어간다.
    # 위의 호스트 주소는 localhost ip로 자기 자신을 의미하므로, 클라이언트 자신의 ip를 지정해  8080포트로 들어가라는 명령
    
print("클라이언트 접속 완료")

# clientSock.send("I am a client".encode('utf-8'))
# print("메시지를 전송했음")
# data = clientSock.recv(1024)
# print('받은 데이터: ', data.decode('utf-8'))

while True:
    recvData = clientSock.recv(1024)
    print('상대방:', recvData.decode('utf-8'))
    
    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))
 

