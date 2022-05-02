'''
Anthony Burwinkel
CS5001 Spring 2022
Final Project

This file contains tests for the stack class
'''

import unittest
from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    def test_stack(self):
        '''
        function: test stack tests the stack class
        parameters: none
        returns: test validations
        '''
        s = Stack(20)
        self.assertEqual(s.end,0) # make sure the stack's end initializes at 0
        for i in range(20):
            s.push(i)
        self.assertEqual(s.push(1),0) # make sure the stack is full and returns 0
        for i in range(10): # empty half of the stack
            s.pop()
        self.assertEqual(s.end, 10) # make sure the stack's end variable has decremented
        for i in range(10): # fill the stack again
            s.push(i)
        for i in range(20): # empty the stack
            s.pop()
        self.assertEqual(s.end, 0)


if __name__ == "__main__":
    unittest.main()
