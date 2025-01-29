import pygame
from data import functions
from data.Healthbar import HealthBar
from data.TempCat import TempCat


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
        self.x = 3 * 64
        self.y = 8 * 64

    def update(self, env, dang, dt):
        self.on_surf = False
        spd1 = (3.125 * self.cell_size) // 1
        if self.live_frames >= 0:
            self.live_frames -= 1

        self.newrect.x = self.rect.x + self.x_speed * dt
        self.newrect.y = self.rect.y + self.y_speed * dt

        trect = self.newrect
        trect.x -= 1
        temp_srf2 = pygame.surface.Surface((trect[2], self.newrect[3] - 6))
        temp_msk2 = pygame.mask.from_surface(temp_srf2)
        tcat2 = TempCat(self.newrect, temp_msk2)
        can_move = True

        if pygame.sprite.spritecollideany(self, env):
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
            if pygame.sprite.collide_mask(self, i):
                if self.live_frames <= 0:
                    self.health -= 12.5
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
            self.rect.x += self.x_speed * dt
            self.x += self.x_speed * dt
        self.rect.y += self.y_speed * dt
        self.y += self.y_speed * dt
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