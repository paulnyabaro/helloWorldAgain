import pygame
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)

pygame.init()

pygame.display.set_caption("Mousetracker")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    circle_position = (screen.get_width() // 2), (screen.get_height() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                circle_position = event.__dict__["pos"]

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, CIRCLE_COLOUR, circle_position, 20)
        pygame.display.update()

        clock.tick(60)

main()