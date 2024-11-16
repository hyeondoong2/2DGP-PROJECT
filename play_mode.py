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

mouse_x, mouse_y = 0, 0
money = 0

def handle_events():
    global running
    global mouse_x, mouse_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)


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

    running = True
    kitchen = Kitchen()
    egg =  Egg()
    noodle = Noodle()
    powder = Powder()
    springOnion = SpringOnion()
    fire = [
        Fire(530, 470),
        Fire(740, 470),
        Fire(460, 380),
        Fire(660, 380),
        Fire(860, 380)
    ]

    pot = [
        Pot(525, 510, 1),
        Pot(735, 510, 1),
        Pot(455, 420, 1),
        Pot(655, 420,1 ),

        Pot(890, 800,1 ),
        Pot(990, 800, 1),
        Pot(1090, 800, 1),
    ]

    game_world.add_object(kitchen, 0)
    game_world.add_object(egg, 1)
    game_world.add_object(noodle, 1)
    game_world.add_object(powder, 1)
    game_world.add_object(springOnion, 1)

    for f in fire:
        game_world.add_object(f, 1)

    for p in pot:
        game_world.add_object(p, 1)






def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass