from pico2d import *
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, play_mode
from menu import GameStart

mouse_x, mouse_y = 0, 0

def handle_events():
    global running
    global mouse_x, mouse_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 900 - event.y  # PyGame은 좌표계가 다름
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # 메뉴 클릭 처리
            if gameStart.isDragged:
                gameStart.effect.play()
                play_mode.TIME_OUT = False
                game_framework.change_mode(play_mode)  # GameStart 메뉴 클릭 시 플레이 모드로 전환


def init():
    global image
    global gameStart
    gameStart = GameStart()

    gameStart.x, gameStart.y = 1400, 170

    image = load_image('resources/rule_background.png')


def finish():
    global image
    del image


def update():
    # 마우스 상태에 따라 메뉴 업데이트
    gameStart.update(mouse_x, mouse_y)
    pass


def draw():
    clear_canvas()
    image.draw(800, 450)
    gameStart.draw()
    update_canvas()
