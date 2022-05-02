'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains tests for the config class
'''

import unittest
from unittest import TestCase
import pygame

from config import Config
from game_logic import GameOfLife

class TestConfig(TestCase):
    '''
    class: test config contains tests for the config class
    parameters: derived from unittest.TestCase
    returns: validated tests for config class
    '''

    def make_config(self):
        '''
        function: make config quickly makes a display config for testing
        parameters: none
        returns: game config, running instance of pygame (as sideeffect)
        '''
        game = GameOfLife(38,38) # make a game instance to hand to the config
        config = Config(game) # make a display config
        return config

    def test_colors(self):
        '''
        function: test colors tests all colors in the colors dictionary
        parameters: none
        returns: test validations for config colors
        '''
        pygame.init() # make an instance of pygame for all the text and rect objects
        config = self.make_config()
        colors = config.colors

        for rgb in colors.values():
            self.assertEqual(len(rgb),3) # make sure every color value is 3 items long
            for num in rgb:
                self.assertTrue(len(str(num))<=3) # make sure each one is less than 3 characters
                self.assertTrue(len(str(num))>=1) # make sure each one is at least one character
                self.assertTrue(isinstance(num, int)) # make sure all values are integers

    def test_text(self):
        '''
        function: test text tests all the text objects to be rendered to the display
        parameters: none
        returns: validated tests for screen text object configurations
        '''
        config = self.make_config()
        text = config.display_text

        # make sure both our font objects are pygame font object type
        self.assertTrue(isinstance(config.font, pygame.font.Font))
        self.assertTrue(isinstance(config.counter_font, pygame.font.Font))

        for text_object in text.values():
            self.assertTrue(isinstance(text_object["location"], tuple)) # make sure locations are tuples
            self.assertTrue(isinstance(text_object["location"][0], int)) # make sure tuple is integers
            self.assertTrue(isinstance(text_object["location"][1], int))

    def test_bg(self):
        '''
        function: test bg tests all the background rectangles for the game display
        parameters: none
        returns: validated tests for rectangle configurations in config object
        '''
        pygame.init() # make an instance of pygame for all the text and rect objects
        config = self.make_config()

        bg = config.background
        for bg in bg.values():
            self.assertTrue(isinstance(bg["location"], pygame.Rect)) # make sure all locations are valid rect objects
            self.assertTrue(isinstance(bg["color"], tuple)) # make sure all colors are valid
            self.assertTrue(bg["color"] in config.colors.values()) # make sure all colors are in colors dict

    def test_buttons(self):
        '''
        function: test buttons tests all the background rectangles for the game display
        parameters: none
        returns: validated tests for rectangle configurations in config object
        '''
        pygame.init() # make an instance of pygame for all the text and rect objects
        config = self.make_config()

        buttons = config.buttons
        for button in buttons.values():
            self.assertTrue(isinstance(button["location"], pygame.Rect)) # make sure all locations are valid rect objects

            self.assertTrue(isinstance(button["color"], tuple)) # make sure all colors are valid
            self.assertTrue(button["color"] in config.colors.values()) # make sure all colors are in colors dict



if __name__ == "__main__":
    unittest.main()
