from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, play_mode
from menu import GameRule
from menu import GameStart


def handle_events():
    global running
    global mouse_x, mouse_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif  SDL_MOUSEMOTION:
            mouse_x = event.x
            mouse_y = event.y
            #game_framework.change_mode(play_mode)
        elif  SDL_MOUSEBUTTONUP:
            mouse_x = event.x
            mouse_y = event.y
            #game_framework.change_mode(play_mode)


def init():
    global image
    global gamestart
    global gamerule

    image = load_image('lobby_background.png')


def finish():
    global image
    del image


def update():
    pass



def draw():
    clear_canvas()
    image.draw(800, 450)
    update_canvas()
