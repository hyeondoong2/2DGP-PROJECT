from pico2d import load_image, draw_rectangle
import game_world

class Tray:
    def __init__(self):
        self.image = load_image('resources/tray.png')
        self.x, self.y = 1250, 450
        self.origin_x, self.origin_y = 1250, 450
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.bb_x, self.bb_y = 50, 50
        self.width, self.height = 181, 118
        self.move_right = False

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def get_bb(self):
        # fill here
        return (self.x - self.bb_x + 50, self.y - self.bb_y,
                self.x + self.bb_x + 50, self.y + self.bb_y)

    def update(self,x, y):
        if self.move_right:
            self.x += 3

        if self.x > 1700:
            self.x = self.origin_x
            self.move_right = False
        pass

    def handle_collision(self, group, other):

        pass
