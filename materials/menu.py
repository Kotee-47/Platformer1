import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню")

# Загрузка изображения фона
try:
    background = pygame.image.load("фон.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабирование до размера окна
except pygame.error as e:
    print(f"Ошибка загрузки изображения: {e}")
    background = None  # если изображение не загрузилось, то background будет None и его не будем отображать

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)


# Класс для кнопки
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x + 400, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = font
        self.text_surf = self.font.render(self.text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        color = self.color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.hover_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()


# Функции для действий кнопок
def start_game():
    print("Начало игры")
    # Код для начала игры


def continue_game():
    print("Продолжение игры")
    # Код для продолжения игры


def exit_game():
    print("Выход из игры")
    pygame.quit()
    sys.exit()


# Создание кнопок
start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 80, 200, 50, "Начать", GRAY, RED, start_game)
continue_button = Button(WIDTH // 2 - 100, HEIGHT // 2, 200, 50, "Продолжить", GRAY, RED, continue_game)
exit_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 80, 200, 50, "Выйти", GRAY, RED, exit_game)

buttons = [start_button, continue_button, exit_button]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    # Отрисовка фона (если он загружен)
    if background:
        screen.blit(background, (0, 0))
    else:  # если не удалось загрузить фон, то сделаем заливку белым цветом
        screen.fill(WHITE)

    # Отрисовка кнопок
    for button in buttons:
        button.draw(screen)

    # Обновление экрана
    pygame.display.flip()