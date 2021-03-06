import pygame, random, sys, os, time
from pygame.locals import *
from classes import *
import game_functions as gf
from pygame.sprite import Group
from mapData import *

pygame.init()

clock = pygame.time.Clock()

def setup():
    global room_settings, screen, bg_color, p, player_settings, countSec, countFrame, FPS, fps_font, tiles, camera_settings, deltatime
    room_settings = RoomSettings()
    player_settings = PlayerSettings(room_settings)
    camera_settings = CameraSettings()
    screen = pygame.display.set_mode((room_settings.screen_width, room_settings.screen_height), pygame.HWSURFACE|pygame.SRCALPHA|pygame.DOUBLEBUF)
    pygame.display.set_caption("r/GantMemes")
    bg_color = room_settings.bg_color
    p = Player(player_settings, room_settings, screen)
    countSec = 0
    countFrame = 0
    FPS = 0
    deltatime = 0
    fps_font = pygame.font.Font("C://Windows//Fonts//PrestigeEliteStd-Bd.otf", 20)
    tiles = Tiles(room_settings)

def show_fps():
    fps_overlay = fps_font.render("FPS: "+str(FPS), True, (0, 255, 0, 100))
    screen.blit(fps_overlay, (0,0))

def count_fps():
    global countFrame, countSec, FPS, deltatime
    if countSec == time.strftime("%S"):
        countFrame += 1
    else:
        FPS = countFrame
        countFrame = 0
        countSec = time.strftime("%S")
        if FPS > 0:
            # to set the same speed for all FPS if stable
            deltatime = 1 / FPS

setup()
while True:
    
    # Checks events
    gf.check_events(p, camera_settings) 
    p.update(player_settings)
    camera_settings.update(deltatime, room_settings)
    # gf.slide(mapData, tileData, room_settings, player_settings, p, screen)
    


    gf.update_screen(room_settings, screen, p, tiles, camera_settings)

    show_fps()
    #Reloads the screen
    pygame.display.update()
    count_fps()
    clock.tick(100)