import numpy
import pygame
from constants import CHUNK_SIZE
from constants import TILE_SIZE
from pygame import Vector2
from textures import texture_list


def build(data):
	layer_surface = pygame.Surface((TILE_SIZE * CHUNK_SIZE, TILE_SIZE * CHUNK_SIZE))
	for x in range(CHUNK_SIZE):
		for y in range(CHUNK_SIZE):
			for z in range(3):
				layer_surface.blit(texture_list[data[z][x][y]], Vector2(x, y) * TILE_SIZE)
	return layer_surface


def new(position):
	new_chunk_data = numpy.full((3, CHUNK_SIZE, CHUNK_SIZE), 0)
	for x in range(CHUNK_SIZE):
		for y in range(CHUNK_SIZE):
			for z in range(3):
				new_chunk_data[z][x][y] = 1
	return new_chunk_data
