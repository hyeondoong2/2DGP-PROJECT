import pico2d
import logo_mode as start_mode
import game_framework


pico2d.open_canvas()
game_framework.run(start_mode)
pico2d.close_canvas()
