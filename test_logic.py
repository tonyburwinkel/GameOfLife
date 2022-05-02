'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains tests for the game logic of conway's game of life
'''

import unittest
from unittest import TestCase

from game_logic import GameOfLife

class TestLogic(TestCase):
    '''
    class: Test Logic contains tests for the game logic module of conway's game of life
    parameters: derived from unittest(TestCase)
    returns: validated tests for GameOfLife class and methods
    '''

    def test_make_board(self):
        '''
        function: test make board tests to make sure the make board function is operating withing
                specified parameters
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(10,10) # make a game with 10 rows and columns
        self.assertEqual(len(game.board),10) # make sure the game board has 10 rows
        for row in game.board: # loop through each row
            self.assertEqual(len(row),10) # make sure each row has 10 cells
            for cell in row: # loop through each cell
                self.assertTrue(isinstance(cell, int)) # make sure each cell is an integer
                self.assertEqual(cell, 0) # make sure each cell is set to 0

    def test_get_neighbors(self):
        '''
        function: test get neighbors tests the get neighbors function by creating a board with known
                neighbor values and seeing if the function returns the correct sums for certain cells
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(5, 5) # make a game with 5 rows and columns
        game.board = [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                ]
        # 1st test shows that circular buffer trick is working and the board
        # wraps around on itself. upper left corner should have 3 live neighbors - the other corners
        self.assertEqual(game.get_neighbors([0,0]), 3)
        # check a few more cells for neighbor values
        self.assertEqual(game.get_neighbors([1,2]), 3)
        self.assertEqual(game.get_neighbors([2,2]), 2)
        self.assertEqual(game.get_neighbors([4,2]), 0)

        game = GameOfLife(3, 3) # make a game with 3 rows and columns
        # the next 8 tests provide obvious proof of get_neighbors efficacy
        # we will set the game board manually, increasing the number of neighbors that the
        # center cell has to the maximum, and checking the result of get neighbors each time
        game.board = [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 1)

        game.board = [
                [1, 1, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 2)

        game.board = [
                [1, 1, 1],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 3)

        game.board = [
                [1, 1, 1],
                [1, 0, 0],
                [0, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 4)

        game.board = [
                [1, 1, 1],
                [1, 0, 1],
                [0, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 5)

        game.board = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 0, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 6)

        game.board = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 7)

        game.board = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
                ]
        self.assertEqual(game.get_neighbors([1,1]), 8)

    def test_update_cell(self):
        '''
        function: test update cell tests all possible configurations for the update cell function
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(1, 1) # make a game

        # test if update_cell follows the rules

        # tests for a living cell - should die with less than 2 or more than 3 neighbors
        # should continue living with 2 or 3 living neighbors
        self.assertEqual(game.update_cell(1,1),0)
        self.assertEqual(game.update_cell(1,2),1)
        self.assertEqual(game.update_cell(1,3),1)
        self.assertEqual(game.update_cell(1,4),0)
        self.assertEqual(game.update_cell(1,5),0)
        self.assertEqual(game.update_cell(1,6),0)
        self.assertEqual(game.update_cell(1,7),0)
        self.assertEqual(game.update_cell(1,8),0)

        # tests for dead cell - should only come alive if it has 3 living neighbors
        self.assertEqual(game.update_cell(0,1),0)
        self.assertEqual(game.update_cell(0,2),0)
        self.assertEqual(game.update_cell(0,3),1)
        self.assertEqual(game.update_cell(0,4),0)
        self.assertEqual(game.update_cell(0,5),0)
        self.assertEqual(game.update_cell(0,6),0)
        self.assertEqual(game.update_cell(0,7),0)
        self.assertEqual(game.update_cell(0,8),0)

    def test_update_board(self):
        '''
        function: test update board tests the update board function by giving it a known pattern and
                seeing if the predicted one emerges
        parameters: none
        returns: validated tests
        '''

        game = GameOfLife(4, 4) # make a game with 4 rows and columns

        # we know this pattern should stabilize into a box of 4 cells
        game.board = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                ]
        game.board = game.update_board()
        self.assertEqual(game.board,
                [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                ])
        # this state should stay no matter how many times we update
        for i in range(10):
            game.board = game.update_board()
        game.board = [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                ]

    def test_play_one(self):
        '''
        function: test play one round tests the play one round function by checking to see if the pinwheel
                pattern predicted by conway's rules emerges
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(4, 4) # make a game with 4 rows and columns
        # this test tests the pinwheel shape, which should repeat endlessly
        # set the board to the vertical bar
        game.board = [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                ]
        # update the board and see if the horizontal bar has emerged
        game.play_one_round()
        self.assertEqual(game.board,
                [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                ])
        # see if updating the board 10 times produces the same pattern
        for i in range(11):
            game.play_one_round()

        self.assertEqual(game.board,
                [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                ])

    def test_go_back_one(self):
        '''
        function: test go back one tests the go back one round function by checking to see if the pinwheel
                also runs backwards
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(5, 5) # make a game with 4 rows and columns
        # this test tests the pentomino shape, which should change many times before stabilizing
        # set the board to the pentomino
        game.board = [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                ]
        # play 50 rounds and then go back 50 rounds
        for i in range(50):
            game.play_one_round()
        for i in range(50):
            game.go_back_one_round()
        # see if we get the pentomino back
        self.assertEqual(game.board,
                [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                ])

    def test_reset(self):
        '''
        function: test reset checks to see if the reset function works
        parameters: none
        returns: validated tests
        '''
        game = GameOfLife(5, 5) # make a game with 5 rows and columns
        # make the pentomino
        game.board = [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                ]
        # play 50 rounds and then reset
        for i in range(50):
            game.play_one_round()
            game.reset()
        # see if we get the pentomino back
        self.assertEqual(game.board,
                [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                ])
        self.assertEqual(game.frame_stack.pop(),0)

if __name__ == "__main__":
    unittest.main()
