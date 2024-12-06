from pico2d import load_image, draw_rectangle

import game_world
import play_mode
from water import Water

class Pot:
    def __init__(self, x, y, boiling):
        self.image = load_image('resources/pot.png')
        self.x, self.y = x, y
        self.origin_x, self.origin_y = x, y
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.bb_x, self.bb_y = 50, 30
        self.move_bb_x, self.move_bb_y = 20, 10
        self.width, self.height = 181, 118
        self.price = 1000
        self.water = False
        self.egg = False
        self.noodle = False
        self.powder = False
        self.spring_onion = False
        self.isBoiling = boiling
        self.isCooked = False
        self.isSelected = False
        self.isSelected2 = False
        self.make_water = False
        self.isMoving = False
        self.isBurnt = False
        self.checkScore = False
        self.ingredients = []
        self.timer = 0
        self.frame_num = 5
        self.frame_duration = [2900, 80, 80, 80, 80]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        self.image.clip_composite_draw(
            self.frame_x * self.image_width, 0, self.image_width, self.image_height,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )
        #draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.get_move_bb())

    def get_bb(self):
        return self.x - self.bb_x, self.y - self.bb_y + 20, self.x + self.bb_x, self.y + self.bb_y + 20

    def get_move_bb(self):
        return (self.x - self.move_bb_x, self.y - self.move_bb_y - 60,
                self.x + self.move_bb_x, self.y + self.move_bb_y - 60)
        pass

    def attach_ingredient(self, ingredient):
        # 재료를 냄비에 추가
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            ingredient.attached_pot = self  # 재료에 냄비를 연결

    def detach_ingredient(self, ingredient):
        # 재료를 냄비에서 제거
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            ingredient.attached_pot = None  # 재료의 냄비 연결 해제

    def Initialize(self):
        self.x = self.origin_x
        self.y = self.origin_y
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.bb_x, self.bb_y = 50, 30
        self.move_bb_x, self.move_bb_y = 20, 10
        self.width, self.height = 181, 118
        self.price = 1000
        self.water = False
        self.egg = False
        self.noodle = False
        self.powder = False
        self.spring_onion = False
        self.isCooked = False
        self.isSelected = False
        self.isSelected2 = False
        self.make_water = False
        self.isMoving = False
        self.isBurnt = False
        self.checkScore = False
        self.ingredients = []
        self.timer = 0
        self.frame_num = 5
        self.frame_duration = [2900, 80, 80, 80, 80]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적
    pass

    def check(self, click_x, click_y):
        # 마우스가 영역에 들어갔는지 확인
        if self.isBoiling:
            self.isSelected = (self.origin_x - self.width // 2 <= click_x <= self.origin_x + self.width // 2 and
                               self.origin_y - self.height // 2 <= click_y <= self.origin_y + self.height // 2)

            left, bottom, right, top = self.get_move_bb()

            self.isSelected2 = left <= click_x <= right and bottom <= click_y <= top
        pass

    def update(self, mouse_x, mouse_y):
        if self.checkScore:
            self.x += 3
            if self.x > 1700 and self.isBurnt == False:
                self.Initialize()
            elif self.x > 1700 and self.isBurnt:
                pot = play_mode.get_temporary_pot()
                if pot:
                    pot.isBoiling = True
                    pot.x, pot.y = self.origin_x, self.origin_y
                    pot.origin_x, pot.origin_y = self.origin_x, self.origin_y

                    game_world.add_collision_pair('pot:egg', None, pot)
                    game_world.add_collision_pair('pot:powder', None, pot)
                    game_world.add_collision_pair('pot:noodle', None, pot)
                    game_world.add_collision_pair('pot:springOnion', None, pot)
                    game_world.add_collision_pair('pot:kettle', None, pot)
                    game_world.add_collision_pair('pot:tray', None, pot)
                    if pot.y == 510:
                        game_world.add_object(pot, 2)
                    else:
                        game_world.add_object(pot, 3)

                game_world.remove_object(self)


        else:
            if not self.make_water and self.water == True:
                water = Water(self.x, self.y, self.powder)
                game_world.add_object(water, 4)
                game_world.add_collision_pair('pot:water', water, None)
                game_world.add_collision_pair('pot:water', None, self)
                # print('makeWater')
                self.make_water = True

            if self.isMoving:  # 냄비가 움직이고 있으면
                self.x, self.y = mouse_x, mouse_y
                for ingredient in self.ingredients:  # 연결된 재료들도 함께 움직임
                    ingredient.x, ingredient.y = self.x, self.y

            if self.water and not self.isMoving:
                self.timer += 1

                if self.timer > 0:
                    self.current_frame_time += 1

                    # 첫 번째 프레임을 길게 표시한 후 나머지 프레임만 반복
                    if self.current_frame_time >= self.frame_duration[self.frame_x]:
                        # 마지막 프레임인지 확인
                        if self.frame_x < self.frame_num - 1:
                            self.frame_x = 1 + (self.frame_x - 1 + 1) % (self.frame_num - 1)
                        else:
                            # print('Reached the last frame')  # 디버그용 출력
                            pass

                        if self.frame_x > 1:
                            self.isBurnt = True

                        self.current_frame_time = 0  # 지속 시간 초기화

            if self.isSelected2:
                self.x, self.y = mouse_x, mouse_y
                for ingredient in self.ingredients:  # 연결된 재료들도 함께 움직임
                    ingredient.x, ingredient.y = self.x, self.y
                self.isMoving = True
            else:
                self.x = self.origin_x
                self.y = self.origin_y
                self.isMoving = False



        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def handle_collision(self, group, other):
        if group == 'pot:egg':
            if self.isMoving:
                other.isMoving = True
                pass
        elif group == 'pot:noodle' and other.attached_pot == self:
            if self.water:
                other.water = True
            pass
        elif group == 'pot:springOnion':
            pass
        elif group == 'pot:powder':
            pass
        elif group == 'pot:water':
            #print('water')
            if self.powder:
                other.powder = True
            else:
                other.powder = False

            if self.isMoving:
                other.isMoving = True
            else:
                other.isMoving = False
            pass
        elif group == 'pot:kettle' and other.water:
            self.water = True
            pass
        elif group == 'pot:tray':
            if self.checkScore == False:
                play_mode.check_score(self)
                other.move_right = True
                self.checkScore = True
            pass