'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains configurations for the game of life display module. The main purpose of this module
is to declutter the display module. All pygame rectangles to be rendered (besides the game board) as well as text
to be rendered, are stored here in dictionaries. The (r,g,b) color set for the game is also stored here.
'''

import pygame
from pygame.locals import *

class Config:
    def __init__(self, game):
        '''
        class: Config
        parameters: instance of Conway's Game of Life
        returns: object containing configurations for pygame display
        '''
        self.game = game
        self.window_width = 798
        self.window_height = 1000
        self.font = pygame.font.SysFont(None,84) # font setting for text
        self.counter_font = pygame.font.SysFont(None,64) # font for counter

        self.colors = {
            # VAPORWAVE COLORS OOH!
            "PINK" : (233,52,121),
            "DARK" : (48, 3, 80),
            "PURPLE" : (148, 22, 127),
            "YELLOW" : (249, 172, 83),
            "BLUE" : (21, 60, 180),
            "GREEN" : (119, 173, 149),
            "BLACK" : (0, 0, 0),
            "WHITE" : (200, 200, 200)
                }

        '''
        to render text, pygame creates text objects with a call to a font object's render function
        in the below dictionary, i outline all the parameters for blitting text to the screen as values
        paired with a descriptive key. the text key contains the render call's value, and the location contains
        the tuple that pygame's screen.blit function will use to locate the text object's upper left corner
        '''
        self.display_text = {
            # TEXT OBJECTS TO BE BLITTED OVER DISPLAY
            "start_text":   {
                "text" : self.font.render('start', True, self.colors["DARK"]),
                "location" : (35,920)
                },
            "stop_text":    {
                "text" : self.font.render('stop', True, self.colors["DARK"]),
                "location" : (240,920)
                },
            "step_l_text":  {
                "text" : self.font.render('<<', True, self.colors["WHITE"]),
                "location" : (425,920)
                },
            "step_r_text":  {
                "text" : self.font.render('>>', True, self.colors["WHITE"]),
                "location" : (515,920)
                },
            "clear_text":   {
                "text" : self.font.render('clear', True, self.colors["WHITE"]),
                "location" : (625,920)
                },
            "banner_text":  {
                "text" : self.font.render("Conway's Game of Life", True, self.colors["BLACK"]),
                "location" : (5,25)
                },
            "counter_text":  {
                "text": self.counter_font.render(f"{str(self.game.step_count)}", True, self.colors["BLACK"]),
                "location": (670,30)
                }
            }

        '''
        the following section contains two dictionaries that describe rectangles that will be passed to pygame's
        draw module to be rendered to the display. each key is a rectangle, and each value set is a dictionary
        containing the color configuration of the rectangle and the pygame rect object that describes its
        location and dimensions. a rendering loop in the display module will take every rectangle in these two
        dictionaries and render them according to the rect and color settings listed here.
        '''

            # RECT OBJECTS THAT MAKE UP THE DISPLAY BACKGROUND
        self.background = {
            "banner_rect" :{
                "color": self.colors["BLUE"],
                "location": pygame.Rect(0,0,800,100)
                },
            "counter_rect" :{
                "color": self.colors["BLACK"],
                "location": pygame.Rect(665,10,125,80)
                },
            "grid_rect" :{
                "color": self.colors["BLACK"],
                "location": pygame.Rect(0,100,900,800)
                },
            "controls_rect" :{
                "color": self.colors["BLUE"],
                "location": pygame.Rect(0,900,800,100)
                },
            }

            # RECT OBJECTS THAT ARE CLICKABLE BUTTONS
        self.buttons = {
            "start_button" : {
                "color": self.colors["GREEN"],
                "location": pygame.Rect(10,910,180,80)
                },
            "stop_button" : {
                "color": self.colors["PINK"],
                "location": pygame.Rect(210,910,180,80)
                },
            "step_l_button" : {
                "color": self.colors["BLACK"],
                "location": pygame.Rect(410,910,89,80)
                },
            "step_r_button" : {
                "color": self.colors["BLACK"],
                "location": pygame.Rect(500,910,89,80)
                },
            "clear_button": {
                "color": self.colors["DARK"],
                "location": pygame.Rect(610,910,180,80)
                }
        }
