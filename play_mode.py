from pico2d import *
import game_world
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, title_mode
from kitchen import Kitchen
from fire import Fire
from egg import Egg
from noodle import Noodle
from powder import Powder
from spring_onion import SpringOnion
from pot import Pot
from kettle import Kettle
import os

mouse_x, mouse_y = 0, 0
click_x, click_y = 0, 0

class Game:
    def __init__(self):
        self.font = load_font("UhBee Seulvely.ttf", 50)
        self.money = 0

    def draw(self):
        self.font.draw(1350, 720, f'{self.money:01d}', (0, 0, 0))
        pass

    def check(self, x, y):
        pass

    def update(self,x, y):
        pass

def handle_events():
    global running
    global mouse_x, mouse_y
    global click_x, click_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 900 - event.y  # PyGame은 좌표계가 다름
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # 메뉴 클릭 처리
            click_x, click_y = event.x, 900 - event.y
            game_world.check_selected(click_x, click_y)


def init():
    global running
    global boy
    global background
    global kitchen
    global fire
    global egg
    global noodle
    global powder
    global springOnion
    global pot
    global kettle
    global game

    running = True
    kitchen = Kitchen()
    egg =  Egg()
    noodle = Noodle()
    powder = Powder()
    springOnion = SpringOnion()
    kettle = Kettle()
    game = Game()

    fire = [
        Fire(530, 470),
        Fire(740, 470),
        Fire(460, 380),
        Fire(660, 380),
        Fire(860, 380)
    ]

    pot = [
        Pot(525, 510, True),
        Pot(735, 510, True),
        Pot(455, 420, True),
        Pot(655, 420,True ),

        Pot(890, 800,False ),
        Pot(990, 800, False),
        Pot(1090, 800, False),
    ]

    game_world.add_object(kitchen, 0)
    game_world.add_objects(fire, 1)
    game_world.add_objects(pot, 1)

    game_world.add_object(egg, 1)
    game_world.add_object(noodle, 1)
    game_world.add_object(powder, 1)
    game_world.add_object(springOnion, 1)

    game_world.add_object(kettle, 1)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update(mouse_x, mouse_y)
    pass


def draw():
    clear_canvas()
    game_world.render()
    game.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

