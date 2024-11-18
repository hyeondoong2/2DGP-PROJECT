from pico2d import load_image

class Tray:
    def __init__(self):
        self.image = load_image('tray.png')

    def draw(self):
        self.image.draw(1250, 450)

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def update(self,x, y):
        pass

    def handle_collision(self, group, other):
        pass
