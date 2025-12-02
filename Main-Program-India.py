#Hieeeeee!!! 👋

import sqlite3 as sql
import pygame as pg
import time
import random
from PIL import Image
import tkinter
import threading as MultiProcessing
import datetime

print("Hallo World!! 👋👋")
time.sleep(2)
print("Taha Husain this side!")
time.sleep(2)
print("This is my Very First Major CS Project and I am soooooo Proud of it!")
time.sleep(2.5)
print("I wanted to combine My Love and Passion for Astronomy with my Upcoming Hobby of Programming.")
time.sleep(3)
print("And honestly, what better way to prove it than making something like this for my CS final project?!")
time.sleep(3)
print("Well anyways, Without any further Ado...")
time.sleep(2)
print("Welcome to 'The Messier Dualis!'")
time.sleep(2)
print("Enjoy! :D")
time.sleep(1)

CurTime = time.time()
current_datetime = datetime.datetime.now()
timestamp_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {timestamp_string}")
time.sleep(1.4)

breathe_scale = 1.0
breathe_direction = 1
breathe_speed = 0.00006
RandomMessierList = []
SerialExplo = 1
randomised = 0
RandomMessierNum2 = 0
Inp = int(input("Do you Want Randomised or Serial-Wise Exploration of the Messier Catalogue? (1 = Random, 2 = Serial-Wise): "))

if (time.time() - CurTime >= 14):
    print("No Input Recieved. Commencing in Randomised Exploration Mode...")
    randomised = 1

if (Inp == 1):
    randomised = 1
    print("Alrighty! Commencing in Randomised Exploration Mode!...")
    time.sleep(1)
    for Taha in range (1, 111):
        RandomMessierNum = random.randint(1, 110)
        RandomMessierList.append(RandomMessierNum)

elif (Inp == 2):
    randomised = 0
    print("Gotcha! Commencing in Serial-Wise Exploration Mode!...")
    time.sleep(1)
    SerialExplo = 1
elif (Inp > 2 or Inp < 1):
    print("You gave an Invalid Input, Commencing program in Serial-Wise Exploration Mode...")
    time.sleep(1)
    randomised = 0

root = tkinter.Tk()
actual_screen_width = root.winfo_screenwidth()
actual_screen_height = root.winfo_screenheight()
root.destroy()

pg.init()
pg.font.init()
pg.mixer.init()

DB = sql.connect("The_Messier_Dualis_Database.db")
Cursor = DB.cursor()

STATE_INTRO = "Intro"
STATE_MAIN = "Main"
CurState = STATE_INTRO
FADEOUT_TIME = 2000
VOLUME = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 680
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
pg.display.set_caption("The Messier Dualis")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
CYAN = (0, 140, 220)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
PURPLE = (191, 64, 191)
ORANGE = (255, 170, 0)

Background_Org = Image.open("Assets/Image Files/Background Image.jpg")

#Welcome_Text = "Welcome to The Messier Dualis!"
#Welcome_Text2 = "Ready to dive in?"
button_rect = pg.Rect(0, 0, 200, 50)
button_text = "Dive in!"
font = pg.font.Font("Assets/Nasalization.ttf", 40)
Welcome_Text = font.render("Welcome to The Messier Dualis!", True, PURPLE)
Welcome_Text2 = font.render("Ready to dive in?", True, GREEN)

Playlist_Choice = random.randint(1, 1000)
if (Playlist_Choice >= 800):
    playlist = [
        "Assets/Audio Files/Music/Billions and Billions - Stellardrone.mp3",
        "Assets/Audio Files/Music/Interstellar Soundtrack - Dust - Hans Zimmer.mp3",
        "Assets/Audio Files/Music/Astronomical Objects - Paolo Vivaladi.mp3",
        "Assets/Audio Files/Music/Meteor Showers - Paolo Vivaladi.mp3"
    ]
elif (Playlist_Choice < 800 and Playlist_Choice > 400):
    playlist = [
        "Assets/Audio Files/Music/Interstellar Soundtrack - Dust - Hans Zimmer.mp3",
        "Assets/Audio Files/Music/Astronomical Objects - Paolo Vivaladi.mp3",
        "Assets/Audio Files/Music/Billions and Billions - Stellardrone.mp3",
        "Assets/Audio Files/Music/Meteor Showers - Paolo Vivaladi.mp3"
    ]
elif (Playlist_Choice <= 400):
    playlist = [
        "Assets/Audio Files/Music/Astronomical Objects - Paolo Vivaladi.mp3",
        "Assets/Audio Files/Music/Interstellar Soundtrack - Dust - Hans Zimmer.mp3",
        "Assets/Audio Files/Music/Billions and Billions - Stellardrone.mp3",
        "Assets/Audio Files/Music/Meteor Showers - Paolo Vivaladi.mp3"
    ]

current_track = 0

MUSIC_END = pg.USEREVENT + 1
pg.mixer.music.set_endevent(MUSIC_END)
Click_Soundeffect = pg.mixer.Sound("Assets/Audio Files/Sound Effects/computer-mouse-click.mp3")
Text_Soundeffect = pg.mixer.Sound("Assets/Audio Files/Sound Effects/text-appear.mp3")
Startup_Sequence_Time = time.time()

def play_track(index):
    pg.mixer.music.load(playlist[index])
    pg.mixer.music.set_volume(VOLUME)
    pg.mixer.music.play(fade_ms=1500)

play_track(current_track)
running = True
#Show_Button_Text_Text = False
#ClickTime = 0
'''
texts = [
    ("Welcome to The Messier Dualis!", PURPLE),
    ("Ready to dive in?", GREEN),
]
Startup_Delay = [2, 4, 6]
'''
while (running == True):
    pg.event.set_grab(True)
    breathe_scale += breathe_direction * breathe_speed
    if (breathe_scale > 1.02 or breathe_scale < 0.98):
        breathe_direction *= -1
    
    if (CurState == STATE_INTRO):
        Background_Org = Background_Org.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.LANCZOS)
        Mode = Background_Org.mode
        Size = Background_Org.size
        Data = Background_Org.tobytes()
        Background = pg.image.fromstring(Data, Size, Mode)
        zoom_width = int(SCREEN_WIDTH * breathe_scale)
        zoom_height = int(SCREEN_HEIGHT * breathe_scale)

        zoomed_image = pg.transform.smoothscale(Background, (zoom_width, zoom_height))

        screen.blit(zoomed_image, ((SCREEN_WIDTH - zoom_width)//2, (SCREEN_HEIGHT - zoom_height)//2))
        #screen.blit(Background, (0, 0))
        current_time = time.time() - Startup_Sequence_Time
        '''
        for i, (text, color) in enumerate(texts):
            if (current_time >= Startup_Delay[i]):
                RenderText = font.render(text, True, color)
                if (i == 0):
                    Render_Button_Rect = RenderText.get_rect(center=(SCREEN_WIDTH // 2, 200))
                    screen.blit(RenderText, Render_Button_Rect)
                elif (i == 1):
                    Render_Button_Rect = RenderText.get_rect(center=(SCREEN_WIDTH // 2, 360))
                    screen.blit(RenderText, Render_Button_Rect)
        '''

        if (time.time() - Startup_Sequence_Time >= 2):
            #Text_Soundeffect.play()
            RenderText = font.render("Welcome to The Messier Dualis!", True, PURPLE)
            #RenderText = RenderText.convert_alpha()
            #RenderText.set_alpha(0)
            Render_Button_Rect = RenderText.get_rect(center=(SCREEN_WIDTH // 2, 200))
            #i = 100
            '''
            while (i < 250):
                time.sleep(0.01)
                i = i + 1
                RenderText.set_alpha(i)
                screen.blit(RenderText, Render_Button_Rect)
            '''
            screen.blit(RenderText, Render_Button_Rect)
        
        if (time.time() - Startup_Sequence_Time >= 4):
            RenderText2 = font.render("Ready to dive in?", True, GREEN)
            Render_Button_Rect2 = RenderText2.get_rect(center=(SCREEN_WIDTH // 2, 360))
            screen.blit(RenderText2, Render_Button_Rect2)

        for event in pg.event.get():
            if (event.type == pg.QUIT):
                running = False

            if (event.type == pg.MOUSEBUTTONDOWN):
                if button_rect.collidepoint(event.pos):
                    #Show_Button_Text_Text = True
                    #ClickTime = time.time()
                    Click_Soundeffect.play()
                    time.sleep(1)
                    CurTime2 = time.time()
                    Next = True
                    CurState = STATE_MAIN
                    
            if (event.type == pg.VIDEORESIZE):
                screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                Background_Org = Background_Org.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.LANCZOS)
                Mode = Background_Org.mode
                Size = Background_Org.size
                Data = Background_Org.tobytes()
                Background = pg.image.fromstring(Data, Size, Mode)

            if (event.type == MUSIC_END):
                pg.mixer.music.fadeout(FADEOUT_TIME)
                current_track = (current_track + 1) % len(playlist)
                play_track(current_track)

            if (event.type == pg.KEYDOWN):
                if event.key == pg.K_ESCAPE:
                    running = False

        #Welcome_Button_Rect = Welcome_Text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
        #Welcome_Text2_rect = Welcome_Text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))

        if (time.time() - Startup_Sequence_Time >= 6):
            button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

            if (button_rect.collidepoint(pg.mouse.get_pos())):
                pg.draw.rect(screen, CYAN, button_rect, border_radius=12)
            else:
                pg.draw.rect(screen, BLUE, button_rect, border_radius=12)

            Button_Text = font.render(button_text, True, BLACK)
            Button_Rect = Button_Text.get_rect(center=button_rect.center)

            #screen.blit(Welcome_Text, Welcome_Button_Rect)
            #screen.blit(Welcome_Text2, Welcome_Text2_rect)
            screen.blit(Button_Text, Button_Rect)

        pg.display.flip()

    if (CurState == STATE_MAIN):
        zoom_width = int(SCREEN_WIDTH * breathe_scale)
        zoom_height = int(SCREEN_HEIGHT * breathe_scale)

        zoomed_image = pg.transform.smoothscale(Background, (zoom_width, zoom_height))
        #screen.blit(Background, (0,0))
        screen.blit(zoomed_image, ((SCREEN_WIDTH - zoom_width)//2, (SCREEN_HEIGHT - zoom_height)//2))
        '''
        z = pg.time.get_ticks() / 2000
        breathe_scale = 1.0 + 0.004 * math.sin(z)
        '''
        if (randomised == 1):
            if (Next == True):
                Choice = RandomMessierList[RandomMessierNum2]

                View_Command = f"SELECT Image_File FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                Fact_Command = f"SELECT Name, Distance, Discovery_Date, Discoverer, Object_Type, Constellation, Apparent_Magnitude, Description FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command2 = f"SELECT Distance FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command3 = f"SELECT Discovery_Date FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command4 = f"SELECT Discoverer FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command5 = f"SELECT Object_Type FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command6 = f"SELECT Constellation FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                #Fact_Command7 = f"SELECT Apparent_Magnitude FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{Choice}';"
                
                Cursor.execute(View_Command)
                Img = Cursor.fetchone()
                Cursor.execute(Fact_Command)
                Facts = Cursor.fetchone()
                #Cursor.execute(Fact_Command2)
                #Fact2 = Cursor.fetchone()
                #Cursor.execute(Fact_Command3)
                #Fact3 = Cursor.fetchone()
                #Cursor.execute(Fact_Command4)
                #Fact4 = Cursor.fetchone()
                #Cursor.execute(Fact_Command5)
                #Fact5 = Cursor.fetchone()
                #Cursor.execute(Fact_Command6)
                #Fact6 = Cursor.fetchone()
                #Cursor.execute(Fact_Command7)
                #Fact7 = Cursor.fetchone()
                ImageDir = Img[0]
                Messier = Image.open(f"Assets/Image Files/{ImageDir}")
                Messier = Messier.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.LANCZOS)
                Mode2 = Messier.mode
                Size2 = Messier.size
                Data2 = Messier.tobytes()
                Background = pg.image.fromstring(Data2, Size2, Mode2)
    
                def FactsWindowTK():
                    FactWindow = tkinter.Tk()
                    FactWindow.title(f"Some Facts about Messier {Choice}")
                    FactWindow.configure(bg='black')
                    FactWindow.geometry(f"{actual_screen_width//2}x{actual_screen_height}+0+0")
                    Name = Facts[0]
                    Dist = Facts[1]
                    DiscoYear = Facts[2]
                    DiscoPer = Facts[3]
                    ObjType = Facts[4]
                    Const = Facts[5]
                    AP_Mag = Facts[6]
                    Desc = Facts[7]
                    FactsText = tkinter.Label(FactWindow, text=f'''
This is Messier {Choice}
It's More Commonly Known Name is {Name}.
It is {Dist} Light Years away from Earth.
It was Discovered in the Year {DiscoYear}AD by {DiscoPer}.
It is a {ObjType}.
From Earth, It's visible in the Constellation of {Const}.
From Earth, It's apparent Magnitude is {AP_Mag}

Here's a Short Brief about Messier {Choice}!:
{Desc}
''', font=("Assets/Nasalization.ttf", 18), wraplength = actual_screen_width//2 - 20, justify = 'center', fg="white", bg="black")
                    FactsText.pack()
                    FactWindow.mainloop()

                MultiProcessing.Thread(target=FactsWindowTK, daemon=True).start()
                Next = False
        elif (randomised == 0):
            if (Next == True):
                if (SerialExplo > 0 and SerialExplo < 111):
                    View_Command = f"SELECT Image_File FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{SerialExplo}';"
                    Cursor.execute(View_Command)
                    Img = Cursor.fetchone()
                    ImageDir = Img[0]
                    Messier = Image.open(f"Assets/Image Files/{ImageDir}")
                    Messier = Messier.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.LANCZOS)
                    Mode2 = Messier.mode
                    Size2 = Messier.size
                    Data2 = Messier.tobytes()
                    Background = pg.image.fromstring(Data2, Size2, Mode2)

                    Fact_Command2 = f"SELECT Name, Distance, Discovery_Date, Discoverer, Object_Type, Constellation, Apparent_Magnitude, Description FROM The_Messier_Objects_Catalogue WHERE Messier_Number = 'M{SerialExplo}';"
                    Cursor.execute(Fact_Command2)
                    Facts = Cursor.fetchone()
                    def FactsWindowTK():
                        FactWindow = tkinter.Tk()
                        FactWindow.configure(bg='black')
                        FactWindow.title(f"Some Facts about Messier {SerialExplo}")
                        FactWindow.geometry(f"{actual_screen_width//2}x{actual_screen_height}+0+0")
                        Name = Facts[0]
                        Dist = Facts[1]
                        DiscoYear = Facts[2]
                        DiscoPer = Facts[3]
                        ObjType = Facts[4]
                        Const = Facts[5]
                        AP_Mag = Facts[6]
                        Desc = Facts[7]
                        FactsText = tkinter.Label(FactWindow, text=f'''
This is Messier {SerialExplo}
It's More Commonly Known Name is {Name}.
It is {Dist} Light Years away from Earth.
It was Discovered in the Year {DiscoYear}AD by {DiscoPer}.
It is a {ObjType}.
From Earth, It's visible in the Constellation of {Const}.
From Earth, It's apparent Magnitude is {AP_Mag}

Here's a Short Brief about Messier {SerialExplo}!:
{Desc}
''', font=("Assets/Nasalization.ttf", 18), wraplength = actual_screen_width//2 - 20, justify = 'center', fg="white", bg="black")
                        FactsText.pack()
                        FactWindow.mainloop()

                    MultiProcessing.Thread(target=FactsWindowTK, daemon=True).start()
                    Next = False
                else:
                    print("The Catalogue has bee Exhausted. Reseting...")
                    time.sleep(0.5)
                    SerialExplo = 1

        if (Next == False):
            Button_Text_Bravo = "Next ->"
            #screen.fill(BLACK)

            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
                
                if (event.type == pg.VIDEORESIZE):
                    screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                    SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                    Cursor.execute(View_Command)
                    Img = Cursor.fetchone()
                    ImageDir = Img[0]
                    Messier = Image.open(f"Assets/Image Files/{ImageDir}")
                    Messier = Messier.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.LANCZOS)
                    Mode2 = Messier.mode
                    Size2 = Messier.size
                    Data2 = Messier.tobytes()
                    Background = pg.image.fromstring(Data2, Size2, Mode2)

                if (event.type == MUSIC_END):
                    pg.mixer.music.fadeout(FADEOUT_TIME)
                    current_track = (current_track + 1) % len(playlist)
                    play_track(current_track)

                if (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_ESCAPE):
                        running = False

                if (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_RIGHT):
                        Next = True
                        SerialExplo = SerialExplo + 1
                        RandomMessierNum2 = RandomMessierNum2 + 1

                if (event.type == pg.KEYDOWN):
                    if (event.key == pg.K_LEFT):
                        Next = True
                        SerialExplo = SerialExplo - 1
                        RandomMessierNum2 = RandomMessierNum2 - 1

                if event.type == pg.ACTIVEEVENT:
                    if event.gain != 1:
                        pg.event.set_grab(True)

            '''
            if (time.time() - CurTime2 >= 4):
                button_rect.center = (SCREEN_WIDTH - 140, SCREEN_HEIGHT - 60)

                if (button_rect.collidepoint(pg.mouse.get_pos())):
                    pg.draw.rect(screen, ORANGE, button_rect, border_radius = 12)
                else:
                    pg.draw.rect(screen, RED, button_rect, border_radius = 12)

                Button_Text2 = font.render(Button_Text_Bravo, True, WHITE)
                Button_Rect2 = Button_Text2.get_rect(center=button_rect.center)
                Button_Text2 = Button_Text2.convert_alpha()
                Button_Text2.set_alpha(160)
                screen.blit(Button_Text2, Button_Rect2)
            '''

            pg.display.flip()

DB.close()
pg.quit()

print("From the bottom of my heart, I truly hope you enjoyed my project and discovered a new spark of curiosity or love for our cosmos through it!")
time.sleep(4)
print("Anyways, By-Bieeeee!! 👋")
time.sleep(1)
exit()
#Bieeee! :D 👋