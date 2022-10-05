##### 1. 서버 소켓 세팅


from socket import *
#소켓 객체 생성
serverSock = socket(AF_INET, SOCK_STREAM) 

#바인드
## 생성된 소켓 번호와 실제 어드레스 패밀리를 연결하는 작업
port = 8080

serverSock.bind(('', port)) 
    # ip, port 두 바인드 정보, 즉 어드레스 패밀리를 튜플 로 입력해 줬음
    # 빈 문자열은 any 인터페이스 와도 연결 가능한 상태로 설정하는 것
        #즉 8080포트에서 모든 인터페이스에게 연결하도록 설정한 것
        
#리슨
serverSock.listen(1) #해당 소켓이 총 몇개의 동시 접속을 허용할 것인지 
    # 이제부터 소켓은 누군가로부터 접속이 올 때 까지 대기하는 상태가 됨
    
print('%d번 포트로 접속 대기중..'%port)
    
#accept
connectionSock, addr = serverSock.accept() # 소켓에 누군가 접속하여, 연결됐을 때 결과값을 return하는 함수
    # 즉, 누군가가 접속하기 전까지 accept에서 프로그램은 머물러 있는다는 뜻
    # 누군가 접속하여 accpet()가 실행되면, return값으로 새로운 소켓과 상대방의 AF를 전달해주게 됨
    # 이후, 서버에 접속한 상대방과 데이터를 주고받기 위해선, accept()를 통해 생성된 connectionSock이라는 소켓을 이용하여 통신하게 됨 이제 serverSock은 역할을 다함
    
print(str(addr),'에서 접속을 확인했음.')

#
# data = connectionSock.recv(1024)
# print('받은 데이터: ', data.decode('utf-8'))

# connectionSock.send('I am a server.'.encode('utf-8'))
# print('메시지를 보냈음.')

# 반복적 송수신
while True:
    sendData = input('>>>')
    connectionSock.send(sendData.encode('utf-8'))
    
    recvData = connectionSock.recv(1024)
    print('상대방: ', recvData.decode('utf-8'))