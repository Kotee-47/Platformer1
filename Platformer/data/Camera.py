class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.cell_size = cell_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x = obj.rect.x + self.dx - self.cell_size // 2
        obj.rect.y = obj.rect.y + self.dy - self.cell_size // 4

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + self.cell_size // 2 - self.width // 2)
        self.dy = -(target.rect.y + self.cell_size // 2 - self.height // 2)
