'''
Anthony Burwinkel
CS5001 Spring 2022
Project 9

this file contains a simple stack class that is used by the game logic module to store past game states
'''

import sys

class Stack:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our stack
        '''
        self.data = [0] * size
        self.end = 0

    def push(self, item):
        ''' push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        '''
        if self.end >= len(self.data):
            print("Full!")
            return 0
        self.data[self.end] = item
        self.end += 1

    def pop(self):
        ''' pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        '''
        if self.end <= 0:
            print("Empty!")
            return 0
        self.end -= 1
        return self.data[self.end]

    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
           self -- the current object
        '''
        for i in range(self.end - 1, -1, -1):
            print(self.data[i])

    def peek(self):
        '''
        function: peek shows the item at the top of the stack
        without popping it
        parameters: none
        returns: item at top of the stack
        '''
        return self.data[self.end-1]

