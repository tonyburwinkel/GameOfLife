import pygame, sys
from pygame.locals import *
from display import Display
from game_logic import GameOfLife
from config import Config

def main():
    pygame.init()

    game = GameOfLife(38,38)
    config = Config(game)
    display = Display(game, config)
    buttons = display.buttons

    running = True # this variable will run the outer event loop
    playing = False # this variable will run the inner event loop

    # OUTER EVENT LOOP
    # this loop runs while we choose which cells to turn on and off
    # this is before the simulation begins
    while running == True:

        # EVENT LOOP
        for event in pygame.event.get(): # check pygame's event loop
            if event.type == KEYDOWN: # if a key gets pressed
                if event.key == K_ESCAPE: # if it's the escape key
                    pygame.quit() # quit the game
                    sys.exit()

        # MOUSE CLICK EVENTS
            elif event.type == pygame.MOUSEBUTTONUP: # if we click the screen
                mouse_pos = pygame.mouse.get_pos() # save where we clicked
                display.update_clicked(mouse_pos) # check all the squares in the game board & update if clicked

        # CLICKABLE BUTTON EVENTS - check if we clicked any buttons
                for button, props in buttons.items(): # loop through our buttons dictionary from config
                    if props["location"].collidepoint(mouse_pos): # check each rect to see if our mouse clicked it
                        if button == "start_button":
                            playing = True # if we clicked the start button, drop us into the inner event loop
                        if button == "step_l_button":
                            game.go_back_one_round() # if we click the left step button, go one board back
                        if button == "step_r_button":
                            game.play_one_round() # if we click step right button, go one board forward
                        if button == "clear_button":
                            game.reset() # if we push the clear button, reset the game

        display.update()

        # INNER EVENT LOOP, FOR RUNNING THE LIFE SIMULATION
        while playing == True:
            game.play_one_round() # have our game logic object update the cells
            display.update() # have the display object update the board and the counter
            pygame.time.wait(300) # wait in between frames, so we can see the changes

            # since we can no longer access the event triggers in the outer event loop, define some here
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        playing = False

                if event.type == pygame.MOUSEBUTTONUP: # if we click the screen
                    mouse_pos = pygame.mouse.get_pos() # save where we clicked
                    if buttons["stop_button"]["location"].collidepoint(mouse_pos): # see if that point is in stop button
                        playing = False # if it is, stop the simulation
                        # only the stop button works while playing is True, and we are in the inner event loop

if __name__ == "__main__":
    main()
