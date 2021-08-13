from tkinter import * # 트킨터

root = Tk()
root.title("Taehee GUI") # 타이틀 설정
#root.geometry("640x480") # 크기 설정 가로x세로
root.geometry("640x480+300+100") # 크기 설정 가로x세로 + x좌표 + y좌표(나타내는위치)

root.resizable(False, False) # x너비, y너비 값변경불가 창크기변경불가

root.mainloop()

