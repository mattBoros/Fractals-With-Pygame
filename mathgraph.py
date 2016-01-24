"""
A set of functions I made to make it very easy to draw mathematical objects on a pygame screen.

"""
import pygame
from math import *

size = width, height = 800,800

square = 10

lX, mX = -1*square,square
lY, mY = -1*square,square

pygame.init()

screen = pygame.display.set_mode(size)
px = pygame.PixelArray(screen)

flip = pygame.display.flip

white = (255,255,255)
black = (0,0,0)


def frange(start, end, steps):
    increment = (end-start)/float(steps-1)
    current = start
    while current < end:
        yield current
        current += increment

def directDraw(xs,ys,color):
    px[xs,ys] = color

def real_to_screen(x,y):
    xs = ((height)/float((lY - mY))*y) + (height * mY)/float(mY - lY)
    ys = ((width)/float((mX - lX))*x) + (width * lX)/float((lX - mX))
    return int(xs), int(ys)

def draw(x,y,color=black):
    ys,xs = real_to_screen(x,y)
    try:
        px[xs,ys] = color
    except: pass

def draw_axes(color = white):
    
    for x in frange(lX,mX,width):
        draw(x,0,color)
    for y in frange(lY,mY,height):
        draw(0,y,color)

def highlight(x,y,colorAdd):
    xs,ys = real_to_screen(x,y)
    if xs > 0 and ys > 0 and xs < width and ys < height:
        color = screen.get_at((xs,ys))
        r,g,b = color.r,color.g,color.b
        
        r = max( min( r+colorAdd[0], 255 ), 0 )
        g = max( min( g+colorAdd[1], 255 ), 0 )
        b = max( min( b+colorAdd[2], 255 ), 0 )
        color = (r,g,b)
        
        directDraw(xs,ys,color)

def distance((x,y),(x1,y1)):
    dx = (x-x1)
    dy = (y-y1)
    return (dx**2+dy**2)**(0.5)

def polar_to_cart(theta,r):
    x = r*cos(theta)
    y = r*sin(theta)
    return (x,y)

def m_b(p1, p2):
    if p1[0] == p2[0]:
        return (9999999, -99999999)
    m = (p1[1] - p2[1])/float(p1[0] - p2[0])
    b = p1[1] - m*p1[0]
    return (m,b)

def draw_line(start, end, color=black):
    start = list(real_to_screen(*start))
    end = list(real_to_screen(*end))
    start.reverse()
    end.reverse()
    pygame.draw.line(screen, color, start, end)

def absolute_value(a,b):
    # z = a + bi
    return pow(a*a + b*b,0.5)

def polar_to_cart(theta, r):
    return cos(theta) * r, sin(theta) * r

def cart_to_polar(p1, p2):
    x,y = (p1[0] - p2[0], p1[1] - p2[1])
    theta = atan2(y, x)
    r = (x**2 + y**2)**0.5
    return (theta, r)

def pythag(p1, p2):
    return pow((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 ,.5)




























