from pico2d import load_image

class Kitchen:
    def __init__(self):
        self.image = load_image('resources/kitchen_background.png')

    def draw(self):
        self.image.draw(800, 450)

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def update(self,x, y):
        pass

    def handle_collision(self, group, other):
        pass
