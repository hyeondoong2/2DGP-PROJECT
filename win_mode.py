from pico2d import load_image, get_time, clear_canvas, update_canvas, get_events, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, play_mode, rule_mode, title_mode
from menu import GameAgain
from menu import GameExit
from mom import Mom

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
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 900 - event.y  # PyGame은 좌표계가 다름
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # 메뉴 클릭 처리
            if gameAgain.isDragged:
                play_mode.TIME_OUT = False
                game_framework.change_mode(play_mode)  # GameStart 메뉴 클릭 시 플레이 모드로 전환
            elif gameExit.isDragged:
                play_mode.TIME_OUT = False
                game_framework.change_mode(title_mode)  # GameRule 메뉴 클릭 시 규칙 출력 (예시)
            pass

def init():
    global image
    global gameAgain
    global gameExit
    global mama
    global font

    gameAgain = GameAgain()
    gameExit = GameExit()
    mama = Mom('happy')

    image = load_image('resources/result_win_background.png')
    font = load_font("resources/UhBee Seulvely.ttf", 60)

def finish():
    global image
    del image


def update():
    # 마우스 상태에 따라 메뉴 업데이트
    gameAgain.update(mouse_x, mouse_y)
    gameExit.update(mouse_x, mouse_y)
    mama.update()



def draw():
    clear_canvas()
    image.draw(800, 450)
    font.draw(450, 580, f'{money:,}', (255, 255, 153))  # 연노랑 글씨로 표시
    gameAgain.draw()
    gameExit.draw()
    mama.draw()
    update_canvas()
