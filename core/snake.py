'''
Created on Oct 29, 2014

@author: haakonkaurel
'''
if __name__=="__main__":
    from time import sleep

X,Y=0,1

class Direction:
    UP      = (0,-1)
    RIGHT   = (1, 0)
    DOWN    = (0, 1)
    LEFT    = (-1,0)
    
class Snake:
    def __init__(self, pos=[0,0], direction=Direction.RIGHT):
        self.pieces = [pos]
        self.direction = direction
        self.grow = False
        
    def tick(self):
        head = self.pieces[0]
        self.pieces.insert(0, [head[X]+self.direction[X], 
                               head[Y]+self.direction[Y]]
                           )
        
        if self.grow:
            self.grow=False
        else:
            self.pieces.pop()
        
if __name__=="__main__":
    snake = Snake()
    
    while True:
        print(snake.pieces)
        snake.tick()
        sleep(1)
        
        