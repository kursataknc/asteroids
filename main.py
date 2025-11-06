import pygame
from constants import *
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # --- Groups ---
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    # Tell Player which groups it should auto-join via CircleShape.__init__
    Player.containers = (updatable, drawable)

    # Instantiate the player (auto-added to both groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        # Update all updatables (Pygame forwards args to each sprite.update)
        updatable.update(dt)


        # Draw phase
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000  # Limit to 60 FPS


if __name__ == "__main__":
    main()