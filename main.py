import chunk
import pygame
import textures
import text
from pygame import Vector2
from math import floor
from constants import DISPLAY_SIZE
from constants import VERSION
from constants import TILE_SIZE

pygame.init()
textures.reload()

screen = pygame.display.set_mode(DISPLAY_SIZE, pygame.SCALED)
pygame.display.set_caption("PyCraft - pre-alpha-" + VERSION)
clock = pygame.time.Clock()
delta_time = 0

chunk_list = {}

new_chunk = chunk.build(
	chunk.new(Vector2(0, 0))
)

keys = list

available_tiles = ["stone", "stone_bricks", "dirt"]
selected_tile = 0
camera_position = Vector2(0, 0)
screen_camera_position = Vector2(0, 0)
raw_mouse_position = Vector2(0, 0)
mouse_position = Vector2(0, 0)


def player():
	global camera_position
	global raw_mouse_position
	global mouse_position
	global screen_camera_position
	global selected_tile

	if keys[pygame.K_w]:
		camera_position += Vector2(0, 0.01) * delta_time
	if keys[pygame.K_s]:
		camera_position -= Vector2(0, 0.01) * delta_time
	if keys[pygame.K_a]:
		camera_position -= Vector2(0.01, 0) * delta_time
	if keys[pygame.K_d]:
		camera_position += Vector2(0.01, 0) * delta_time
	if event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 4:
			selected_tile = max(selected_tile + 1, len(available_tiles))
		if event.button == 5:
			selected_tile = min(selected_tile - 1, 0)
		print(selected_tile)

	screen_camera_position = Vector2(-camera_position.x * TILE_SIZE, camera_position.y * TILE_SIZE)
	raw_mouse_position = Vector2(pygame.mouse.get_pos()) - screen_camera_position * 2
	mouse_position = Vector2(
		floor((raw_mouse_position.x + screen_camera_position.x) / TILE_SIZE),
		floor((raw_mouse_position.y + screen_camera_position.y) / TILE_SIZE)
	)


def draw_debug():
	text.draw(screen, Vector2(5, 5), "Camera: " + str(camera_position) + " Real: " + str(screen_camera_position))
	text.draw(screen, Vector2(5, 25), "FPS: " + str(round(clock.get_fps(), 2)))
	text.draw(screen, Vector2(5, 45), "Mouse: " + str(mouse_position) + " Real: " + str(raw_mouse_position))
	text.draw(screen, Vector2(5, 65), "Round Mouse: " + str(mouse_position))


def draw():
	screen.blit(new_chunk, screen_camera_position)
	screen.blit(textures.other_textures["outline"], screen_camera_position + mouse_position * TILE_SIZE)
	draw_debug()


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()

	screen.fill((0, 0, 0))
	player()
	draw()
	pygame.display.flip()
	delta_time = clock.tick()

pygame.quit()
exit(0)
