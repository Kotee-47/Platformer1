import pygame
from data import functions
from data import classes


ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
CELL_SIZE = 16


def main():
    pygame.init()
    size = width, height = 640, 320
    board = classes.Board(ENVIRONMENT_SPRITES, CELL_SIZE)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 30
    board.set_view(0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)

        screen.fill("black")
        board.render(screen)

        ENVIRONMENT_SPRITES.draw(screen)

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
