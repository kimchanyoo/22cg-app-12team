import pygame as pg
import sys
import random
import keyboard
from pygame.locals import*

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
pos_x = 500
pos_y = 524
game_result = False
BLACK = (0,0,0)
score = 0
e = 0
running = True

pg.init()
pg.display.set_caption("피하기 게임")
sysfont = pg.font.SysFont(None,72)
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
obj = pg.image.load(
    "E:\\2022-1\\computer grapics\\\game\\obj.jpg")  # 이미지 불러오기
character = pg.image.load("C:\\Users\\cksdb\\OneDrive\\바탕 화면\\석화닝.png")
background = pg.image.load(
    "E:\\2022-1\\computer grapics\\\game\\background.jpg")
obj = pg.transform.scale(obj,(50,50))
character = pg.transform.scale(character,(50,50))
objdrop = []
start_time = pg.time.get_ticks()
class object:
        def __init__(self):
            self.x = random.randint(0,1000)
            self.y = -3
        def show(self):
            screen.blit(obj, (self.x,self.y))
        def move(self):
            self.y +=5

while running:
    if game_result == True:
        break
    clock.tick(60)
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
            

    if random.random()> 0.8:
        objdrop.append(object())
        
    screen.blit(background,(0,0))
    screen.blit(character,(pos_x,pos_y))
    for objsdrops in objdrop:
        objsdrops.move()
        objsdrops.show()
    
    key_event = pg.key.get_pressed()  # 키 이벤트 주인공이 x 좌표값으로 7씩 움직이게 함
    if key_event[pg.K_LEFT]:
        if pos_x > 0:         # 왼쪽 벽을 못 넘어가는 좌표제한 설정
            pos_x -= 7
            character

    if key_event[pg.K_RIGHT]:
        if 950 > pos_x:
            pos_x += 7
            character
    
    elapsed_time = (pg.time.get_ticks()-start_time)/1000
    
    for e in objdrop:
        if pos_x - 50 < e.x < pos_x + 50:
            if pos_y - 43 < e.y+10 < pos_y + 10:
                game_result = True
                msg = sysfont.render("Your Score is {}".format(int(elapsed_time)),True,BLACK)
                msg_rect = msg.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
                screen.blit(msg, msg_rect)
                game_result =True
                
    message = sysfont.render("Score is {}".format(int(elapsed_time)), True, BLACK)
    # 카운트당 스코어가 오르게하고 화면에 스코어 메세지를 출력하게 함
    message_rect = message.get_rect()
    message_rect.center=(200,50)
    screen.blit(message, message_rect) 
 
    pg.display.update()

pg.time.delay(2000)
pg.quit()