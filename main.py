import pygame
from data import classes
from data import functions


ALL_SPRITES = pygame.sprite.Group()
ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
DANGER_SPRITES = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
HEALTH = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()
PAUSE = pygame.sprite.Group()
FINISH = pygame.sprite.Group()
FINISH_SCREEN = pygame.sprite.Group()
CELL_SIZE = 64


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load("images/icons/ktetmeliv.png"))
    size = width, height = 1080, 720
    board = classes.Board(ENVIRONMENT_SPRITES, DECOR_SPRITES, ALL_SPRITES, DANGER_SPRITES, FINISH, CELL_SIZE)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ketdventure")
    running = True
    dt = 0
    fps = 120
    player = classes.Player(PLAYER, ALL_SPRITES, HEALTH, 3, 8,
                            width, height, CELL_SIZE)
    board.render(screen)
    camera = classes.Camera(width, height, CELL_SIZE)
    classes.Background(BACKGROUND, 'images/backgrounds/' + board.background)
    classes.Background(FINISH_SCREEN, 'images/backgrounds/finished.png')
    classes.Background(PAUSE, 'images/pause/backgrnd_pause.png')
    pause = False
    finish_c = 0
    finished = False
    pause_buttons = [
        classes.PauseButton(1080 // 2 - 200, 270, 400, 100, "Продолжить игру", 'continue'),
        classes.PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]
    win_buttons = [
        classes.PauseButton(1080 // 2 - 200, 270, 400, 100, "Следующий уровень", None),
        classes.PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]

    while running:
        if not finished:
            if not pause:
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
                    if key[pygame.K_ESCAPE]:
                        pause = True

                # screen.fill("#030303")

                camera.update(player)
                for sprite in ALL_SPRITES:
                    camera.apply(sprite)

                for i in PLAYER:
                    if pygame.sprite.spritecollideany(i, FINISH):
                        finish_c += 1
                        if finish_c > 50:
                            finished = True

                BACKGROUND.draw(screen)
                DANGER_SPRITES.draw(screen)
                FINISH.draw(screen)
                ENVIRONMENT_SPRITES.draw(screen)
                DECOR_SPRITES.draw(screen)
                PLAYER.draw(screen)

                player.update(ENVIRONMENT_SPRITES, DANGER_SPRITES, player, dt)
                HEALTH.draw(screen)

                for i in ENVIRONMENT_SPRITES:
                    if i.rect.y < -1500:
                        running = False
                    break

                if player.health < 0:
                    running = False

                pygame.display.flip()
                dt = clock.tick(fps) / 1000
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    key = pygame.key.get_pressed()
                    if key[pygame.K_ESCAPE]:
                        pause = False
                    for button in pause_buttons:
                        if button.handle_event(event) == 'exit':
                            running = False
                        if button.handle_event(event) == 'continue':
                            pause = False

                player.right_move = False
                player.left_move = False
                player.x_speed = 0
                player.y_speed = 0

                BACKGROUND.draw(screen)
                DANGER_SPRITES.draw(screen)
                FINISH.draw(screen)
                ENVIRONMENT_SPRITES.draw(screen)
                DECOR_SPRITES.draw(screen)
                PLAYER.draw(screen)
                HEALTH.draw(screen)

                PAUSE.draw(screen)
                for button in pause_buttons:
                    button.draw(screen)

                pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for button in win_buttons:
                    if button.handle_event(event) == 'exit':
                        running = False

            BACKGROUND.draw(screen)
            FINISH_SCREEN.draw(screen)

            for button in win_buttons:
                button.draw(screen)

            pygame.display.flip()


    pygame.quit()


if __name__ == '__main__':
    main()
