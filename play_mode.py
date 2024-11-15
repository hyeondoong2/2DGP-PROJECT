from pico2d import *

import game_world

import game_framework, title_mode


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        #elif (event.type, event.key) == (SDL_KEYUP, SDLK_i):
            #game_framework.push_mode(item_mode)


def init():
    global running
    global boy

    running = True



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