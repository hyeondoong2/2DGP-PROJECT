from pico2d import load_image, draw_rectangle
import game_world

class Water:
    def __init__(self, x, y, powder):
        self.powder = powder
        self.image1 = load_image('water_sprite_sheet.png')
        self.image2 = load_image('water_sprite_sheet2.png')
        self.x, self.y = x, y + 20
        self.origin_x, self.origin_y =  x, y + 20
        self.frame_x = 0
        self.image_width, self.image_height = 114, 89
        self.bb_x, self.bb_y = 30, 30
        self.width, self.height = 114, 89
        self.frame_num = 14
        self.isBurning = False
        self.frame_duration = [100, 100, 100, 3300, 200, 200, 200, 200, 200, 200, 200, 200, 200, 100, 100, 100]  # 각 프레임에 대해 지속시간 설정
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        if self.powder:
            self.image2.clip_composite_draw(
                self.frame_x * self.image_width, 0, self.image_width, self.image_height,  # 잘라낼 스프라이트 영역
                0,  # 회전 각도
                '',  # 이미지의 대칭 변환 (''는 변환 없음)
                self.x, self.y,  # 그릴 위치 (x, y)
                self.width + 10, self.height + 10  # 그릴 크기 (width, height)
            )
        else:
            self.image1.clip_composite_draw(
                self.frame_x * self.image_width, 0, self.image_width, self.image_height,  # 잘라낼 스프라이트 영역
                0,  # 회전 각도
                '',  # 이미지의 대칭 변환 (''는 변환 없음)
                self.x, self.y,  # 그릴 위치 (x, y)
                self.width + 10, self.height + 10  # 그릴 크기 (width, height)
            )

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
        return self.x - self.bb_x, self.y - self.bb_y + 20, self.x + self.bb_x, self.y + self.bb_y + 20

    def check(self, click_x, click_y):
        pass

    def update(self, mouse_x, mouse_y):
        self.current_frame_time += 1

        # 첫 번째 프레임을 길게 표시한 후 나머지 프레임만 반복
        if self.current_frame_time >= self.frame_duration[self.frame_x]:

            # 마지막 프레임인지 확인
            if self.frame_x < self.frame_num - 1:
                self.frame_x = 1 + (self.frame_x - 1 + 1) % (self.frame_num - 1)
            else:
                # print('Reached the last frame')  # 디버그용 출력
                pass


            if self.frame_x == 7 or self.frame_x == 9 or self.frame_x == 10:
                self.y = self.origin_y - 8
            else:
                self.y = self.origin_y

            self.current_frame_time = 0  # 지속 시간 초기화
        pass

    def check_mouseUp(self, up_x, up_y):
        pass

    def handle_collision(self, group, other):
        pass

