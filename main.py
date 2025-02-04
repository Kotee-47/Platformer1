import pygame
from data import classes
from data import functions
from config import *
from copy import deepcopy
import sys
from data.classes import Button
from data.classes import Slider


def menu():
    pygame.mixer.init()
    try:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music_and_sounds/prologue.mp3'), -1)
    except pygame.error as e:
        print(f"Ошибка при загрузке или проигрывании музыки: {e}")

    def open_settings():
        global menu_state
        menu_state = "settings"

    def close_settings():
        global menu_state
        menu_state = "main"

    def exit_game():
        pygame.quit()
        sys.exit()

    pygame.init()
    size = width, height = 1080, 720
    screen = pygame.display.set_mode(size)

    # Размеры окна
    pygame.display.set_caption("Ketdventure")

    # Загрузка фона
    try:
        background = pygame.image.load("images/backgrounds/menu_backgrnd.png").convert()
        background = pygame.transform.scale(background, (width, height))
    except pygame.error as e:
        print(f"Ошибка загрузки фона: {e}")
        background = pygame.Surface((width, height))
        background.fill((0, 0, 0))

    # Переменные настроек
    brightness = 100
    volume = 50

    # Создание кнопок
    menu_buttons = [
        Button(width // 2 + 300, 20, 225, 50, "Начать игру", level_menu),
        Button(width // 2 + 300, 160, 225, 50, "Настройки", open_settings),
        Button(width // 2 + 300, 90, 225, 50, "Выход", exit_game)
    ]

    settings_buttons = [
        Button(width // 2 - 100, 500, 200, 50, "Назад", close_settings)
    ]

    # Создание слайдеров
    brightness_slider = Slider(width // 2 - 200, 150, 400, 30, 0, 100, brightness, "Яркость")
    volume_slider = Slider(width // 2 - 200, 250, 400, 30, 0, 100, volume, "Громкость")
    sliders = [brightness_slider, volume_slider]

    # Состояние меню
    menu_state = "main"

    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if menu_state == "main":
                for button in menu_buttons:
                    action = button.handle_event(event)
                    if action:
                        action()
            elif menu_state == "settings":
                for button in settings_buttons:
                    action = button.handle_event(event)
                    if action:
                        action()
                #for slider in sliders:
                    #slider.handle_event(event)
                sliders[2].handle_event(event)

        # Обновление значений
        brightness = brightness_slider.get_value()
        volume = volume_slider.get_value()
        # применение яркости
        brightness_factor = brightness / 100.0
        # затемняем фон
        overlay = pygame.Surface(background.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, int(255 * (1 - brightness_factor))))
        screen.blit(background, (0, 0))
        screen.blit(overlay, (0, 0))

        # Отрисовка
        if menu_state == "main":
            # for button in menu_buttons:
            #     button.draw(screen)
            menu_buttons[0].draw(screen)
            menu_buttons[2].draw(screen)
        elif menu_state == "settings":
            for button in settings_buttons:
                button.draw(screen)
            for slider in sliders:
                slider.draw(screen)

        pygame.display.flip()

    pygame.quit()


def level_menu():
    # Настройки окна
    size = width, height = 1080, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ketdventure")
    pygame.font.init()
    pygame.mixer.init()
    try:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music_and_sounds/awake.mp3'), -1)
    except pygame.error as e:
        print(f"Ошибка при загрузке или проигрывании музыки: {e}")
    # Шрифты
    font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 36)

    # Текст заголовка
    title_text = font.render("Ketdventure", True, 'black')

    # Количество уровней
    levels = 10

    # Создание кнопок
    buttons = []
    button_width, button_height = 150, 50
    button_margin = 20

    # Список функций для уровней
    level_functions = [(main, 'files/levels/chapt1/level1.txt'),
                       (main, 'files/levels/chapt1/level2.txt'),
                       (main, 'files/levels/chapt1/level3.txt'),
                       (main, 'files/levels/chapt1/level4.txt'),
                       (main, 'files/levels/chapt1/level5.txt'),
                       (main, 'files/levels/chapt1/level6.txt'),
                       (main, 'files/levels/chapt1/level7.txt'),
                       (main, 'files/levels/chapt1/level8.txt'),
                       (main, 'files/levels/chapt1/level9.txt'),
                       (main, 'files/levels/chapt1/level10.txt')]

    # Расположение кнопок в два ряда
    for i in range(levels):
        row = i // 5
        col = i % 5
        x = (width - (5 * button_width + 4 * button_margin)) // 2 + col * (button_width + button_margin)
        y = (height - (2 * button_height + 1 * button_margin)) // 2 + row * (button_height + button_margin)
        button = pygame.Rect(x, y, button_width, button_height)
        buttons.append({"rect": button, "color": 'green', "pressed": False, "function": level_functions[i]})

    # Кнопка выхода
    exit_button = {"rect": pygame.Rect((width - button_width) // 2, height - 100, button_width, button_height),
                   "color": 'green', "pressed": False}

    # Основной цикл
    running = True
    while running:
        screen.fill('white')

        # Отображение заголовка
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 50))

        # Отображение кнопок уровней
        for button_data in buttons:
            button = button_data["rect"]
            color = button_data["color"]
            pygame.draw.rect(screen, color, button)
            level_text = button_font.render(f"Уровень {buttons.index(button_data) + 1}",
                                            True, 'black')
            screen.blit(level_text, (button.x + 10, button.y + 15))

        # Отображение кнопки выхода
        pygame.draw.rect(screen, exit_button["color"], exit_button["rect"])
        exit_text = button_font.render("Выход", True, 'black')
        screen.blit(exit_text, (exit_button["rect"].x + 30, exit_button["rect"].y + 15))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button_data in buttons:
                    if button_data["rect"].collidepoint(mouse_pos):
                        button_data["color"] = 'red'  # Меняем цвет на красный
                        button_data["pressed"] = True
                if exit_button["rect"].collidepoint(mouse_pos):
                    exit_button["color"] = 'red'
                    exit_button["pressed"] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for button_data in buttons:
                    if button_data["pressed"]:
                        button_data["color"] = 'green'  # Возвращаем цвет к зеленому
                        button_data["pressed"] = False
                        button_data["function"][0](button_data["function"][1]) # Вызываем функцию кнопки
                        return
                if exit_button["pressed"]:
                    exit_button["color"] = 'green'
                    exit_button["pressed"] = False
                    running = False  # Вызываем функцию кнопки выхода

        pygame.display.flip()


def main(level):
    next_lv = 'files/levels/chapt1/level' + str(int(level[-5]) + 1) + '.txt'
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music_and_sounds/first-steps.mp3'), -1)
    except pygame.error as e:
        print(f"Ошибка при загрузке или проигрывании музыки: {e}")
    all_sp = deepcopy(ALL_SPRITES)
    env_sp = deepcopy(ENVIRONMENT_SPRITES)
    dec_sp = deepcopy(DECOR_SPRITES)
    dang_sp = deepcopy(DANGER_SPRITES)
    jump_sp = deepcopy(JUMP_PADS)
    player_sp = deepcopy(PLAYER)
    health_sp = deepcopy(HEALTH)
    backgr_sp = deepcopy(BACKGROUND)
    pause_sp = deepcopy(PAUSE)
    finish_sp = deepcopy(FINISH)
    f_screen_sp = deepcopy(FINISH_SCREEN)
    ded_sp = deepcopy(DEAD_SCREEN)

    pygame.display.set_icon(pygame.image.load("images/icons/ktetmeliv.png"))
    size = width, height = 1080, 720
    board = classes.Board(env_sp, dec_sp, all_sp, dang_sp, finish_sp, jump_sp, CELL_SIZE,
                          level)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ketdventure")
    running = True
    dt = 0
    fps = 120
    objects = {}
    board.render(screen, objects)
    player = classes.Player(player_sp, all_sp, health_sp, board.spawn[0], board.spawn[1],
                            width, height, CELL_SIZE)
    camera = classes.Camera(width, height, CELL_SIZE)
    classes.Background(backgr_sp, 'images/backgrounds/' + board.background)
    classes.Background(f_screen_sp, 'images/backgrounds/finished.png')
    classes.Background(pause_sp, 'images/backgrounds/backgrnd_pause.png')
    classes.Background(ded_sp, 'images/backgrounds/yu_ded.png')
    pause = False
    finish_c = 0
    finished = False
    ded = False

    pause_buttons = [
        classes.PauseButton(1080 // 2 - 200, 270, 400, 100, "Продолжить игру", 'continue'),
        classes.PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]
    win_buttons = [
        classes.PauseButton(1080 // 2 - 200, 270, 400, 100, "Следующий уровень", 'next'),
        classes.PauseButton(1080 // 2 - 200, 380, 400, 100, "Выход", 'exit')
    ]

    while running:
        if not ded:
            if not finished:
                if not pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        key = pygame.key.get_pressed()
                        if key[pygame.K_a]:
                            player.left(player_sp)
                            player.left_move = True
                        else:
                            player.left_move = False
                        if key[pygame.K_d]:
                            player.right(player_sp)
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
                    if 'turrets' in objects.keys():
                        for obj in objects['turrets']:
                            obj.update(player.rect.x, player.rect.y)

                    camera.update(player)
                    for sprite in all_sp:
                        camera.apply(sprite)

                    for i in player_sp:
                        if pygame.sprite.spritecollideany(i, finish_sp):
                            finish_c += 1
                            if finish_c > 50:
                                finished = True
                        if pygame.sprite.spritecollideany(i, jump_sp):
                            player.y_speed = -1200

                    backgr_sp.draw(screen)
                    dang_sp.draw(screen)
                    finish_sp.draw(screen)
                    env_sp.draw(screen)
                    jump_sp.draw(screen)
                    dec_sp.draw(screen)
                    player_sp.draw(screen)

                    player.update(env_sp, dang_sp, player, dt)
                    health_sp.draw(screen)

                    for i in env_sp:
                        if i.rect.y < -1500:
                            ded = True
                        break

                    if player.health < 0:
                        ded = True

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

                    backgr_sp.draw(screen)
                    dang_sp.draw(screen)
                    finish_sp.draw(screen)
                    env_sp.draw(screen)
                    dec_sp.draw(screen)
                    player_sp.draw(screen)
                    health_sp.draw(screen)

                    pause_sp.draw(screen)
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
                        if button.handle_event(event) == 'next':
                            main(next_lv)
                            return

                backgr_sp.draw(screen)
                f_screen_sp.draw(screen)

                for button in win_buttons:
                    button.draw(screen)

                pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if win_buttons[1].handle_event(event) == 'exit':
                    running = False

            backgr_sp.draw(screen)
            ded_sp.draw(screen)

            win_buttons[1].draw(screen)

            pygame.display.flip()

    level_menu()


if __name__ == '__main__':
    menu()
