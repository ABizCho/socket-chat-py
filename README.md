# socket-chat-py
파이썬의 소켓을 이용한 간단한 채팅 프로그램

<br><br>

## 1. Version.1 : 클라/서버 소켓 세팅
![socket_set](/img_src/socket_set.png)

<br><br>

## 2. Version.2 : 반복,순차적 채팅 구현
![chat_iter](/img_src/v2_socket_iter.png)

## 3. Version.3 : 
송수신의 순서에 제한받지 않는 동시성 채팅 구현<br><br>

**스레드 활용**: 프로세스 내부에서 병렬 처리를 하기 위해, 프로세스의 소스코드 내부에서 특정 함수만 따로 뽑아내어 분신을 생성하는 것입니다. 원래라면 하나의 절차를 따르며 해야하는 일들도, 스레드를 생성해서 돌릴 경우엔 동시 다발적으로 일을 할 수 있음

