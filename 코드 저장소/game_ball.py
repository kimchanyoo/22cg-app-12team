import tkinter
import pygame as pg
import sys
import random
import os
import time
import keyboard
import pyautogui
from pygame.locals import *
from tkinter import *
from turtle import width
from PIL import Image, ImageTk, ImageFilter, ImageGrab
import tkinter as tk
from tkinter import filedialog
from tkinter import filedialog as fd
from tkinter.colorchooser import *
from tkinter.filedialog import *

from django.contrib.sessions.backends import file

im = None
tk_img = None
window = None
canvas = None
x1, y1 = None, None


# 사용자에게 색상을 입력받는 함수
def colorASK():
    global color
    color = askcolor()


# 굴기 지정 함수
def penWidth1():
    global mywidth
    mywidth = 1


def penWidth5():
    global mywidth
    mywidth = 5


def penWidth10():
    global mywidth
    mywidth = 10


def penWidth20():
    global mywidth
    mywidth = 20


def penWidth30():
    global mywidth
    mywidth = 30


def penWidth50():
    global mywidth
    mywidth = 50


mycolor = "white"
mywidth = 5


# 그리기 함수
def paint(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1, y1, x1 + 1, y1 + 1, width=mywidth, fill=mycolor)


# 사각형 그리기 함수
def paint3(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_rectangle(x1 - 10, y1 - 10, x1 + 100, y1 + 100, fill=color[1])


# 원 그리기 함수
def paint4(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_oval(x1 - 10, y1 - 10, x1 + 100, y1 + 100, fill=color[1])


# 삼각형 그리기 함수
def paint5(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_polygon(x1, y1, x1, y1 + 140, x1 + 140, y1 + 60, fill=color[1])


def rectangle():
    global color
    color = askcolor()
    canvas.bind("<Double-Button-1>", paint3)


def oval():
    global color
    color = askcolor()
    canvas.bind("<Double-Button-1>", paint4)


def triangle():
    global color
    color = askcolor()
    canvas.bind("<Double-Button-1>", paint5)


# 지우기 함수
def eraser(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1, y1, x1 + 1, y1 + 1, width=mywidth, fill="black")


# 색 변형 함수
def change_colorRed():
    global mycolor
    mycolor = "red"


def change_colorYellow():
    global mycolor
    mycolor = "yellow"


def change_colorBlue():
    global mycolor
    mycolor = "blue"


def change_colorGray80():
    global mycolor
    mycolor = "Gray80"


def change_colorGray60():
    global mycolor
    mycolor = "Gray60"


def change_colorGray30():
    global mycolor
    mycolor = "Gray30"


def change_colorGray10():
    global mycolor
    mycolor = "Gray10"


def change_colorGreen():
    global mycolor
    mycolor = "green"


def change_colorBrown():
    global mycolor
    mycolor = "Brown"


def change_colorPink():
    global mycolor
    mycolor = "pink"


def change_colorOrange():
    global mycolor
    mycolor = "orange"


def change_colorPurple():
    global mycolor
    mycolor = "purple"


def change_colorLawngreen():
    global mycolor
    mycolor = "lawngreen"


def change_colorWhite():
    global mycolor
    mycolor = "white"


def change_colorSkyblue():
    global mycolor
    mycolor = "skyblue"


def change_colorDarkblue():
    global mycolor
    mycolor = "darkblue"


def paint2(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1, y1, x1 + 1, y1 + 1, width + mywidth, fill=color[1])


# 화면을 다 지우는 함수
def clearCanvas():
    canvas.delete("all")


# 파일 메뉴에서 "저장"을 선택했을 때 호출되는 함수
def Save():
    im3 = pyautogui.screenshot('C:\\Users\\cksdb\\OneDrive\\바탕 화면\\my_region.png', region=(144, 230 ,810, 810))


# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def open(text_box=None):
    global im, tk_img
    fname = fd.askopenfilenames()
    im = Image.open(fname)
    tk_img = Image.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()
    read = file.read()
    text_box.insert(tk.END, read)


# 파일 메뉴에서 "종료"를 선택하였을 때 호출되는 함수
def quit():
    window.quit()
    window.destroy()


# 영상처리 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def image_blur():
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = Image.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update()


# 윈도우를 생성한다
window = Tk()
window.title("그려서 게임으로!")
canvas = Canvas(window, width=700, height=600, bg="black")
canvas.create_text(350, 80, text="그려서 게임으로!", fill="white", font=("둥근모꼴", 35))
canvas.create_text(193, 350, text="< 조작키 >", fill="red", font=("둥근모꼴", 12))
canvas.create_text(350, 430, text="마우스를 이용하여 여러 기능을 활용해 보세요!\n 초기 설정된 색은 흰 색 입니다", fill="yellow", font=("둥근모꼴", 12))
canvas.create_text(350, 500, text="== ALL CLEAR를 눌러 시작하세요! ==", fill="white", font=("둥근모꼴", 14))

canvas.create_text(410, 150, text="==<실행설명>==", fill="red", font=("둥근모꼴", 15))
canvas.create_text(420, 250, text="우클릭 = 기본색상선택\n\n휠 클릭 = 그 외 색상선택\n\n좌클릭 = 지우개\n\n우더블클릭 = 도형 삽입", fill="white",
                   font=("둥근모꼴", 16))

canvas.create_rectangle(130, 160, 250, 330, outline="white")
canvas.create_line(130, 220, 250, 220, fill="white")
canvas.create_rectangle(130, 160, 190, 220, fill="gray22", outline="white")
canvas.grid()

frame = Frame(window)
frame.grid()

# 메뉴를 생성한다
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
rotatemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)

menubar.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기(O)", command=open)
filemenu.add_command(label="저장(S)", command=Save)
filemenu.add_command(label="다른 이름으로 저장(A)", command=Save)
filemenu.add_command(label="끝내기(X)", command=quit)


# 우클릭시 함수가 호출됨
canvas.bind("<B1-Motion>", paint)
# 마우스휠 클릭시 함수가 호출됨
canvas.bind("<B2-Motion>", paint2)
# 좌클릭시 함수가 호출됨
canvas.bind("<B3-Motion>", eraser)

clear = Button(frame, text="==ALL CLEAR==", fg="darkblue", command=clearCanvas, font=("둥근모꼴", 20))
clear.grid(row=1, column=2)
l2 = Label(window, text="색상 선택: ")
l2.place(x=705, y=70)

# 화면에 위젯을 위치하게하는 코드
button1 = Button(window, text="  ", bg="red", command=change_colorRed)
button1.place(x=705, y=90)
button2 = Button(window, text="  ", bg="orange", command=change_colorOrange)
button2.place(x=730, y=90)
button3 = Button(window, text="  ", bg="yellow", command=change_colorYellow)
button3.place(x=755, y=90)
button3 = Button(window, text="  ", bg="gray80", command=change_colorGray80)
button3.place(x=780, y=90)
button4 = Button(window, text="  ", bg="skyblue", command=change_colorSkyblue)
button4.place(x=705, y=115)
button5 = Button(window, text="  ", bg="pink", command=change_colorPink)
button5.place(x=730, y=115)
button6 = Button(window, text="  ", bg="lawngreen", command=change_colorLawngreen)
button6.place(x=755, y=115)
button3 = Button(window, text="  ", bg="gray60", command=change_colorGray60)
button3.place(x=780, y=115)
button7 = Button(window, text="  ", bg="purple", command=change_colorPurple)
button7.place(x=705, y=140)
button8 = Button(window, text="  ", bg="white", command=change_colorWhite)
button8.place(x=730, y=140)
button9 = Button(window, text="  ", bg="green", command=change_colorGreen)
button9.place(x=755, y=140)
button3 = Button(window, text="  ", bg="gray30", command=change_colorGray30)
button3.place(x=780, y=140)
button10 = Button(window, text="  ", bg="brown", command=change_colorBrown)
button10.place(x=705, y=165)
button11 = Button(window, text="  ", bg="blue", command=change_colorBlue)
button11.place(x=730, y=165)
button12 = Button(window, text="  ", bg="darkblue", command=change_colorDarkblue)
button12.place(x=755, y=165)
button3 = Button(window, text="  ", bg="gray10", command=change_colorGray10)
button3.place(x=780, y=165)
user = Button(window, text="그 외 색상선택", fg="black", command=colorASK)
user.place(x=705, y=190)

l2 = Label(window, text="도형 찍기: ")
l2.place(x=705, y=270)
button = Button(window, text=" 사각형 ", fg="black", command=rectangle)
button.grid(row=0, column=1)
button = Button(window, text=" 원 형 ", fg="black", command=oval)
button.grid(row=0, column=2)
button = Button(window, text=" 삼각형 ", fg="black", command=triangle)
button.place(x=705, y=320)

l1 = Label(window, text="선 굵기: ")
l1.place(x=705, y=380)
button = Button(window, text=" 굵기 1 ", fg="black", command=penWidth1)
button.place(x=705, y=400)
button = Button(window, text=" 굵기 5 ", fg="black", command=penWidth5)
button.place(x=760, y=400)
button = Button(window, text=" 굵기 10 ", fg="black", command=penWidth10)
button.place(x=705, y=430)
button = Button(window, text=" 굵기 20 ", fg="black", command=penWidth20)
button.place(x=760, y=430)
button = Button(window, text=" 굵기 30 ", fg="black", command=penWidth30)
button.place(x=705, y=460)
button = Button(window, text=" 굵기 50 ", fg="black", command=penWidth50)
button.place(x=760, y=460)


now = time.localtime()
time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
img=ImageGrab.grab()
saveas="{}{}".format(time,'.png')
img.save(saveas)


window.config(menu=menubar)
window.mainloop()

# 불러오기
# 불러오기를 위해 tkinter로 root를 설정
root = Tk()
# root의 위치를 지정
root.geometry("200x100")
# root의 제목 지정
root.title('장애물을 바꿔봐요!')


def open():
    # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    global my_image
    # 불러온 파일의 주소를 기억하도록 전역변수 선언  
    global address
    # root의 파일이름을 가지옴
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
        ('jpg files', '*.jpg'), ('png files', '*.png'), ('all files', '*.*')))
    address = root.filename
    # 파일경로 view
    Label(root, text=root.filename).pack()  
    # 파일경로에 있는 이미지를 가져옴
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    # 사진 view
    Label(image=my_image).pack()  

# 파일열기 버튼을 누르면 open함수를 실행시키게 함
my_btn = Button(root, text='파일열기', command=open).pack()
# 여러 모듈에서 위젯 생성하고, 트리거 설정하고 한 뒤 실행흐름 마지막에 사용자(유저)의 입력을 
# '계속 기다리게 하는 목적'
root.mainloop()

# 게임 실행
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
pos_x = 500
pos_y = 524
game_result = False
BLACK = (0, 0, 0)
score = 0
e = 0
running = True
# pygame 시작
pg.init()
# 게임 제목 설정
pg.display.set_caption("피하기 게임")
# Font객체 생성
sysfont = pg.font.SysFont(None, 72)
# 화면생성
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# FPS 초당 프레임 변수 설정
clock = pg.time.Clock()
# 사운드 파일 불러오기
sound = pg.mixer.Sound(
    "E:\\2022-1\\computer grapics\\game\\let-the-games-begin-21858.mp3")
# 사운드 무한반복 시키기
sound.play(-1)
# 불러오기에서 가져온 주소에서 이미지 불러오기
obj = pg.image.load(
    address)  
# 이미지 불러오기
character = pg.image.load(
    "E:\\2022-1\\computer grapics\\game\\charater.jpg")
background = pg.image.load(
    "C:\\Users\\cksdb\\OneDrive\\바탕 화면\\배경.jpg")
# 배경, 떨어지는 물체, 유저가 움직일 캐릭터 크기 강제 제한
obj = pg.transform.scale(obj, (50, 50))
character = pg.transform.scale(character, (50, 50))
background = pg.transform.scale(background,(1000,600))
# 떨어지는 물체를 저장하는 배열
objdrop = []
# pygame.init()이 호출된 이후 경과된 밀리초를 반환
start_time = pg.time.get_ticks()

# 떨어지는 물체 클래스 선언
class object:
    def __init__(self):
        # 떨어지는 물체의 위치 지정
        self.x = random.randint(0, 1000)
        self.y = -3

    def show(self):
        screen.blit(obj, (self.x, self.y))

    def move(self):
        self.y += 5

# 게임이 끝나기 전까지 무한 반복
while running:
    # FPS를 60으로 지정
    clock.tick(60)
    # 대기열에서 이벤트를 얻게 만듬
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
    # random값이 0.8이 넘을때마다 떨어지는 물체를 생성하여 objdrop 배열에 추가시킨다
    if random.random() > 0.8:
        objdrop.append(object())
    # 배경화면을 (0,0)지점에 작성 
    screen.blit(background, (0, 0))
    # 캐릭터를 지정해놓은 장소에 작성
    screen.blit(character, (pos_x, pos_y))
    # objdrop에 들어가있는 것들을 움직이고 화면에 표현되게 만듬
    for objsdrops in objdrop:
        objsdrops.move()
        objsdrops.show()
    # 키 이벤트 주인공이 x 좌표값으로 7씩 움직이게 함
    key_event = pg.key.get_pressed()
    # 왼쪽 키가 눌려진다면   
    if key_event[pg.K_LEFT]:
         # 왼쪽 벽을 못 넘어가는 좌표제한 설정
        if pos_x > 0: 
            # 왼쪽이 눌려질때 캐릭터가 -7씩 이동 
            pos_x -= 7
            character
    # 오른쪽 키가 눌려진다면
    if key_event[pg.K_RIGHT]:
        # 오른쪽 벽을 못 넘어가는 좌표제한
        if 950 > pos_x:
            # 오른쪽이 눌려질때 캐릭터가 +7씩 이동
            pos_x += 7
            character
    # 게임의 스코어를 진행된 시간으로 수행하기위해 게임에서 진행된 밀리초에서
    # 게임 반복문이 시작되기 전까지의 밀리초를 빼주고 1000을 나눠줌
    elapsed_time = (pg.time.get_ticks() - start_time) / 1000
    # objdrop배열에서 1개라도 캐릭터와 충돌하는지 확인
    for e in objdrop:
        if pos_x - 50 < e.x < pos_x + 50:
            if pos_y - 43 < e.y + 10 < pos_y + 10:
                # 게임 종료시 현재까지 진행시간을 화면에 출력하게 함
                msg = sysfont.render("Your Score is {}".format(
                    int(elapsed_time)), True, BLACK)
                msg_rect = msg.get_rect(
                    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                screen.blit(msg, msg_rect)
                # 게임 종료
                running = False
    # 게임 시작이후 진행 시간동안 스코어가 오르게하고 화면에 스코어 메세지를 출력하게 함
    message = sysfont.render("Score is {}".format(
        int(elapsed_time)), True, BLACK)
    message_rect = message.get_rect()
    message_rect.center = (200, 50)
    screen.blit(message, message_rect)
    # 게임 화면을 업데이트 시켜준다
    pg.display.update()
# 게임에 딜레이를 2000밀리초(2초)만큼 할당한다
pg.time.delay(2000)
# pygame을 종료시킨다
pg.quit()
