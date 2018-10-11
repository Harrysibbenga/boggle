from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    '''
    creates a grid that will hold all the tiles for boggle game
    
    '''
    return { (row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width) } 