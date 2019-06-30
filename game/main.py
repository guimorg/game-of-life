import pygame

from math import floor

"""
    ~ ~ ~ GAME CONSTANTS ~ ~ ~
    PYGAME use tuples to assign colot values (RGB)
"""

BORDER = (0, 0, 0)  # black
BACKGROUND = (255, 255, 255)  # white

"""
    ~ ~ ~ SETUP ~ ~ ~
    Setting Up Pygame
"""

pygame.init()
width, height = 800, 800  # Maybe change this?
size = (width, height)
screen = pygame.display.set_mode(size)  # Setting up Screen Size
pygame.display.set_caption("Conway's Life Game")
font = pygame.font.SysFont("monospace", 20)

"""
    ~ ~ ~ FUNCTIONS ~ ~ ~
"""


def draw(
    grid_width: int,
    grid_height: int,
    tile_width: int,
    tile_height: int
):
    """
        Drawing grid.

        grid_width (int): Width Dimention
        grid_height (int): Height Dimention
        tile_width (int): Tile Width Dimention
        tile_height (int): Tile Height Dimention

    """
    for i in range(0, grid_width):
        for j in range(0, grid_width):
            pygame.draw.rect(
                screen,
                BORDER,
                (i * tile_width, j * tile_height, tile_width, tile_height),
                1  # Border's Width
            )

    label = font.render("This is the label!", 1, BORDER)
    screen.blit(label, (20, height - 30))  # Hardcoded - Maybe change this?


def clear_screen():
    """
        Clearing the screen with background colour.
    """
    screen.fill(BACKGROUND)


"""
    ~ ~ ~ VARIABLES ~ ~ ~
"""

done = False
clock = pygame.time.Clock()


"""
    ~ ~ ~ VARIABLES ~ ~ ~
"""

while not done:

    grid_width, grid_height = 50, 50
    tile_width, tile_height = round(width / grid_width), round((height - 50) / grid_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            target_x = int(floor(pos[0] / tile_width))
            target_y = int(floor(pos[1] / tile_height))
            print(f'{target_x},{target_y}')

    clear_screen()

    draw(
        grid_width,
        grid_height,
        tile_width,
        tile_height
    )

    pygame.display.flip()  # Update

    clock.tick(30)

pygame.quit()
