from pico2d import *

class GameStart:
    def __init__(self):
        self.image = load_image('game_start_sprite_sheet.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 100, 100, 400, 500)

    def update(self):
        pass

class GameRule:
    def __init__(self):
        self.image = load_image('game_rule_sprite_sheet.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 745, 0, 100, 100, 400, 300)

    def update(self):
        pass