import pygame
import sys
import pygame
from data import functions
from data import classes

pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Загрузка фона
try:
    background = pygame.image.load("фон.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Ошибка загрузки фона: {e}")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0))

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Шрифт
font = pygame.font.Font(None, 36)


# Класс для кнопки
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = WHITE
        self.hover_color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = WHITE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return self.action
        return None


# Класс для слайдера
class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.handle_radius = height // 2
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.text = text
        self.dragging = False

    def draw(self, surface):
        # Рисуем фон слайдера
        pygame.draw.rect(surface, GRAY, self.rect)

        # Вычисляем позицию ручки слайдера на основе текущего значения
        ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        handle_x = self.rect.x + int(ratio * self.rect.width)

        # Рисуем ручку
        pygame.draw.circle(surface, WHITE, (handle_x, self.rect.centery), self.handle_radius)

        # Рисуем текст слайдера
        text_surface = font.render(f"{self.text}: {int(self.value)}", True, BLACK)
        text_rect = text_surface.get_rect(bottomleft=(self.rect.left, self.rect.top - 5))
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.get_handle_rect().collidepoint(event.pos):
                    self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x = event.pos[0]
                new_value = self.min_value + (
                            max(min(mouse_x, self.rect.right), self.rect.left) - self.rect.left) / self.rect.width * (
                                        self.max_value - self.min_value)
                self.value = round(max(min(new_value, self.max_value), self.min_value))

    def get_handle_rect(self):
        ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        handle_x = self.rect.x + int(ratio * self.rect.width)
        handle_rect = pygame.Rect(handle_x - self.handle_radius,
                                  self.rect.y,
                                  self.handle_radius * 2,
                                  self.rect.height)
        return handle_rect

    def get_value(self):
        return self.value


# Переменные настроек
brightness = 100
volume = 50

# Глобальные переменные для игры
ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
CELL_SIZE = 16
game_running = False  # переменная, которая будет запускать игру только если она была вызвана из меню
game_screen = None  # переменная для экрана, для избежания конфликтов


# Функции действий кнопок
def start_game():
    global game_running, game_screen
    print("Начало игры")

    size = width, height = 640, 320
    board = classes.Board(ENVIRONMENT_SPRITES, CELL_SIZE)
    game_screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("erm")
    running = True
    dt = 0
    fps = 30
    board.set_view(0, 0)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)

        game_screen.fill("black")
        board.render(game_screen)
        ENVIRONMENT_SPRITES.draw(game_screen)

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

    game_running = False  # сбрасываем переменную при выходе из игрового цикла
    pygame.display.set_mode((WIDTH, HEIGHT))  # возвращаем размеры окна меню
    pygame.display.set_caption("Меню игры")  # возвращаем заголовок меню


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


# Создание кнопок
menu_buttons = [
    Button(WIDTH // 2 - 100, 150, 200, 50, "Начать игру", start_game),
    Button(WIDTH // 2 - 100, 250, 200, 50, "Продолжить игру", continue_game),
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