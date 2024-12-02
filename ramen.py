from pico2d import load_image

class Ramen:
    def __init__(self):
        self.image = load_image('resources/pot.png')
        self.price = 0
        self.water = False
        self.egg = False
        self.noodle = False
        self.powder = False
        self.spring_onion = False
        self.isBurnt = False

    def draw(self):
        self.image.draw(800, 450)

    def update(self):
        pass
