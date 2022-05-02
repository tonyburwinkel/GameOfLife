'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains tests for the display module
'''

import unittest
from unittest import TestCase
import pygame

from config import Config
from game_logic import GameOfLife
from display import Display


class TestDisplay(TestCase):
    '''
    class: TestDisplay contains tests for the display class
    parameters: derived from unittest.TestCase
    returns: validated tests
    '''
    def test_rect_array(self):
        '''
        function: test rect array tests the make rect array function
        parameters: none
        returns: test validations
        '''
        pygame.init()
        game = GameOfLife(38,38)
        config = Config(game)
        display = Display(game, config)
        # make sure the rect array matches the game board
        self.assertEqual(len(display.rect_array), len(game.board))
        for i in range(len(display.rect_array)):
            self.assertEqual(len(display.rect_array[i]), len(game.board[i]))

    # all other tests for the display module have been done via manual testing and visual confirmation
    # since the functions in display update a pygame display, the way to test them is to play the game and make
    # sure the expected game behaviors are exhibited


if __name__ == "__main__":
    unittest.main()
