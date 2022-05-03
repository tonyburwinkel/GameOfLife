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

    def test_update_clicked(self):
        '''
        function: test rect array tests the make rect array function
        parameters: none
        returns: test validations
        '''
        pygame.init()
        game = GameOfLife(1,1) # make a game with one cell we can test
        config = Config(game)
        display = Display(game, config)

        self.assertEqual(game.board[0][0],0) # check the board to make sure our starting value is 0
        display.update_clicked((15,115)) # fake a click inside the cell
        self.assertEqual(game.board[0][0],1) # make sure the corresponding board value changed
        display.update_clicked((15,115)) # fake another click
        self.assertEqual(game.board[0][0],0) # make sure the board value changed back
        display.update_clicked((15,15)) # fake another click this time outside of the cell
        self.assertEqual(game.board[0][0],0) # make sure the board value stayed the same

    # all other tests for the display module have been done via manual testing and visual confirmation
    # since the functions in display update a pygame display, the way to test them is to play the game and make
    # sure the expected game behaviors are exhibited

    # special care has been taken to test the config module, which contains all assets and settings to
    # be rendered by display. Any invalid changes made to these will be caught by test_config


if __name__ == "__main__":
    unittest.main()
