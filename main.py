import pygame
from data import functions
from data import classes


ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
CELL_SIZE = 32


def main():
    pygame.init()
    size = width, height = 1088, 704
    board = classes.Board(ENVIRONMENT_SPRITES, DECOR_SPRITES, CELL_SIZE)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 120
    player = classes.Player('images/player/cat.png', PLAYER, 0, 0, CELL_SIZE)
    board.render(screen)
    x_cam = 0
    y_cam = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if key[pygame.K_LEFT]:
                player.left(PLAYER)
                player.left_move = True
            else:
                player.left_stop()
            if key[pygame.K_RIGHT]:
                player.right(PLAYER)
                player.left_move = False
            else:
                player.right_stop()
            if key[pygame.K_UP]:
                player.jump()
            if key[pygame.K_DOWN]:
                print(dt)

        screen.fill("#030303")

        ENVIRONMENT_SPRITES.draw(screen)
        PLAYER.draw(screen)

        # сталкивание с полом и падение
        player.update(ENVIRONMENT_SPRITES, player, dt)

        # for i in PLAYER:
        #     x_cam = i.rect[0]
        #     y_cam = i.rect[1]
        # for i in ENVIRONMENT_SPRITES:
        #     i.rect = i.startrect[0] + x_cam, i.startrect[1] + y_cam
        # for i in PLAYER:
        #     i.rect = i.rect[0], i.rect[1]
        # for i in DECOR_SPRITES:
        #     i.rect = i.startrect[0] + x_cam, i.startrect[1] + y_cam

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
