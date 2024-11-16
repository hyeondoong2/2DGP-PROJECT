from pico2d import load_image

class Pot:
    def __init__(self, x, y, size):
        self.image = load_image('pot.png')
        self.x, self.y = x, y
        self.frame_x = 0
        self.image_width, self.image_height = 181, 118
        self.width, self.height = 181 * size, 118 * size
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

    def update(self):
        pass
