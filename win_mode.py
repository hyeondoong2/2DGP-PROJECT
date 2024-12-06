from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, play_mode, rule_mode
from menu import GameRule
from menu import GameStart
from mom import Mom

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
                game_framework.change_mode(play_mode)  # GameStart 메뉴 클릭 시 플레이 모드로 전환
            elif gameRule.isDragged:
                game_framework.change_mode(rule_mode)  # GameRule 메뉴 클릭 시 규칙 출력 (예시)

def init():
    global image
    global gameStart
    global gameRule
    global mama

    gameStart = GameStart()
    gameRule = GameRule()
    mama = Mom()

    image = load_image('resources/result_win_background.png')


def finish():
    global image
    del image


def update():
    # 마우스 상태에 따라 메뉴 업데이트
    gameStart.update(mouse_x, mouse_y)
    gameRule.update(mouse_x, mouse_y)
    mama.update()



def draw():
    clear_canvas()
    image.draw(800, 450)
    gameStart.draw()
    gameRule.draw()
    mama.draw()
    update_canvas()
