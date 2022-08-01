import sys
import pygame
from pygame import event
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурмами и поведением игры."""

    def __init__(self):
        """Инизиализует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("AliensSex")

        self.bg_color = self.settings.bg_color_light
        # Какая выбрана тема
        if self.settings.game_theme == False:
            self.bg_color = self.settings.bg_color_dark

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        
    def run_game(self):
        """Заупуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_d:
            # Переместить кораблеь вправо
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # Переместить кораблеь влево
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Выход из игры
            sys.exit()
        elif event.key == pygame.K_f:
            self._toggle_fullscreen()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            

    def _toggle_fullscreen(self):
        """Переход в полноэкранный режим и обратно"""
        if self.settings.fullscreen == False:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self.ship = Ship(self)
            self.settings.fullscreen = True

        elif self.settings.fullscreen == True:
            self.settings = Settings()
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.ship = Ship(self)

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowd:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)


        # Создание первого ряда пришельцев.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        # Создание пришельца и размещение его в ряду.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Обновляет изображение на эране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
        

if __name__ == '__main__':
    # Создание экземлеяра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()