from socket import *
import threading #순서무관 동시성 채팅을 위한 스레드 도입
import time #오버클럭 방지를 위함


## 스레드
# 스레드는 본인의 task를 다하면 자동으로 사라짐
# 여기선 지속적 채팅을 구현하므로, 아래의 send와 receive 함수 들에 while True로 반복을 걸어뒀음.
    # 이제 sender와 receiver는 메인 프로세스가 종료되지 않는 한 영원히 실행될 것임
    
def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))
    
port = 8080



serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')


# 하지만 위에서 정의하고 바로 밑에서 호출된 스레드는 분신의 개념으로 메인 프로세스가 종료되면 본인들도 소멸함. 따라서 메인 프로세스도 반복돼야함. 따라서 맨 마지막에 메인 프로세스에 while True를 걸었으며
    # 메인 프로세스의 과도한 반복으로 인한 디바이스 오버클럭 방지를 위해 1초의 타임슬립을 걸어줬음


#스레드 함수에서 핵심 인자는 아래의 target과 args임
    # target: 실제로 스레드가 실행할 함수
    # args: 그 함수에게 전달할 인자
sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
