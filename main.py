import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario
import re

windowSize = (640,480)
def main():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)
    pygame.display.set_caption("Super Dogeee??")
    programIcon = pygame.image.load('img/doge.png')
    pygame.display.set_icon(programIcon)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    level.mario = mario
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption("Super Dogeee?? running at {:d} FPS".format(int(clock.get_fps())))
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    main()


if __name__ == "__main__":
    main()
