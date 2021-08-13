import pygame

pygame.init() #초기화 반드시필요하다

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Taehee Game") #게임이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/Administrator/Desktop/PythonWorkspace/pygame_basic/background.png")

#이벤트루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이아님
    
    screen.blit(background, (0, 0)) # 배경그리기

    pygame.display.update() # 게임화면을 다시 그리기!

    #백그라운드 안만들고 바로 색으로 채우기가능
    #background.fill((0,0,255))

    

#pygame종료
pygame.quie()

