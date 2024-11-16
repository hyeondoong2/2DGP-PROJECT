from pico2d import load_image, draw_rectangle

class Powder:
    def __init__(self):
        self.image = load_image('powder.png')
        self.x, self.y = 270, 830
        self.origin_x, self.origin_y = self.x, self.y
        self.frame_x = 0
        self.width, self.height = 91, 83
        self.isActive = False
        self.isSelected = False
        self.bb_x, self.bb_y = 100, 60
        self.frame_duration = [50, 50]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        self.image.clip_composite_draw(
            self.frame_x * 1000, 0, self.width, self.height,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
        return self.x - self.bb_x, self.y - self.bb_y, self.x + self.bb_x, self.y + self.bb_y

    def check(self, click_x, click_y):
        # 마우스가 메뉴 영역에 들어갔는지 확인
        self.isSelected = (self.origin_x - self.width // 2 <= click_x <= self.origin_x + self.width // 2 and
                           self.origin_y - self.height // 2 <= click_y <= self.origin_y + self.height // 2)

        if self.isSelected:
            self.bb_x, self.bb_y = 40, 20
        else:
            self.bb_x, self.bb_y = 100, 60

    def update(self, mouse_x, mouse_y):
        if self.isSelected:
            self.x = mouse_x
            self.y = mouse_y
        else:
            self.x = self.origin_x
            self.y = self.origin_y

        pass
