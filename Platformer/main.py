import sys
import pygame
from LevelMenu import level_manu
from data.Button import Button
from data.Slider import Slider
from constants import WIDTH, HEIGHT, screen


def continue_game():
    print("Продолжение игры")
    pass


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

# Размеры окна
pygame.display.set_caption("Ketdventure")

# Загрузка фона
try:
    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Ошибка загрузки фона: {e}")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0))

# Переменные настроек
brightness = 100
volume = 50

# Создание кнопок
menu_buttons = [
    Button(WIDTH // 2 - 100, 150, 200, 50, "Начать игру", level_manu),
    Button(WIDTH // 2 - 125, 250, 225, 50, "Продолжить игру", continue_game),
    Button(WIDTH // 2 - 100, 350, 200, 50, "Настройки", open_settings),
    Button(WIDTH // 2 - 100, 450, 200, 50, "Выход", exit_game)
]

settings_buttons = [
    Button(WIDTH // 2 - 100, 500, 200, 50, "Назад", close_settings)
]

# Создание слайдеров
brightness_slider = Slider(WIDTH // 2 - 200, 150, 400, 30, 0, 100, brightness, "Яркость")
volume_slider = Slider(WIDTH // 2 - 200, 250, 400, 30, 0, 100, volume, "Громкость")
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
            for slider in sliders:
                slider.handle_event(event)

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
        for button in menu_buttons:
            button.draw(screen)
    elif menu_state == "settings":
        for button in settings_buttons:
            button.draw(screen)
        for slider in sliders:
            slider.draw(screen)

    pygame.display.flip()

pygame.quit()
