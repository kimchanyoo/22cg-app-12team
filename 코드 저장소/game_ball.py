from xml.etree.ElementInclude import default_loader
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
    canvas.create_rectangle(x1 - 10, y1 - 10, x1 + 100,
                            y1 + 100, fill=color[1])


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
    canvas.create_polygon(x1, y1, x1, y1 + 140, x1 +
                          140, y1 + 60, fill=color[1])


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
    pyautogui.screenshot(
    'C:\\Users\\cksdb\\OneDrive\\바탕 화면\\screenshot1.png', region=(53, 153, 674, 566))

# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def open():
    global im, tk_img
    fname = fd.askopenfilenames()
    im = Image.open(fname)
    tk_img = Image.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()


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
canvas = Canvas(window, width=700, height=600, bg="white")
canvas.create_text(350, 80, text="그려서 게임으로!", fill="black", font=("둥근모꼴", 35))
canvas.create_text(193, 350, text="< 조작키 >", fill="red", font=("둥근모꼴", 12))
canvas.create_text(350, 430, text="마우스를 이용하여 여러 기능을 활용해 보세요!\n 초기 설정된 색은 흰 색 입니다",
                   fill="darkblue", font=("둥근모꼴", 12))
canvas.create_text(350, 500, text="== ALL CLEAR를 눌러 시작하세요! ==",
                   fill="black", font=("둥근모꼴", 14))

canvas.create_text(410, 150, text="==<실행설명>==", fill="red", font=("둥근모꼴", 15))
canvas.create_text(420, 250, text="우클릭 = 기본색상선택\n\n휠 클릭 = 그 외 색상선택\n\n좌클릭 = 지우개\n\n좌더블클릭 = 도형 삽입", fill="black",
                   font=("둥근모꼴", 16))

canvas.create_rectangle(130, 160, 250, 330, outline="black")
canvas.create_line(130, 220, 250, 220, fill="black")
canvas.create_rectangle(130, 160, 190, 220, fill="gray22", outline="black")
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

clear = Button(frame, text="==ALL CLEAR==", fg="darkblue",
               command=clearCanvas, font=("둥근모꼴", 20))
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
button6 = Button(window, text="  ", bg="lawngreen",
                 command=change_colorLawngreen)
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
button12 = Button(window, text="  ", bg="darkblue",
                  command=change_colorDarkblue)
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


window.config(menu=menubar)
window.mainloop()

root = Tk()
root.geometry("200x100")
root.title('장애물을 바꿔봐요!')


def open():
    global my_image  # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    global address
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
        ('jpg files', '*.jpg'), ('png files', '*.png'), ('all files', '*.*')))
    address = root.filename
    Label(root, text=root.filename).pack()  # 파일경로 view
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_image).pack()  # 사진 view


my_btn = Button(root, text='파일열기', command=open).pack()

root.mainloop()

window.mainloop()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
pos_x = 500
pos_y = 524
game_result = False
BLACK = (0, 0, 0)
score = 0
e = 0
running = True

pg.init()
pg.display.set_caption("피하기 게임")
sysfont = pg.font.SysFont(None, 72)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
sound = pg.mixer.Sound(
    "E:\\2022-1\\computer grapics\\game\\let-the-games-begin-21858.mp3")
sound.play(-1)

obj = pg.image.load(
    address)  # 이미지 불러오기
character = pg.image.load(
    "C:\\Users\\cksdb\\OneDrive\\바탕 화면\\KakaoTalk_20220524_032357479.jpg")
background = pg.image.load(
    "E:\\2022-1\\computer grapics\\\game\\background.jpg")
obj = pg.transform.scale(obj, (50, 50))
character = pg.transform.scale(character, (50, 50))
objdrop = []
start_time = pg.time.get_ticks()


class object:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = -3

    def show(self):
        screen.blit(obj, (self.x, self.y))

    def move(self):
        self.y += 5


while running:
    if game_result == True:
        break
    clock.tick(60)
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()

    if random.random() > 0.8:
        objdrop.append(object())

    screen.blit(background, (0, 0))
    screen.blit(character, (pos_x, pos_y))
    for objsdrops in objdrop:
        objsdrops.move()
        objsdrops.show()

    key_event = pg.key.get_pressed()  # 키 이벤트 주인공이 x 좌표값으로 7씩 움직이게 함
    if key_event[pg.K_LEFT]:
        if pos_x > 0:  # 왼쪽 벽을 못 넘어가는 좌표제한 설정
            pos_x -= 7
            character

    if key_event[pg.K_RIGHT]:
        if 950 > pos_x:
            pos_x += 7
            character

    elapsed_time = (pg.time.get_ticks() - start_time) / 1000

    for e in objdrop:
        if pos_x - 50 < e.x < pos_x + 50:
            if pos_y - 43 < e.y + 10 < pos_y + 10:
                game_result = True
                msg = sysfont.render("Your Score is {}".format(
                    int(elapsed_time)), True, BLACK)
                msg_rect = msg.get_rect(
                    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                screen.blit(msg, msg_rect)
                game_result = True

    message = sysfont.render("Score is {}".format(
        int(elapsed_time)), True, BLACK)
    # 카운트당 스코어가 오르게하고 화면에 스코어 메세지를 출력하게 함
    message_rect = message.get_rect()
    message_rect.center = (200, 50)
    screen.blit(message, message_rect)

    pg.display.update()

pg.time.delay(2000)
pg.quit()
