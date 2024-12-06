import random
from random import randint

from pico2d import *

import game_world
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP
import game_framework, title_mode
import price
from kitchen import Kitchen
from fire import Fire
from egg import Egg
from noodle import Noodle
from powder import Powder
from spring_onion import SpringOnion
from pot import Pot
from kettle import Kettle
from recipe import Recipe
from tray import Tray
from price import Price
import time

# 딜레이를 관리하는 변수
recipe_creation_time = None
recipe_delay_duration = 1.0  # 딜레이 시간 (초)

mouse_x, mouse_y = 0, 0
click_x, click_y = 0, 0
up_x, up_y = 0, 0
global recipe

class Game:
    def __init__(self):
        self.font = load_font("resources/UhBee Seulvely.ttf", 50)
        self.money = 0

    def draw(self):
        self.font.draw(1320, 720, f'{self.money:01d}', (0, 0, 0))
        pass

    def check(self, x, y):
        pass

    def update(self):
        pass

def handle_events():
    global running
    global mouse_x, mouse_y
    global click_x, click_y
    global up_x, up_y

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
        elif event.type == SDL_MOUSEBUTTONUP:
            # 메뉴 클릭 처리
            up_x, up_y = event.x, 900 - event.y
            game_world.check_mouseUp(up_x, up_y)


def init():
    global running
    global boy
    global background
    global kitchen, tray
    global fire
    global egg
    global noodle
    global powder
    global springOnion
    global pot, temporary_pot
    global kettle
    global game
    global recipe

    running = True
    kitchen = Kitchen()
    egg =  Egg()
    noodle = Noodle()
    powder = Powder()
    springOnion = SpringOnion()
    kettle = Kettle()
    game = Game()
    tray = Tray()
    recipe = Recipe(random.randint(0, 3))

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
        Pot(655, 420,True )
    ]
    temporary_pot = [
        Pot(890, 800, False),
        Pot(990, 800, False),
        Pot(1090, 800, False)
    ]


    game_world.add_object(kitchen, 0)
    game_world.add_object(tray, 0)
    game_world.add_objects(fire, 1)
    game_world.add_objects(pot, 3)
    game_world.add_objects(temporary_pot, 3)

    game_world.add_object(noodle, 4)
    game_world.add_object(powder, 6)
    game_world.add_object(egg, 7)
    game_world.add_object(springOnion, 8)

    game_world.add_object(kettle, 9)
    game_world.add_object(recipe, 9)

    # 충돌 정보 등록
    game_world.add_collision_pair('pot:egg', egg, None)
    game_world.add_collision_pair('pot:powder', powder, None)
    game_world.add_collision_pair('pot:noodle', noodle, None)
    game_world.add_collision_pair('pot:springOnion', springOnion, None)
    game_world.add_collision_pair('pot:kettle', kettle, None)
    game_world.add_collision_pair('pot:tray', tray, None)

    for p in pot:
        game_world.add_collision_pair('pot:egg', None, p)
        game_world.add_collision_pair('pot:powder', None, p)
        game_world.add_collision_pair('pot:noodle', None, p)
        game_world.add_collision_pair('pot:springOnion',None, p)
        game_world.add_collision_pair('pot:kettle', None, p)
        game_world.add_collision_pair('pot:tray', None, p)


def finish():
    game_world.clear()
    pass

def check_score(pot):
    global price
    global recipe  # 함수 시작 부분에 global 선언
    global recipe_creation_time

    if (pot.isBurnt or pot.water == False or pot.isCooked == False
            or pot.noodle == False or pot.powder == False):
        pot.price = 0
        game.money += pot.price
        price = Price(1, pot.price)
        game_world.add_object(price, 10)
    elif recipe.type == 0:
        # 파o, 계란o
        if not pot.spring_onion:
            pot.price -= 250
        if not pot.egg:
            pot.price -= 250
        game.money += pot.price
    elif recipe.type == 1:
        # 파x, 계란 x
        if pot.spring_onion:
            pot.price -= 250
        if pot.egg:
            pot.price -= 250
        game.money += pot.price
    elif recipe.type == 2:
        # 계란 x
        if pot.egg:
            pot.price -= 500
        if not pot.spring_onion:
            pot.price -= 200
        game.money += pot.price
    elif recipe.type == 3:
        # 파 x
        if pot.spring_onion:
            pot.price -= 500
        if not pot.egg:
            pot.price -= 200
        game.money += pot.price

    if pot.price == 1000:
        price = Price(2, pot.price)
        game_world.add_object(price, 10)
    elif pot.price == 750:
        price = Price(3, pot.price)
        game_world.add_object(price, 10)
    elif pot.price == 500:
        price = Price(4, pot.price)
        game_world.add_object(price, 10)
    elif pot.price == 300:
        price = Price(5, pot.price)
        game_world.add_object(price, 10)
    elif pot.price == 800:
        price = Price(6, pot.price)
        game_world.add_object(price, 10)

    # 현재 recipe 제거
    game_world.remove_object(recipe)
    recipe_creation_time = time.time()  # 현재 시간을 기록
    pass

def get_temporary_pot():
    global temporary_pot
    if temporary_pot:  # 리스트가 비어있지 않은 경우
        pot = temporary_pot.pop(0)  # 가장 앞의 냄비를 가져옵니다
        game_world.remove_object(pot)  # 해당 냄비를 게임 월드에서 제거
        return pot  # 냄비 반환
    else:
        #print("No temporary pots available!")
        return None

def update():
    global recipe_creation_time
    global recipe

    # recipe 생성 딜레이 체크
    if recipe_creation_time and time.time() - recipe_creation_time >= recipe_delay_duration:
        recipe_creation_time = None  # 타이머 초기화
        recipe = Recipe(random.randint(0, 3))  # 새로운 recipe 생성
        game_world.add_object(recipe, 9)  # game_world에 추가

    game_world.update(mouse_x, mouse_y)
    game_world.handle_collisions()
    game.update()
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

