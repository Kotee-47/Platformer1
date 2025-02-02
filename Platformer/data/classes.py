import random
import os
from data import functions
import math
import pygame


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, group, grp2, x, y, cell_size=16, additional_group=None):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        if additional_group:
            super().__init__(group, grp2, additional_group)
        else:
            super().__init__(group, grp2)
        self.startrect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        self.mask = pygame.mask.from_surface(self.image)


class Board:
    def __init__(self, envgroup, decgroup, allgroup, dangroup, fingrp, cell_size=16):
        self.cell_size = cell_size
        self.dangroup = dangroup
        self.envgroup = envgroup
        self.decgroup = decgroup
        self.allgroup = allgroup
        file = open('files/levels/yara_test_field.txt', 'rt')
        self.board = file.read().split('p')
        for i in range(0, len(self.board)):
            self.board[i] = self.board[i].split()
        file.close()
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 10
        self.top = 10


    def render(self, screen):
        self.screen = screen
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == '0':
                    pass
                elif self.board[y][x] == 'st':
                    sprite = Environment('images/blocks/special/cave/start.png',
                                         self.decgroup, self.allgroup,
                                         x / 2, y / 2, self.cell_size * 2)
                    self.spawn = x, y
                elif self.board[y][x] == 'en':
                    sprite = Environment('images/blocks/special/cave/end/end1.png',
                                         self.fingroup, self.allgroup,
                                         x / 2, y / 2, self.cell_size * 2)
                elif self.board[y][x] == 'st':
                    sprite = Environment('images/blocks/special_cave/start.png',
                                         self.decgroup, self.allgroup,
                                         x / 2, y / 2, self.cell_size * 2)
                elif self.board[y][x] == 'en':
                    sprite = Environment('images/blocks/special_cave/end/end1.png',
                                         self.fingroup, self.allgroup,
                                         x / 2, y / 2, self.cell_size * 2)
                elif self.board[y][x] == '1':
                    sprite = Environment('images/blocks/environment/1_stone_surface.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '2':
                    sprite = Environment('images/blocks/environment/2_stone.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '3':
                    sprite = Environment('images/blocks/environment/3_stone_corner.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '4':
                    sprite = Environment('images/blocks/decor/4_moss.png',
                                         self.decgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '5':
                    sprite = Environment('images/blocks/environment/5_stone_surface_moss.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '6':
                    sprite = Environment('images/blocks/decor/6_grass.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '7':
                    sprite = Environment('images/blocks/environment/7_stone_surface_grass.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '8':
                    sprite = Environment('images/blocks/environment/8_dead_bush.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '9':
                    sprite = Environment('images/blocks/environment/9_dirt.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '10':
                    sprite = Environment('images/blocks/danger/10_spikes.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '15':
                    sprite = Environment('images/blocks/decor/11_lian_1.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '16':
                    sprite = Environment('images/blocks/decor/12_lian_2.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '13':
                    sprite = Environment('images/blocks/decor/13_lian_3.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '14':
                    sprite = Environment('images/blocks/danger/14_small_spike.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '11':
                    sprite = Environment('images/turret/turret_base.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '12':
                    sprite = Turret('images/turret/turret_cannon.png', self.dangroup, self.allgroup, x, y, self.cell_size)
                    if 'turrets' in objects:
                        objects['turrets'].append(sprite)
                    else:
                        objects['turrets'] = [sprite]

class Player(pygame.sprite.Sprite):
    def __init__(self, group, allgroup, healthgrp, x, y, width, height, cell_size=16):

        self.images = []
        self.images.append(functions.load_image('images/player/sprites/standing.png'))
        self.images.append(functions.load_image('images/player/sprites/jump.png'))
        self.images.append(functions.load_image('images/player/sprites/lie.png'))
        self.images.append(functions.load_image('images/player/sprites/run/running2.png'))
        self.images.append(functions.load_image('images/player/sprites/run/running3.png'))
        self.images.append(functions.load_image('images/player/sprites/run/running1.png'))
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (cell_size * 2, cell_size))

        self.image = self.images[0]

        super().__init__(group, allgroup)
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size * 2, cell_size)
        self.newrect = pygame.Rect(x * cell_size, y * cell_size, 2 * cell_size + 2, cell_size)
        self.mask = pygame.mask.from_surface(self.images[0])
        self.y_speed = 0
        self.x_speed = 0
        self.run_cadres = 0
        self.run_im = 0
        self.left_player = False
        self.left_move = False
        self.right_move = False
        self.on_surf = False
        self.facing_right = True
        self.cell_size = cell_size
        self.healthbar = HealthBar(width, height, healthgrp)
        self.health = 100
        self.move = False
        self.live_frames = 0

    def update(self, env, dang, player, dt):
        self.on_surf = False
        spd1 = (3.125 * self.cell_size) // 1
        if self.live_frames >= 0:
            self.live_frames -= 1

        player.newrect.x = player.rect.x + self.x_speed * dt
        player.newrect.y = player.rect.y + self.y_speed * dt

        trect = player.newrect
        trect.x -= 1
        temp_srf2 = pygame.surface.Surface((trect[2], player.newrect[3] - 6))
        temp_msk2 = pygame.mask.from_surface(temp_srf2)
        tcat2 = TempCat(player.newrect, temp_msk2)
        can_move = True

        if pygame.sprite.spritecollideany(player, env):
            self.on_surf = True

        if not self.on_surf:
            self.image = self.images[1]
        else:
            if self.x_speed == 0:
                self.image = self.images[0]
            else:
                self.run_cadres += 1
                if self.run_cadres > 20:
                    self.run_cadres = 0
                if self.run_cadres == 1:
                    self.run_im += 1
                    if self.run_im > 4:
                        self.run_im = 1
                    if self.run_im == 1:
                        self.image = self.images[4]
                    elif self.run_im == 2:
                        self.image = self.images[3]
                    elif self.run_im == 3:
                        self.image = self.images[4]
                    elif self.run_im == 4:
                        self.image = self.images[5]
                else:
                    if self.run_im == 1:
                        self.image = self.images[4]
                    elif self.run_im == 2:
                        self.image = self.images[3]
                    elif self.run_im == 3:
                        self.image = self.images[4]
                    elif self.run_im == 4:
                        self.image = self.images[5]


        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        for i in env:
            if pygame.sprite.collide_mask(tcat2, i):
                can_move = False
        for i in dang:
            if pygame.sprite.collide_mask(player, i):
                if self.live_frames <= 0:
                    self.health -= 13
                    self.live_frames = 30
                self.y_speed = -500
        if not self.on_surf:
            if self.y_speed < spd1 * 3:
                self.y_speed += spd1 // 10
            else:
                self.y_speed = spd1 * 3
        else:
            if self.y_speed > 0:
                self.y_speed = 0

        if self.x_speed > spd1 * 2:
            self.x_speed = spd1 * 2
        elif self.x_speed < -spd1 * 2:
            self.x_speed = -spd1 * 2

        if self.left_move:
            self.x_speed -= spd1 // 10
        elif self.right_move:
            self.x_speed += spd1 // 10
        elif self.x_speed > spd1 // 10:
            self.x_speed -= spd1 // 20
        elif self.x_speed < -spd1 // 10:
            self.x_speed += spd1 // 20
        else:
            self.x_speed = 0

        if can_move:
            player.rect.x = player.rect.x + self.x_speed * dt
        player.rect.y = player.rect.y + self.y_speed * dt

        self.healthbar.update(self.health)

    def left(self, player):
        self.left_move = True
        self.right_move = False
        self.move = True
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False

    def right(self, player):
        self.left_move = False
        self.right_move = True
        self.move = True
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = True

    def jump(self):
        spd1 = (3.125 * self.cell_size) // 1
        if self.on_surf:
            if self.y_speed != 4 * spd1:
                self.y_speed = -4 * spd1


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.cell_size = cell_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x = obj.rect.x + self.dx - self.cell_size // 2
        obj.rect.y = obj.rect.y + self.dy - self.cell_size // 4

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + self.cell_size // 2 - self.width // 2)
        self.dy = -(target.rect.y + self.cell_size // 2 - self.height // 2)


class TempCat:
    def __init__(self, rect, mask):
        self.rect = rect
        self.mask = mask


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, width, height, healthgrp):
        super().__init__(healthgrp)
        self.rect = pygame.Rect(0, 0, 256, 64)
        self.rect.x = width // 50
        self.rect.y = height // 50

        self.zero = functions.load_image('images/player/health_bar/0_hp.png')
        self.one = functions.load_image('images/player/health_bar/1_hp.png')
        self.two = functions.load_image('images/player/health_bar/2_hp.png')
        self.three = functions.load_image('images/player/health_bar/3_hp.png')
        self.four = functions.load_image('images/player/health_bar/4_hp.png')
        self.five = functions.load_image('images/player/health_bar/5_hp.png')
        self.six = functions.load_image('images/player/health_bar/6_hp.png')
        self.seven = functions.load_image('images/player/health_bar/7_hp.png')
        self.eight = functions.load_image('images/player/health_bar/8_hp.png')

        self.image = self.eight

    def update(self, env, dang, player, dt):
        self.on_surf = False
        spd1 = (3.125 * self.cell_size) // 1
        if self.live_frames >= 0:
            self.live_frames -= 1
        player.newrect.x = player.rect.x + self.x_speed * dt
        player.newrect.y = player.rect.y + self.y_speed * dt
        trect = player.newrect
        trect.x -= 1
        temp_srf2 = pygame.surface.Surface((trect[2], player.newrect[3] - 6))
        temp_msk2 = pygame.mask.from_surface(temp_srf2)
        tcat2 = TempCat(player.newrect, temp_msk2)
        can_move = True
        if pygame.sprite.spritecollideany(player, env):
            self.on_surf = True
        if not self.on_surf:
            self.image = self.images[1]
        else:
            if self.x_speed == 0:
                self.image = self.images[0]
            else:
                self.run_cadres += 1
                if self.run_cadres > 20:
                    self.run_cadres = 0
                if self.run_cadres == 1:
                    self.run_im += 1
                    if self.run_im > 4:
                        self.run_im = 1
                    if self.run_im == 1:
                        self.image = self.images[4]
                    elif self.run_im == 2:
                        self.image = self.images[3]
                    elif self.run_im == 3:
                        self.image = self.images[4]
                    elif self.run_im == 4:
                        self.image = self.images[5]
                else:
                    if self.run_im == 1:
                        self.image = self.images[4]
                    elif self.run_im == 2:
                        self.image = self.images[3]
                    elif self.run_im == 3:
                        self.image = self.images[4]
                    elif self.run_im == 4:
                        self.image = self.images[5]


class Background(pygame.sprite.Sprite):
    def __init__(self, group, background):
        super().__init__(group)
        self.rect = 0, 0
        self.image = functions.load_image(background)


class Turret(pygame.sprite.Sprite):
    cell_size = 16
    def __init__(self, picture, group, allgroup, x, y, cell_size):
        self.original_image = pygame.transform.scale(functions.load_image(picture), (cell_size, cell_size))
        self.image = self.original_image.copy()
        super().__init__(group, allgroup)
        self.x = x * cell_size
        self.y = y * cell_size
        self.rect = pygame.Rect(self.x, self.y, cell_size, cell_size)
        self.mask = pygame.mask.from_surface(self.image)
        self.degrees = 180

    def update(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        z = math.sqrt(dx ** 2 + dy ** 2)
        angle = math.degrees(math.acos(-dx / z) * math.copysign(1, math.asin(dy / z)))

        if angle != self.degrees:
            self.degrees = angle
            self.image = pygame.transform.rotate(self.original_image, self.degrees)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)


class PauseButton:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = 'gray'
        self.hover_color = 'dark gray'

    def draw(self, surface):
        font = pygame.font.SysFont('Segoe UI', 36, True)
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, 'black')
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = 'gray'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return self.action