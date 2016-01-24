"""
Draws the T-Square fractal.

"""
import pygame, time
from mathgraph import *

def distance((x,y),(x1,y1)):
    dx = (x-x1)
    dy = (y-y1)
    return (dx**2+dy**2)**(0.5)


class Square(object):
    def __init__(self, (center_x, center_y), side_length, color=black):
        self.center = (center_x, center_y)
        self.side_length = side_length
        self.color = color
        self.corners = [(self.center[0] + i * self.side_length/2.0, self.center[1] + j * self.side_length/2.0) for i in (1,-1) for j in (1,-1)]
    
    def draw(self):
        x_min = self.center[0] - self.side_length/2.0
        x_max = self.center[0] + self.side_length/2.0
        y_min = self.center[1] - self.side_length/2.0
        y_max = self.center[1] + self.side_length/2.0
        x_draws = self.side_length / float(mX - lX) * width * 1.2
        y_draws = self.side_length / float(mY - lY) * height * 1.2
        for x in frange(x_min, x_max, x_draws):
            for y in frange(y_min, y_max, y_draws):
                draw(x,y,self.color)

counter = 0
def t_square(square, max_iterations, iterations = 0):
    square.draw()
    flip()
    global counter
    counter += 1
    if iterations < max_iterations:
        [t_square(Square(corner, square.side_length/2.0), max_iterations, iterations + 1) for corner in square.corners]

t1 = time.time()

screen.fill(white)
s = Square((0,0), mX)
t_square(s, 7)
flip()

t2 = time.time()


print "Done."
print "{0} squares in {1} seconds".format(counter, round((t2 - t1), 3))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()





























