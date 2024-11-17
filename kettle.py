from pico2d import load_image, draw_rectangle
import game_world
import game_framework

class Kettle:
    def __init__(self):
        self.image = load_image('kettle_sprite_sheet.png')
        self.x, self.y = 840, 450
        self.ramen_x, self.ramen_y = 0, 0
        self.origin_x, self.origin_y = self.x, self.y
        self.bb_x, self.bb_y = 15, 15
        self.frame_x = 0
        self.isSelected = False
        self.isSelected2 = False
        self.OnRamen = False
        self.frame_num = 3
        self.width, self.height = 204, 220
        self.frame_duration = [50, 50, 50]  # 각 프레임에 대해 지속시간 설정 (첫 번째 프레임은 길게 설정)
        self.current_frame_time = 0  # 현재 프레임이 얼마나 지속됐는지 추적


    def draw(self):
        self.image.clip_composite_draw(
            self.frame_x * 204, 0, self.width, self.height,  # 잘라낼 스프라이트 영역
            0,  # 회전 각도
            '',  # 이미지의 대칭 변환 (''는 변환 없음)
            self.x, self.y,  # 그릴 위치 (x, y)
            self.width, self.height  # 그릴 크기 (width, height)
        )
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
        return self.x - self.bb_x - 75, self.y - self.bb_y, self.x + self.bb_x - 75, self.y + self.bb_y

    def check(self, click_x, click_y):
        # 메뉴 영역 클릭 여부 확인
        self.isSelected = (self.origin_x - self.width // 2 <= click_x <= self.origin_x + self.width // 2 and
                           self.origin_y - self.height // 2 <= click_y <= self.origin_y + self.height // 2)

        # 냄비 위에 있는 경우 두 번째 클릭으로 고정
        if self.OnRamen:
            self.isSelected2 = True  # 고정 상태 활성화
        elif not self.OnRamen:
            self.isSelected2 = False  # 냄비 위가 아니면 초기화

    def check_mouseUp(self, up_x, up_y):
        if self.OnRamen:
            pass
        else:
            pass

    def update(self, mouse_x, mouse_y):
        if self.isSelected2:  # 냄비 위에서 고정된 상태
            self.x = self.ramen_x
            self.y = self.ramen_y

            self.current_frame_time += 1

            # 첫 번째 프레임을 길게 표시한 후 나머지 프레임만 반복
            if self.current_frame_time >= self.frame_duration[self.frame_x]:
                # 첫 번째 프레임 이후, 2번째와 3번째 프레임만 반복
                if self.frame_x == 0:
                    self.frame_x = 1  # 첫 번째 프레임에서 두 번째로 이동
                else:
                    self.frame_x = 1 + (self.frame_x - 1 + 1) % (self.frame_num - 1)

                self.current_frame_time = 0  # 지속 시간 초기화

        elif self.isSelected:  # 마우스로 드래그 중인 상태
            self.x = mouse_x
            self.y = mouse_y
        else:  # 원래 자리로 복귀
            self.x = self.origin_x
            self.y = self.origin_y
        pass

    def handle_collision(self, group, other):
        if group == 'pot:kettle' and not self.isSelected2:
            self.OnRamen = True
            self.ramen_x, self.ramen_y = other.x + 90, other.y + 70 # 냄비의 좌표를 저장
        elif not self.isSelected2:
            self.OnRamen = False
        pass