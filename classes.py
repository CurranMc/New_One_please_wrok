###################
import pygame, sys, os
from pygame.locals import *


class Player():
    def __init__(self, player_settings, room_settings, screen): 
        self.down1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.down2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.right1 = pygame.transform.flip(self.left1, True, False)
        self.right2 = pygame.transform.flip(self.left2, True, False)
        self.image = self.down1
        self.rect =  self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen_rect.centerx = room_settings.magnification * (room_settings.room_width/2)
        self.screen_rect.bottom = room_settings.magnification * ((room_settings.room_height/2) + (room_settings.tile_size/2))
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def update(self, player_settings):
        if self.moving_left:
            # self.rect.centerx -= player_settings.p_speed_factor
            self.image = self.left1
        elif self.moving_right:
            # self.rect.centerx += player_settings.p_speed_factor
            self.image = self.right1
        elif self.moving_down:
            # self.rect.bottom += player_settings.p_speed_factor
            self.image = self.down1
        elif self.moving_up:
            # self.rect.bottom -= player_settings.p_speed_factor
            self.image = self.up1
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class RoomSettings():
    def __init__(self):
        self.room_width = 256
        self.room_height = 176
        self.magnification = 1
        self.screen_width = int(self.room_width * self.magnification)
        self.screen_height = int(self.room_height * self.magnification)
        self.tile_size = 16
        self.room_tile_width = int(self.room_width / self.tile_size)
        self.room_tile_height = int(self.room_height / self.tile_size)
        self.bg_color = (0,0,0)
        self.screen_tile = int(self.tile_size * self.magnification)
        self.tile_per_roomx = 16
        self.tile_per_roomy = 11

class PlayerSettings():
    def __init__(self, room_settings):
        self.player_width = 16
        self.player_height = 16
        self.p_speed_factor = room_settings.magnification
        self.p_max_health = 100
        self.p_health = self.p_max_health
        self.p_atk = 5        

class Tiles():
    def __init__(self, room_settings):
        self.t1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2b = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2b.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2l = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2l.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3b = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3b.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3l = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3l.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t6h = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','6h.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t6v = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','6v.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7tr.png')), (room_settings.screen_tile, room_settings.screen_tile))

        self.sky = pygame.image.load(os.path.join('finalProject/models/map', 'sky.png'))
        self.Sky = pygame.Surface(self.sky.get_size(), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
        self.Sky.blit(self.sky, (0,0))
        del self.sky
    def loadtexture(self, file, room_settings):
        bitmap = file
        surface = pygame.Surface((room_settings.screen_tile, room_settings.screen_tile), pygame.HWSURFACE|pygame.SRCALPHA|pygame.DOUBLEBUF)
        surface.blit(bitmap, (0,0))
        return surface

class CameraSettings():
    def __init__(self):
        self.camerax = 0
        self.cameray = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def update(self, deltatime, room_settings):
        if self.moving_left:
            self.camerax += deltatime * 50 * room_settings.magnification
        elif self.moving_right:
            self.camerax -= deltatime * 50 * room_settings.magnification
        elif self.moving_down:
            self.cameray -= deltatime * 50 * room_settings.magnification
        elif self.moving_up:
            self.cameray += deltatime * 50 * room_settings.magnification