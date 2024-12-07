from pico2d import *

class Fire:
    def __init__(self, x, y):
        self.image = load_image('resources/fire.png')
        self.x, self.y = x, y
        self.frame_x = 0
        self.width, self.height = 100, 100
        self.frame_duration = [100, 100]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        self.image.clip_composite_draw(
            self.frame_x * 1156, 0, 1156, 1000,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def update(self,x, y):
        self.current_frame_time += 1

        if self.current_frame_time >= self.frame_duration[self.frame_x]:
            self.frame_x = (self.frame_x + 1) % 2
            self.current_frame_time = 0  # 시간 초기화

        pass


    def handle_collision(self, group, other):
        # fill here
        pass
