# imports code from the open-source pygame library
import pygame

# import everything  from constants.py into main.py
from constants import *

def main():
    # initialize all imported pygame modules
    pygame.init()

    # set GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # print starting messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop
    while True:

        # check if the user closed the window and exit the game loop if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # use fill to fill the screen with a solid black color
        screen.fill((0,0,0))
        
        #use display.flip() to refresh - call this last!
        pygame.display.flip()



if __name__ == "__main__":
    main()
