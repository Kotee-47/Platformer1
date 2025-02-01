import sys
import pygame
from data.Player import Player
from data.Camera import Camera
from data.Background import Background
from data.Board import Board
from data.PauseButton import PauseButton


class game:
    def main():
        play_music('lena-raine-prologue.mp3')
        ALL_SPRITES = pygame.sprite.Group()
        ENVIRONMENT_SPRITES = pygame.sprite.Group()
        DECOR_SPRITES = pygame.sprite.Group()
        DANGER_SPRITES = pygame.sprite.Group()
        PLAYER = pygame.sprite.Group()
        HEALTH = pygame.sprite.Group()
        BACKGROUND = pygame.sprite.Group()
        PAUSE = pygame.sprite.Group()
        CELL_SIZE = 64
        pygame.init()
        pygame.display.set_icon(pygame.image.load("images/icons/ktetmeliv.png"))
        size = width, height = 1080, 720
        board = Board(ENVIRONMENT_SPRITES, DECOR_SPRITES, ALL_SPRITES, DANGER_SPRITES, CELL_SIZE)
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Ketdventure")
        running = True
        dt = 0
        fps = 120
        player = Player(PLAYER, ALL_SPRITES, HEALTH, 3, 8,
                        width, height, CELL_SIZE)
        objects = board.render(screen)
        camera = Camera(width, height, CELL_SIZE)
        Background(BACKGROUND, 'images/backgrounds/cave.png')
        Background(PAUSE, 'images/pause/backgrnd_pause.png')
        pause = False
        pause_buttons = [
            PauseButton(1080 // 2 - 200, 270, 400, 100, "Продолжить игру", 'continue'),
            PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
        ]
        win_buttons = [
            PauseButton(1080 // 2 - 200, 270, 400, 100, "Следующий уровень", None),
            PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
        ]

        while running:
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
                    for button in pause_buttons:
                        if button.handle_event(event) == 'exit':
                            running = False
                        if button.handle_event(event) == 'continue':
                            pause = False

                player.update(ENVIRONMENT_SPRITES, DANGER_SPRITES, dt)
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
                        running = False
                    key = pygame.key.get_pressed()
                    if key[pygame.K_ESCAPE]:
                        pause = False
                    for button in pause_buttons:
                        if button.handle_event(event) == 'exit':
                            running = False
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
                HEALTH.draw(screen)
                PAUSE.draw(screen)

                for button in pause_buttons:
                    button.draw(screen)

                pygame.display.flip()

        pygame.quit()