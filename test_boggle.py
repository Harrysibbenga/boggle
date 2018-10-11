import unittest
import boggle
from string import ascii_uppercase

#class test_boggle(unittest.TestCase):
#    def test_is_this_thing_on(self):
#        self.assertEqual(1,1)

class TestBoggle(unittest.TestCase):
    '''
    our test suit for boggle solver
    '''
    
    def test_can_create_an_empty_grid(self):
        '''
        test to see if we can create an empty grid
        '''
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_is_width_times_height(self):
        '''
        Test is to ensure that the total size of the grid is equal to the width * height
        '''
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        '''
        test to ensure that all of the coordinates inside the grid can be accssesd
        '''
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid) 
        self.assertIn((0, 1), grid) 
        self.assertIn((1, 0), grid) 
        self.assertIn((1, 1), grid) 
        self.assertNotIn((2, 2), grid)
        
        
    def test_grid_is_filled_with_letters(self):
        '''
        ensure that each of the coordinates in the grid contains letters
        '''
        grid = boggle.make_grid(2 ,3)
        for letter in grid.values():    
            self.assertIn(letter, ascii_uppercase)