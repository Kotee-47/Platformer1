import pygame
from data import functions


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, group, x, y, cell_size=16):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        super().__init__(group)
        self.startrect = x * cell_size, y * cell_size
        self.rect = x * cell_size, y * cell_size
        self.mask = pygame.mask.from_surface(self.image)


class Board:
    def __init__(self, envgroup, decgroup, cell_size=16):
        self.cell_size = cell_size
        self.envgroup = envgroup
        self.decgroup = decgroup
        file = open('files/levels/test_field.txt', 'rt')
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
                elif self.board[y][x] == '1':
                    sprite = Environment('images/blocks/environment/1_stone_surface.png', self.envgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '2':
                    sprite = Environment('images/blocks/environment/2_stone.png', self.envgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '3':
                    sprite = Environment('images/blocks/environment/3_stone_corner.png', self.envgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '4':
                    sprite = Environment('images/blocks/decor/4_moss.png', self.decgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '5':
                    sprite = Environment('images/blocks/environment/5_stone_surface_moss.png', self.envgroup,
                                         x, y, self.cell_size)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if self.width >= x + 1 > 0 and self.height >= y + 1 > 0:
            return x, y

    def on_click(self, cell):
        print("Была выбрана ячейка " + str(cell))
        self.render(self.screen)


class Player(pygame.sprite.Sprite):
    def __init__(self, picture, group, x, y, cell_size=16):
        # self.image = functions.load_image(picture)
        self.image = pygame.image.load(picture)
        self.image = pygame.transform.scale(self.image, (cell_size * 2, cell_size))
        super().__init__(group)
        self.rect = x * cell_size, y * cell_size
        self.mask = pygame.mask.from_surface(self.image)
        self.y_speed = 0
        self.x_speed = 0
        self.left_player = False
        self.left_move = False
        self.on_surf = False

    def update(self, env, player, dt):
        self.on_surf = False
        for i in env:
            if pygame.sprite.collide_mask(player, i):
                self.on_surf = True
        if not self.on_surf:
            if self.y_speed < 200:
                self.y_speed += 10
            else:
                self.y_speed = 200
        else:
            if self.y_speed > 0:
                self.y_speed = 0

        if self.x_speed > 100:
            self.x_speed = 100
        if self.x_speed < -100:
            self.x_speed = -100

        player.rect = (player.rect[0] + self.x_speed * dt, player.rect[1] + self.y_speed * dt)

    def left(self, player):
        if not self.left_player:
            for i in player:
                pygame.transform.flip(i.image, True, False)
                self.left_player = True
        self.x_speed = -150
        self.left_move = True

    def right(self, player):
        if self.left_player:
            for i in player:
                pygame.transform.flip(i.image, True, False)
                self.left_player = False
        self.x_speed = 150
        self.left_move = False

    def jump(self):
        if self.on_surf:
            if self.y_speed != 400:
                self.y_speed = -400

    def left_stop(self):
        if self.x_speed < 0:
            self.x_speed = 0

    def right_stop(self):
        if self.x_speed > 0:
            self.x_speed = 0
