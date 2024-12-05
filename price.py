import random
from pico2d import load_image, load_font
import game_world
import play_mode
from recipe import Recipe

class Price:
    def __init__(self, type, price):
        self.type = type
        self.time = 0
        self.goLeft = False
        self.goRight = False
        self.price = price
        self.font = load_font("resources/UhBee Seulvely.ttf", 50)
        if self.type == 1:
            self.image = load_image('resources/price1.png')
            pass
        elif self.type == 2:
            self.image = load_image('resources/price2.png')
            pass
        elif self.type == 3:
            self.image = load_image('resources/price3.png')
            pass
        elif self.type == 4:
            self.image = load_image('resources/price4.png')
            pass
        self.x, self.y = 1800, 600


    def draw(self):
        self.image.clip_composite_draw(
            0, 0, 1040, 708,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            500, 300  # 그릴 크기 (width, height)
        )
        #self.image.draw(self.x, self.y)

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def update(self,x, y):
        if self.goLeft == False and self.x > 1200:
            self.x -= 7

        if self.x < 1200:
            self.goLeft = True

        if self.goLeft == True:
            self.time += 1

        if self.time > 100:
            self.goRight = True
            self.time = 0

        if self.goRight:
            self.x += 7
            if self.x > 1600:
                game_world.remove_object(self)


        pass


    def handle_collision(self, group, other):
        # fill here
        pass
