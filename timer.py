import random
from pico2d import load_image, load_font, get_time
import time

import play_mode


class Timer:
    def __init__(self):
        self.time1 = load_image("resources/time_bar1.png")  # 배경 이미지
        self.time2 = load_image("resources/time_bar2.png")  # 시간 표시 이미지
        self.time = 30  # 초기 시간 설정
        self.max_time = 30  # 최대 시간 (60초)
        self.previous_time = get_time()

    def draw(self):
        # 배경 시간바 그리기
        self.time1.clip_composite_draw(
            0, 0, 452, 28,
            0, '', 960, 630,
            452, 28
        )

        # 시간에 따라 time2의 크기 조정
        time_width = (self.time / self.max_time) * 429
        draw_position_x = 960 - (429 / 2) + (time_width / 2)

        self.time2.clip_composite_draw(
            0, 0, int(time_width), 14,
            0, '', draw_position_x, 630,
            int(time_width), 14
        )

    def check(self, x, y):
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def update(self, mouse_x, mouse_y):
        current_time = get_time()
        delta_time = current_time - self.previous_time
        self.previous_time = current_time

        if self.time > 0:
            self.time -= delta_time
            if self.time < 0:
                self.time = 0
                play_mode.TIME_OUT = True

    def reset(self):
        self.time = self.max_time
        self.previous_time = time.time()
