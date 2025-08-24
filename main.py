# import
import pygame
from constants import *
from player import Player

def main():
    # initialize all imported pygame modules
    pygame.init()
    
    # set GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # initialize a clock for fps calculations
    clock = pygame.time.Clock()
    dt = 0

    # create updatable and drawable groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # set both groups as containers for the Player
    Player.containers = (updatable, drawable)

    # instantiate (create instance of a class) a player object and spawn it in the middle of the screen
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # print starting messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # main game loop
    while True:

        # check if the user closed the window and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # use fill to fill the screen with a solid black color
        screen.fill("black")
        
        # update player movement before each frame
        updatable.update(dt)

        # re-render the player on the screen each frame
        for entity in drawable:
            entity.draw(screen)

        #use display.flip() to refresh
        pygame.display.flip()

        # limit the framerate to 60 FPS  
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
