def make_grid(width, height):
    '''
    creates a grid that will hold all the tiles for boggle game
    
    '''
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
    } 