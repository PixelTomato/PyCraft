from pygame import freetype
import pygame
from pygame import Vector2

freetype.init()
pygame.font.init()

FONT_PATH = "assets/fonts/minecraft_font.ttf"

font = pygame.font.Font


def set_font(font_name, size):
	global font
	font = pygame.font.Font(font_name, size)


set_font("assets\\fonts\\minecraft_font.ttf", 16)


def draw(surface, position, text, antialias=False, color=(255, 255, 255), shadow=True):
	if shadow:
		draw(surface, (Vector2(position) + Vector2(2, 2)), text, color=(0, 0, 0), shadow=False)
	text_surface = font.render(text, antialias, color)
	surface.blit(text_surface, position)
