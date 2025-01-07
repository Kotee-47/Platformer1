import pygame
from data import functions


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, group, x, y, cell_size=16):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        super().__init__(group)
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

    def set_view(self, left=10, top=10):
        self.left = left
        self.top = top

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
