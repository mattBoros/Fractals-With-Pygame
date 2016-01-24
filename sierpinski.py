"""
Draws Sierpinski's triangle.

"""
import pygame, time
from mathgraph import *

def average(p1, p2):
    return map(lambda tup : sum(tup)/2.0, zip(p1, p2))

class Triangle(object):
    def __init__(self, p1, p2, p3):
        self.points = [p1,p2,p3]

    def draw(self):
        [draw_line(start, end) for start in self.points for end in self.points if start != end]

    def get_insides(self):
        p1,p2,p3 = self.points
        m1 = average(p1, p2)
        m2 = average(p1, p3)
        m3 = average(p2, p3)
        return [Triangle(t1, t2, t3) for (t1, t2, t3) in ((m1, p1, m2), (m1, p2, m3), (m3, m2, p3))]


counter = 0
def sierpinski(triangle, max_iterations, iterations=0):
    triangle.draw()
    flip()
    global counter
    counter += 1
    if iterations < max_iterations:
        [sierpinski(t, max_iterations, iterations + 1) for t in triangle.get_insides()]


t1 = time.time()

screen.fill(white)
t = Triangle((-7,-7), (7,-7), (0,7))
sierpinski(t, 7)
flip()

t2 = time.time()


print "Done."
print "{0} triangles in {1} seconds".format(counter, round((t2 - t1), 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




























