import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = WHITE
        self.hover_color = GRAY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
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
