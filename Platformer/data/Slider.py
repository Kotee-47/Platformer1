import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)


class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value, text):
        self.font = pygame.font.Font(None, 36)
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
        text_surface = self.font.render(f"{self.text}: {int(self.value)}", True, BLACK)
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