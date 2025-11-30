import pygame as pg
import time
import random

pg.init()
pg.font.init()
pg.mixer.init()

FADEOUT_TIME = 2000
VOLUME = 0.8

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
pg.display.set_caption("The Messier Dualis")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
CYAN = (0, 140, 220)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
PURPLE = (191, 64, 191)

Background_original = pg.image.load("Assets/Image Files/Background Image.jpg")
Background = pg.transform.smoothscale(Background_original, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Welcome_Text = "Welcome to The Messier Dualis!"
#Welcome_Text2 = "Ready to dive in?"
button_rect = pg.Rect(0, 0, 200, 50)
button_text = "Dive in!"
font = pg.font.Font("Assets/Nasalization.ttf", 40)
Welcome_Text = font.render("Welcome to The Messier Dualis!", True, PURPLE)
Welcome_Text2 = font.render("Ready to dive in?", True, GREEN)

playlist = [
    "Assets/Audio Files/Music/Interstellar Soundtrack - Dust.mp3",
    "Assets/Audio Files/Music/Astronomical Objects - Paolo Vivaladi.mp3",
]

random.shuffle(playlist)
current_track = 0

MUSIC_END = pg.USEREVENT + 1
pg.mixer.music.set_endevent(MUSIC_END)
Click_Soundeffect = pg.mixer.Sound("Assets/Audio Files/Sound Effects/computer-mouse-click.mp3")
Startup_Sequence_Time = time.time()

def play_track(index):
    pg.mixer.music.load(playlist[index])
    pg.mixer.music.set_volume(VOLUME)
    pg.mixer.music.play(fade_ms=1500)

play_track(current_track)
running = True
#Show_Button_Text_Text = False
#ClickTime = 0

texts = [
    ("Welcome to The Messier Dualis!", PURPLE),
    ("Ready to dive in?", GREEN),
]
Startup_Delay = [2, 4, 6]

while running:
    screen.blit(Background, (0, 0))

    current_time = time.time() - Startup_Sequence_Time
    for i, (text, color) in enumerate(texts):
        if (current_time >= Startup_Delay[i]):
            RenderText = font.render(text, True, color)
            if (i == 0):
                Render_Text_Rect = RenderText.get_rect(center=(SCREEN_WIDTH // 2, 200))
                screen.blit(RenderText, Render_Text_Rect)
            elif (i == 1):
                Render_Text_Rect = RenderText.get_rect(center=(SCREEN_WIDTH // 2, 360))
                screen.blit(RenderText, Render_Text_Rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                #Show_Button_Text_Text = True
                #ClickTime = time.time()
                Click_Soundeffect.play()
                
        if event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            Background = pg.transform.smoothscale(Background_original, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if event.type == MUSIC_END:
            pg.mixer.music.fadeout(FADEOUT_TIME)
            current_track = (current_track + 1) % len(playlist)
            play_track(current_track)

    #Welcome_Text_rect = Welcome_Text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
    #Welcome_Text2_rect = Welcome_Text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))

    if (time.time() - Startup_Sequence_Time >= 6):
        button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

        if button_rect.collidepoint(pg.mouse.get_pos()):
            pg.draw.rect(screen, CYAN, button_rect, border_radius=12)
        else:
            pg.draw.rect(screen, BLUE, button_rect, border_radius=12)

        text_surface = font.render(button_text, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)

        #screen.blit(Welcome_Text, Welcome_Text_rect)
        #screen.blit(Welcome_Text2, Welcome_Text2_rect)
        screen.blit(text_surface, text_rect)

    pg.display.flip()

pg.quit()