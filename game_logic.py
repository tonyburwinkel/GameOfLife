'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains a game logic class. The class contains all relevant methods for making a game of life board
data structure, evaluating the next state from the current (playing conway's game), storing past states via a stack, and stepping forward and back in the game one board at a time.
'''

from pprint import pprint
from stack import Stack

class GameOfLife:
    '''
    class: game of life contains all game logic and game data structures
    parameters: rows - int number of rows of cells, cols - int number of columns of cells
    returns: instance of game of life to be rendered via the display module
    '''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.step_count = 0
        self.frame_stack = Stack(10000)
        self.board = self.make_board()

    def make_board(self):
        '''
        function: make board creates a data structure for our game data
        parameters: none, draws from self.rows and self.cols
        returns: boolean array - array of booleans representing cell values (all dead to start)
        '''
        bools = []
        for x in range(self.rows):
            bools.append([])
            for y in range(self.cols):
                bools[-1].append(0)
        return bools

    def get_neighbors(self, coords):
        '''
        function: get neighbors
        parameters: coords - array length 2, x and y of cell to find neighbors of
                    board - 2-d array of booleans representing the current state of the game
        returns: total value of neighbor cells - int 0 - 8
        '''
        board = self.board
        width = len(board[0])
        height = len(board)
        x = coords[0]
        y = coords[1]
        neighbors = [
                board[x-1][(y+1)%height],
                board[x][(y+1)%height],
                board[(x+1)%width][(y+1)%height],
                board[x-1][y],
                board[(x+1)%width][y],
                board[x-1][y-1],
                board[x][y-1],
                board[(x+1)%width][y-1],
                ]
        return sum(neighbors)

    def update_cell(self, cell_value, neighbors):
        '''
        function: update cell
        parameters: cell value - int (0-1), neighbors - int (0-8)
        returns: int 0-1 depending on rules of conway's game
        '''
        if cell_value == 1:
            if neighbors < 2:
                return 0
            elif 2 <= neighbors <= 3:
                return 1
            else:
                return 0
        else:
            if neighbors == 3:
                return 1
            else:
                return 0

    def update_board(self):
        '''
        function: update board
        parameters: board to be updated - 2-d array, list of lists of bools
        returns: updated board based on current board and conway's rules
        '''
        board = self.board.copy()
        new_board = [] # make an empty array to hold our new board
        width = len(board[0]) # make a width variable so we know how far to iterate
        height = len(board) # make a height variable so we know how far to iterate
        for x in range(width): # loop through each row in the board
            new_board.append([]) # add an empty list to be filled with updated values
            for y in range(height): # loop through indexes of each x position in y row
                cell_value = self.board[x][y] # take value in the current board at each x position in this row
                neighbors = self.get_neighbors([x,y]) # get the number of living neighbors this cell has
                new_cell_value = self.update_cell(cell_value, neighbors) # calculate the cell's new value
                new_board[-1].append(new_cell_value) # put the new value where the old one was in our new board
        return new_board

    def play_one_round(self):
        '''
        function: play_one_round plays a round of conways game of life and updates the board and step count
        parameters: none
        returns: side effects, modifies object's board
        '''
        self.frame_stack.push(self.board.copy())
        self.board = self.update_board()
        self.step_count += 1

    def go_back_one_round(self):
        '''
        function: go_back_one_round sets the board back one step
        parameters: none
        returns: side-effects, either board goes back one round, or prints stack is empty
        '''
        if self.frame_stack.peek() != 0:
            self.board = self.frame_stack.pop()
            self.step_count -= 1
        else:
            print("cannot go back any further")

    def reset(self):
        '''
        function: reset resets the game, deleting all saved frames in the stack and blanking the board
        parameters: none
        returns: side-effects, board and stack reset
        '''
        self.frame_stack = Stack(10000)
        self.board = self.make_board()
        self.step_count = 0
