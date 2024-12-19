import pygame
from data import functions


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left=10, top=10, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.screen = screen
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, pygame.Color('dark green'), (
                                 x * self.cell_size + self.left,
                                 y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size),
                                 self.board[y][x])


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
        x, y = cell
        self.board[y][x] = int(not self.board[y][x])
        self.render(self.screen)
