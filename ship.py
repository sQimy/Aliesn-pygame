import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализурует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('image/1.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра кораБЛЯ
        self.x = float(self.rect.x)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию кораблся с учетеом флага"""
        # Обновляется атрибут х, не rect
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x