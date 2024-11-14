import pico2d
import play_mode as start_mode
import game_framework


pico2d.open_canvas(1600, 900)
game_framework.run(start_mode)
pico2d.close_canvas()