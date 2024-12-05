from pico2d import load_image, draw_rectangle
import game_world

class Tray:
    def __init__(self):
        self.image = load_image('resources/tray.png')
        self.x, self.y = 1250, 450
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.bb_x, self.bb_y = 80, 80
        self.width, self.height = 181, 118

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def get_bb(self):
        # fill here
        return self.x - self.bb_x, self.y - self.bb_y, self.x + self.bb_x, self.y + self.bb_y

    def update(self,x, y):
        pass

    def handle_collision(self, group, other):

        pass
