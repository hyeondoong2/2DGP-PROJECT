from pico2d import *
import game_world
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, title_mode
from kitchen import Kitchen
from fire import Fire

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

    running = True
    kitchen = Kitchen()
    fire = [
        Fire(480, 470),
        Fire(690, 470),
        Fire(400, 380),
        Fire(600, 380),
        Fire(800, 380)
    ]

    game_world.add_object(kitchen, 0)
    for f in fire:
        game_world.add_object(f, 1)





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