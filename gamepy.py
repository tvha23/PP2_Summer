import pygame,sys
from    pygame.locals import *
pygame.init()
#use tuples to set window dimensions
win=pygame.display.set_mode((900,500))
#To set caption of window:
pygame.display.set_caption("Hello World!")
#make some color variables to make life easier
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)  
#We’ll use fonts anytime we need to print text on a pygame window
my_font=pygame.font.SysFont(None,48)
"""
The Font object that you’ve stored in the my_Font variable has a method called render().
This method will return a Surface object with the text drawn on it. The first parameter to
render() is the string of the text to draw.
The second parameter is a Boolean for whether
or not to anti-alias the font. Anti-aliasing blurs your text slightly to make it look smoother
Third and fourth one are color of text and backgroud, respectively
"""

text=my_font.render("Hello World!", 0, white, blue)
text_rect=text.get_rect()
text_rect.centerx=win.get_rect().centerx
text_rect.centery=win.get_rect().centery
win.fill(white)
#pygame.gfxdraw.trigon(win, 10, 10, 30, 20, 50, 100, black)
pygame.draw.line(win, red, (5,5), (10,25), 10)
pygame.draw.circle(win,blue,(300,300),100,0)
pix_array=pygame.PixelArray(win)
pix_array[480][380] = black
del pix_array
pygame.display.update()
win.blit(text,text_rect)
while(True):
    for event in pygame.event.get():
        if(event.type==QUIT):
            pygame.quit()
            sys.exit()



