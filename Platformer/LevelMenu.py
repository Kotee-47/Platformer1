import sys
import pygame
from constants import WIDTH, HEIGHT, WHITE, RED, GREEN, BLACK, screen
from Level1 import run_level


def level_manu():
    # Настройки окна
    pygame.display.set_caption("Catdventure")

    # Шрифты
    font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 36)

    # Текст заголовка
    title_text = font.render("Catventure", True, BLACK)

    # Количество уровней
    levels = 10

    # Создание кнопок
    buttons = []
    button_width, button_height = 150, 50
    button_margin = 20

    # Список функций для уровней
    level_functions = [run_level, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Расположение кнопок в два ряда
    for i in range(levels):
        row = i // 5
        col = i % 5
        x = (WIDTH - (5 * button_width + 4 * button_margin)) // 2 + col * (button_width + button_margin)
        y = (HEIGHT - (2 * button_height + 1 * button_margin)) // 2 + row * (button_height + button_margin)
        button = pygame.Rect(x, y, button_width, button_height)
        buttons.append({"rect": button, "color": GREEN, "pressed": False, "function": level_functions[i]})

    # Кнопка выхода
    exit_button = {"rect": pygame.Rect((WIDTH - button_width) // 2, HEIGHT - 100, button_width, button_height),
                   "color": GREEN, "pressed": False}

    # Основной цикл
    running = True
    while running:
        screen.fill(WHITE)

        # Отображение заголовка
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        # Отображение кнопок уровней
        for button_data in buttons:
            button = button_data["rect"]
            color = button_data["color"]
            pygame.draw.rect(screen, color, button)
            level_text = button_font.render(f"Level {buttons.index(button_data) + 1}", True, BLACK)
            screen.blit(level_text, (button.x + 30, button.y + 15))

        # Отображение кнопки выхода
        pygame.draw.rect(screen, exit_button["color"], exit_button["rect"])
        exit_text = button_font.render("Exit", True, BLACK)
        screen.blit(exit_text, (exit_button["rect"].x + 50, exit_button["rect"].y + 15))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button_data in buttons:
                    if button_data["rect"].collidepoint(mouse_pos):
                        button_data["color"] = RED  # Меняем цвет на красный
                        button_data["pressed"] = True
                if exit_button["rect"].collidepoint(mouse_pos):
                    exit_button["color"] = RED
                    exit_button["pressed"] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for button_data in buttons:
                    if button_data["pressed"]:
                        button_data["color"] = GREEN  # Возвращаем цвет к зеленому
                        button_data["pressed"] = False
                        button_data["function"]()  # Вызываем функцию кнопки
                if exit_button["pressed"]:
                    exit_button["color"] = GREEN
                    exit_button["pressed"] = False
                    running = False  # Вызываем функцию кнопки выхода

        pygame.display.flip()
