import pygame
from data import classes


ALL_SPRITES = pygame.sprite.Group()
ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
CELL_SIZE = 64


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load("images/icons/ktetmblu.png"))
    size = width, height = 1080, 720
    board = classes.Board(ENVIRONMENT_SPRITES, DECOR_SPRITES,ALL_SPRITES , CELL_SIZE)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 120
    player = classes.Player('images/player/cat.png', PLAYER, ALL_SPRITES, 3, 8, CELL_SIZE)
    board.render(screen)
    camera = classes.Camera(width, height, CELL_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                player.left(PLAYER)
                player.left_move = True
            else:
                player.left_move = False
            if key[pygame.K_d]:
                player.right(PLAYER)
                player.right_move = True
            else:
                player.right_move = False
            if key[pygame.K_w]:
                player.jump()
            if key[pygame.K_DOWN]:
                print(dt)

        screen.fill("#030303")

        camera.update(player)
        for sprite in ALL_SPRITES:
            camera.apply(sprite)

        ENVIRONMENT_SPRITES.draw(screen)
        PLAYER.draw(screen)

        player.update(ENVIRONMENT_SPRITES, player, dt)

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
