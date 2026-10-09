# song loader
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Matrices-animation/media/credits.mp3")
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)