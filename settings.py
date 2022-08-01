class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        # Параметры экрана
        self.fullscreen = False
        self.screen_width = 1800
        self.screen_height = 800
        self.bg_color_dark = (46, 41, 51)
        self.bg_color_light = (130, 105, 233)

        self.game_theme = False # True = light; False = dark

        self.ship_speed = 2.4

        # Параметры снаряда
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowd = 3