from pico2d import load_image

class Kitchen:
    def __init__(self):
        self.image = load_image('kitchen_background.png')

    def draw(self):
        self.image.draw(800, 450)

    def check(self, x, y):
        pass

    def update(self,x, y):
        pass
