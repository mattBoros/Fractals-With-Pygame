"""
Draws a set of lines, then a set of lines perpendicular to
the original set, then another perpendicular set, and so on.

"""
import pygame, time
from mathgraph import *


class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.midpoint = map(lambda tup : sum(tup)/2.0, zip(self.start, self.end))
        self.length = pythag(self.start, self.end)

    def draw(self, color=black):
        draw_line(self.start, self.end, color)

    def perpendicular_lines(self):
        theta,r = cart_to_polar(self.start, self.end)
        angles = [theta + pi/2.0, theta - pi/2.0]
        end_coordinates = [map(sum,zip(polar_to_cart(angle, self.length/2.0), self.midpoint)) for angle in angles]
        return [Line(self.midpoint, end) for end in end_coordinates] + [Line(self.start, self.midpoint)]

counter = 0

def perp_branches(line, max_iterations, iterations=0):
    c = 255*iterations/float(max_iterations+1)
    line.draw((c,c, c))
    flip()
    global counter
    counter += 1
    if iterations < max_iterations:
        [perp_branches(l, max_iterations, iterations + 1) for l in line.perpendicular_lines()]
        

t1 = time.time()

screen.fill(white)
l1 = Line((-9, 0), (9,0))
perp_branches(l1, 9)
flip()

t2 = time.time()

print "Done."
print "{0} lines in {1} seconds".format(counter, round(t2 - t1, 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()










































