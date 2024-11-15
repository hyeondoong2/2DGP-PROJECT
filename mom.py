from pico2d import *

class Mom:
    def __init__(self):
        self.mama_image = load_image('mama.png')
        self.mama_angry_image = load_image('mama_angry.png')
        self.mama_happy_image = load_image('mama_happy.png')
        self.frame_x = 0
        self.x, self.y = 1280, 300  # 중심 좌표
        self.width, self.height = 800, 700 # 크기
        self.frame_duration = [1000, 5, 5, 5]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적

    def draw(self):
        self.mama_image.clip_composite_draw(
            self.frame_x * 600, 0, 600, 500,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y + 30,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )

    def update(self):
        self.current_frame_time += 1

        # 첫 번째 프레임을 길게 표시하기 위해
        if self.current_frame_time >= self.frame_duration[self.frame_x]:
            self.frame_x = (self.frame_x + 1) % 4  # 4개 프레임을 반복
            self.current_frame_time = 0  # 시간 초기화

