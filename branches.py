"""
Draws branches randomly at a 45 degree angle from each other.
Produces some cool results.

"""
import random
from math import atan2
from mathgraph import *

size = width, height = 600,600

square = 10

lX, mX = -1*square,square
lY, mY = -1*square,square


class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.midpoint = map(lambda tup : sum(tup)/2.0, zip(self.start, self.end))
        self.length = pythag(self.start, self.end)

    def draw(self):
        draw_line(self.start, self.end)

    def get_other_lines(self):
        m,b = m_b(self.start, self.end)
        angle = degrees(atan2(m,1))
        angles = map(radians, [angle + 45, angle - 45])
        points = map(lambda theta : polar_to_cart(theta, self.length/2.0), angles)
        points = [(p[0] + self.midpoint[0], p[1] + self.midpoint[1]) for p in points]
        
        return map(lambda point2 : Line(self.midpoint, point2), points)
      
def draw_branches(line, max_iterations, iterations=0):
    line.draw()
    if iterations < max_iterations:
        lines = line.get_other_lines()
        if random.random() < 0.92:
            draw_branches(lines[0], max_iterations, iterations + 1)
        if random.random() < 0.92:
            draw_branches(lines[1], max_iterations, iterations + 1)
            
        
if __name__ == '__main__':
    screen.fill(white)
    l = Line((-7.5, 0), (7.5,0))
    draw_branches(l, 10)

    flip()

    print "Done."

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()










































