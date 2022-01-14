import pygame
import os
from pathlib import Path
from constants import TILE_SIZE

texture_list = []
texture_index = []
other_textures = {}


def reload():
	global texture_list
	global texture_index
	global other_textures

	texture_list.clear()
	texture_index.clear()

	for file in os.listdir(Path("assets/textures/blocks")):
		texture_list.append(
			pygame.transform.scale(
				pygame.image.load(os.path.join(Path("assets/textures/blocks"), file)),
				(TILE_SIZE, TILE_SIZE)
			)
		)

		texture_index.append(
			str(file).removesuffix(".png")
		)

	other_textures["outline"] = pygame.transform.scale(
		pygame.image.load(Path("assets/textures/other/outline.png")),
		(TILE_SIZE, TILE_SIZE)
	)
