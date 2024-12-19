import pygame
from data import functions
from data import classes

def main():
    pygame.init()
    size = width, height = 736, 480
    board = classes.Board(23, 15)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 30
    board.set_view(0, 0, 32)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)

        screen.fill("black")
        board.render(screen)
        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
