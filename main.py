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
    fps = 60
    x_speed = 0
    y_speed = 0
    board.set_view(0, 0)
    player = classes.Player('images/player/cat.png', PLAYER, 0, 0, CELL_SIZE)
    left_player = False
    on_surf = False
    right_move = False
    left_move = False

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
                if not left_player:
                    for i in PLAYER:
                        pygame.transform.flip(i.image, True, False)
                        left_player = True
                x_speed -= 100
                left_move = True
            else:
                left_move = False
            if key[pygame.K_RIGHT]:
                if left_player:
                    for i in PLAYER:
                        pygame.transform.flip(i.image, 1, False)
                        left_player = False
                x_speed += 100
                right_move = True
            else:
                right_move = False
            if key[pygame.K_UP]:
                if on_surf:
                    if y_speed != 300:
                        y_speed = -300
                print(dt)

        screen.fill("black")
        board.render(screen)

        ENVIRONMENT_SPRITES.draw(screen)
        PLAYER.draw(screen)

        # сталкивание с полом и падение
        on_surf = False
        for i in ENVIRONMENT_SPRITES:
            if pygame.sprite.collide_mask(i, player):
                on_surf = True
        if not on_surf:
            if y_speed < 200:
                y_speed += 10
            else:
                y_speed = 200
        else:
            if y_speed > 0:
                y_speed = 0

        if x_speed > 100:
            x_speed = 100
        if x_speed < -100:
            x_speed = -100

        player.rect = (player.rect[0] + x_speed * dt, player.rect[1] + y_speed * dt)

        if x_speed > 0 and right_move is False:
            x_speed = 0
        if x_speed < 0 and left_move is False:
            x_speed = 0

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
