from pico2d import *

class GameStart:
    def __init__(self):
        self.image = load_image('game_start_sprite_sheet.png')
        self.frame = 0
        self.x, self.y = 350, 500  # 메뉴의 중심 좌표
        self.width, self.height = 300, 100 # 메뉴의 크기
        self.isDragged = False  # 마우스가 올라가 있는지 여부

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, self.width, self.height, self.x, self.y)

    def update(self, mouse_x, mouse_y):
        # 마우스가 메뉴 영역에 들어갔는지 확인
        self.isDragged = (self.x - self.width // 2 <= mouse_x <= self.x + self.width // 2 and
                      self.y - self.height // 2 <= mouse_y <= self.y + self.height // 2)

        if self.isDragged == True:
            self.frame = 1
        else:
            self.frame = 0

class GameRule:
    def __init__(self):
        self.image = load_image('game_rule_sprite_sheet.png')
        self.frame = 0
        self.x, self.y = 350, 370  # 메뉴의 중심 좌표
        self.width, self.height = 300, 100  # 메뉴의 크기
        self.isDragged = False  # 마우스가 올라가 있는지 여부

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, self.width, self.height, self.x, self.y)

    def update(self, mouse_x, mouse_y):
        # 마우스가 메뉴 영역에 들어갔는지 확인
        self.isDragged = (self.x - self.width // 2 <= mouse_x <= self.x + self.width // 2 and
                          self.y - self.height // 2 <= mouse_y <= self.y + self.height // 2)

        if self.isDragged == True:
            self.frame = 1
        else:
            self.frame = 0

        pass