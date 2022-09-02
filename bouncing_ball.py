import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
BALL_COLOUR = Colour(red=255, green=253, blue=65)

BALL_RADIUS = 20

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()

        clock.tick(60)

main()