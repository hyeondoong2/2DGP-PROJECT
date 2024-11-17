from pico2d import load_image, draw_rectangle
import game_world

class Pot:
    def __init__(self, x, y, burning):
        self.image = load_image('pot.png')
        self.x, self.y = x, y
        self.origin_x, self.origin_y = x, y
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.bb_x, self.bb_y = 70, 30
        self.width, self.height = 181, 118
        self.price = 0
        self.water = False
        self.egg = False
        self.noodle = False
        self.powder = False
        self.spring_onion = False
        self.isBurnt = burning
        self.isSelected = False
        self.frame_duration = [50, 50]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        self.image.clip_composite_draw(
            self.frame_x * 1000, 0, self.image_width, self.image_height,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
        return self.x - self.bb_x, self.y - self.bb_y + 20, self.x + self.bb_x, self.y + self.bb_y + 20

    def check(self, click_x, click_y):
        # 마우스가 메뉴 영역에 들어갔는지 확인
        if self.isBurnt:
            self.isSelected = (self.origin_x - self.width // 2 <= click_x <= self.origin_x + self.width // 2 and
                               self.origin_y - self.height // 2 <= click_y <= self.origin_y + self.height // 2)


    def update(self, mouse_x, mouse_y):
        if self.isSelected:
            pass
        else:
            self.x = self.origin_x
            self.y = self.origin_y

        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def handle_collision(self, group, other):
        if group == 'pot:egg':
            self.egg = True
            pass
        elif group == 'pot:noodle':
            self.noodle = True
            pass
        elif group == 'pot:springOnion':
            self.spring_onion = True
            pass
        elif group == 'pot:powder':
            self.powder = True
            pass
        elif group == 'pot:kettle':
            self.water = True
            pass