import random
import pygame
from Ant import Ant

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
DONE = False
PAUSE = False
terrain = None

# test_ants = [Ant(
#                200,
#                200,
#                screen,
#                terrain,
#                color = (
#                    random.randint(0, 255),
#                    random.randint(0, 255),
#                    random.randint(0, 255),))
#            for x in range(200)]

test_ant = Ant(200, 200, screen, terrain)


if __name__ == "__main__":
    while not DONE:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSE = not PAUSE
                if event.key == pygame.K_ESCAPE:
                    DONE = True

        if not PAUSE:

            mousex, mousey = pygame.mouse.get_pos()
            test_ant.test_force[0] = mousex - test_ant.position[0]
            test_ant.test_force[1] = mousey - test_ant.position[1]
            screen.fill((0,0,0))
            test_ant.update()
            test_ant.show()
            test_ant.debug()
#            for ant in test_ants:
#                ant.move(random.randint(-1,1), random.randint(-1,1))
#                # ant.debug()
#                ant.show()

            pygame.display.flip()
            clock.tick(20)

