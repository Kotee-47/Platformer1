import pygame
from data import functions


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, group, grp2, x, y, cell_size=16):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        super().__init__(group, grp2)
        self.startrect = x * cell_size, y * cell_size
        self.rect = x * cell_size, y * cell_size
        self.mask = pygame.mask.from_surface(self.image)


class Board:
    def __init__(self, envgroup, decgroup, allgroup, cell_size=16):
        self.cell_size = cell_size
        self.envgroup = envgroup
        self.decgroup = decgroup
        self.allgroup = allgroup
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


class Player(pygame.sprite.Sprite):
    def __init__(self, picture, group, allgroup, x, y, cell_size=16):
        # self.image = functions.load_image(picture)
        self.image = pygame.image.load(picture)
        self.image = pygame.transform.scale(self.image, (cell_size * 2, cell_size))
        super().__init__(group, allgroup)
        self.rect = x * cell_size, y * cell_size
        self.mask = pygame.mask.from_surface(self.image)
        self.y_speed = 0
        self.x_speed = 0
        self.left_player = False
        self.left_move = False
        self.right_move = False
        self.on_surf = False
        self.facing_right = True
        self.cell_size = cell_size

    def update(self, env, player, dt):
        self.on_surf = False
        spd1 = (3.125 * self.cell_size) // 1
        for i in env:
            if pygame.sprite.collide_mask(player, i):
                self.on_surf = True
        if not self.on_surf:
            if self.y_speed < spd1:
                self.y_speed += spd1 // 10
            else:
                self.y_speed = spd1 * 2
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

        player.rect = (player.rect[0] + self.x_speed * dt, player.rect[1] + self.y_speed * dt)

    def left(self, player):
        self.left_move = True
        self.right_move = False
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False

    def right(self, player):
        self.left_move = False
        self.right_move = True
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
        obj.rect = (obj.rect[0] + self.dx - self.cell_size // 2, obj.rect[1])
        obj.rect = (obj.rect[0], obj.rect[1] + self.dy - self.cell_size // 4)

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect[0] + self.cell_size // 2 - self.width // 2)
        self.dy = -(target.rect[1] + self.cell_size // 2 - self.height // 2)
