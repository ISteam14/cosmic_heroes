import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Statistic
from scores import Scores
import time


def start_game():

    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Cosmic Heroes")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Statistic()
    sc = Scores(screen, stats)
    game_running = True

    while game_running:
        this_round_begin = int(round(time.time() * 1000))
        this_round_end = int(round(time.time() * 1000))
        if this_round_end - this_round_begin <= 4:
            time.sleep(0.0009 * (4 - (this_round_end - this_round_begin)))

        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen,sc, gun, inos, bullets)
