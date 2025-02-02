import pygame
from data.Player import Player
from data.Board import Board
from data.Background import Background
from data.Camera import Camera
from data.PauseButton import PauseButton
from constants import ALL_SPRITES, ENVIRONMENT_SPRITES, DECOR_SPRITES, DANGER_SPRITES, PLAYER, HEALTH, BACKGROUND, \
    PAUSE, WIDTH, HEIGHT, CELL_SIZE,JUMP_PADS, FINISH, screen


# Функции действий кнопок
def run_level():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load('lena-raine-prologue.mp3')
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Ошибка при загрузке или проигрывании музыки: {e}")

    pygame.display.set_icon(pygame.image.load("images/icons/ktetmeliv.png"))
    pygame.display.set_caption("Ketdventure")
    size = 1080, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ketdventure")
    running = True
    dt = 0
    finish_c = 0
    finished = False
    level2 = 'files/levels/yara_test_field.txt'
    fps = 120
    player = Player(PLAYER, ALL_SPRITES, HEALTH, 3, 8,
                    WIDTH, HEIGHT, CELL_SIZE)
    board = Board(ENVIRONMENT_SPRITES, DECOR_SPRITES, ALL_SPRITES, DANGER_SPRITES, FINISH, JUMP_PADS)
    objects = board.render(screen)
    camera = Camera(WIDTH, HEIGHT, CELL_SIZE)
    Background(BACKGROUND, 'images/backgrounds/cave.png')
    Background(PAUSE, 'images/pause/backgrnd_pause.png')

    pause_buttons = [
        PauseButton(1080 // 2 - 200, 270, 400, 100, "Продолжить игру", 'continue'),
        PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]
    win_buttons = [
        PauseButton(1080 // 2 - 200, 270, 400, 100, "Следующий уровень", None),
        PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]

    clock = pygame.time.Clock()
    pause = False
    running = True
    while running:
        if not finished:
            if not pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
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
                    for button in pause_buttons:
                        if button.handle_event(event) == 'exit':
                            pygame.quit()
                        if button.handle_event(event) == 'continue':
                            pause = False

            player.update(ENVIRONMENT_SPRITES, DANGER_SPRITES, dt)
            if 'turrets' in objects.keys():
                for obj in objects['turrets']:
                    obj.update(player.x, player.y)

            camera.update(player)
            for sprite in ALL_SPRITES:
                camera.apply(sprite)

            screen.fill("grey")
            BACKGROUND.draw(screen)
            ENVIRONMENT_SPRITES.draw(screen)
            DANGER_SPRITES.draw(screen)
            DECOR_SPRITES.draw(screen)
            PLAYER.draw(screen)
            HEALTH.draw(screen)

            for i in ENVIRONMENT_SPRITES:
                if i.rect.y < -1500:
                    running = False
                break

            pygame.display.flip()
            dt = clock.tick(fps) / 1000
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    pause = False
                for button in pause_buttons:
                    if button.handle_event(event) == 'exit':
                        pygame.quit()
                    elif button.handle_event(event) == 'continue':
                        pause = False

            player.right_move = False
            player.left_move = False
            player.x_speed = 0
            player.y_speed = 0

            BACKGROUND.draw(screen)
            ENVIRONMENT_SPRITES.draw(screen)
            DANGER_SPRITES.draw(screen)
            DECOR_SPRITES.draw(screen)
            PLAYER.draw(screen)
            JUMP_PADS.draw(screen)
            HEALTH.draw(screen)
            FINISH.draw(screen)
            PAUSE.draw(screen)

            for i in PLAYER:
                if pygame.sprite.spritecollideany(i, FINISH):
                    finish_c += 1
                    if finish_c > 50:
                        finished = True
                if pygame.sprite.spritecollideany(i, JUMP_PADS):
                    player.y_speed = -1200

            for button in pause_buttons:
                button.draw(screen)

            pygame.display.flip()
