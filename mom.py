from pico2d import *

class Mom:
    def __init__(self, state):
        self.mama_image = load_image('resources/mama.png')
        self.mama_angry_image = load_image('resources/mama_angry.png')
        self.mama_happy_image = load_image('resources/mama_happy.png')
        self.frame_x = 0
        self.state = state
        self.x, self.y = 1280, 300  # 중심 좌표
        self.width, self.height = 800, 700 # 크기
        self.frame_num = 4
        self.frame_num2 = 2
        self.frame_duration1 = [1000, 10, 10, 10]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.frame_duration2 = [40, 40, 40, 40]
        self.frame_duration3 = [40, 40]
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적

    def draw(self):
        if self.state == 'mama' :
            self.mama_image.clip_composite_draw(
                self.frame_x * 600, 0, 600, 500,  # 잘라낼 스프라이트 영역
                0,  # 회전 각도
                '',  # 이미지의 대칭 변환 (''는 변환 없음)
                self.x, self.y + 30,  # 그릴 위치 (x, y)
                600 * 1.4, 500 * 1.4  # 그릴 크기 (width, height)
            )
        elif self.state =='angry' :
            self.mama_angry_image.clip_composite_draw(
                self.frame_x * 380, 0, 380, 500 ,  # 잘라낼 스프라이트 영역
                0,  # 회전 각도
                '',  # 이미지의 대칭 변환 (''는 변환 없음)
                self.x, self.y + 30,  # 그릴 위치 (x, y)
                380 * 1.5, 500 * 1.5  # 그릴 크기 (width, height)
            )
            pass
        elif self.state =='happy' :
            self.mama_happy_image.clip_composite_draw(
                self.frame_x * 388, 0, 388, 500,  # 잘라낼 스프라이트 영역
                0,  # 회전 각도
                '',  # 이미지의 대칭 변환 (''는 변환 없음)
                self.x, self.y + 30,  # 그릴 위치 (x, y)
                388 * 1.6, 500 * 1.6  # 그릴 크기 (width, height)
            )
            pass

    def update(self):
        self.current_frame_time += 1

        if self.state == 'mama' :
            # 첫 번째 프레임을 길게 표시하기 위해
            if self.current_frame_time >= self.frame_duration1[self.frame_x]:
                self.frame_x = (self.frame_x + 1) % self.frame_num  # 4개 프레임을 반복
                self.current_frame_time = 0  # 시간 초기화
        elif self.state =='angry':
            if self.current_frame_time >= self.frame_duration2[self.frame_x]:
                self.frame_x = (self.frame_x + 1) % self.frame_num  # 4개 프레임을 반복
                self.current_frame_time = 0  # 시간 초기화
            pass
        elif self.state == 'happy':
            if self.current_frame_time >= self.frame_duration3[self.frame_x]:
                self.frame_x = (self.frame_x + 1) % self.frame_num2  # 2개 프레임을 반복
                self.current_frame_time = 0  # 시간 초기화
            pass


