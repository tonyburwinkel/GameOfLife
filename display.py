'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains a display class for conway's game of life. The class renders an array of rectangles that is
created and updated in parallel with the game board from the logic class.
'''

from pygame.locals import *
import pygame

class Display:
    '''
    class: Display
    parameters: game of life object, config object, buttons object
    returns: display object for rendering to pygame display
    '''
    def __init__(self, game, config):
        self.config = config
        self.screen = pygame.display.set_mode((self.config.window_width, self.config.window_height))
        self.game = game
        self.rect_array = self.make_rect_array(20)
        # initialize the display settings in config object
        self.colors = self.config.colors
        self.display_text = self.config.display_text
        self.background = self.config.background
        self.buttons = self.config.buttons

    def make_rect_array(self, rect_size):
        '''
        function: make rect array makes a 2-d array of pygame rectangle objects to be rendered
        parameters: rows - int, cols - int, rect_size - int, # of pixels side of rectangle is
        returns: 2d array of rect objects
        '''
        game = self.game
        rect_array = []
        for x in range(game.rows):
            rect_array.append([])
            for y in range(game.cols):
                rect_array[-1].append(pygame.Rect(x*rect_size + x, y*rect_size+y+101, rect_size, rect_size))
        return rect_array

    def draw_frame(self):
        '''
        function: draw frame takes all rect objects that make
                up the display and has pygame's draw module draw them
                also blits text objects to the screen surface
        parameters: none
        returns: side-effects, rendered game of life display
        '''
        # DRAWING THE FRAME
        for backdrop in self.background.values():
            pygame.draw.rect(self.screen, backdrop["color"], backdrop["location"])

        for button in self.buttons.values():
            pygame.draw.rect(self.screen, button["color"], button["location"])

        for text in self.display_text.values():
            self.screen.blit(text["text"],text["location"])

    def draw_board(self):
        '''
        function: draw board uses the associative array structure to draw the rects in the rect array
                in yellow or dark depending on the state of the game board
        parameters: rect array - 2d array of rect objects
                    bool array - 2d array of bool objects
        returns: side-effects - renders rectangles in green or white to the pygame display object stored in screen
        '''
        for x in range(len(self.game.board)):
            for y in range(len(self.game.board[0])):
                if self.game.board[x][y] == 1:
                    pygame.draw.rect(self.screen, self.colors["YELLOW"], self.rect_array[x][y])
                else:
                    pygame.draw.rect(self.screen, self.colors["DARK"], self.rect_array[x][y])

    def update_clicked(self, mouse_pos):
        '''
        function: update clicked takes a clicked mouse position and checks to see if it is in one
                     of the rectangle objects of our game of life cell array. if it is, it toggles the
                    cell to its opposite state
        parameters: mouse_pos - int tuple - place the mouse clicked
                    rect_array - 2d array of the rectangle objects
                    bool_array - current state of our boolean data structure
        returns: side effects - changes state of bools array according to mouse clicks
        '''
        for x in range(len(self.rect_array)): # loop over a range matching the array width
            for y in range(len(self.rect_array[0])): # loop over a range matching the array height
                if self.rect_array[x][y].collidepoint(mouse_pos): # check each element in the board for clicked
                    print(mouse_pos, f"x:{x}, y:{y}") # print the mouse position clicked (debug)
                    if self.game.board[x][y] == 1: # if the cell we clicked was on, turn it off in the game board
                        self.game.board[x][y] = 0
                    else:
                        self.game.board[x][y] = 1 # otherwise, do the opposite

    def make_counter(self):
        '''
        function: make counter makes a text object dynamically based on the steps played
        parameters: step_count - int, from game variables
        returns: text object for rendering
        '''
        counter_font = pygame.font.SysFont(None,64) # font for counter
        counter_text = counter_font.render(f'{str(self.game.step_count)}',True, self.colors["YELLOW"])
        self.screen.blit(counter_text, (670,30))

    def update(self):
        '''
        function: update updates pygame display
        parameters: self
        returns: side effects, updates pygame display
        '''
        self.draw_frame()
        self.draw_board()
        self.make_counter()
        pygame.display.update() # this final call updates pygame's display object with all that we have drawn
