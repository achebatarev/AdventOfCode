import pygame
from pygame.locals import KEYDOWN, K_q
import sys

SCREENSIZE = WIDTH, HEIGHT = 1920,1080 
PADDING = PADLEFTRIGHT, PADTOPBOTTOM = 0, 0
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
_VARS = {'surf': False}

def main():
    pygame.init()
    print(SCREENSIZE)
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(GREY)
    while True:
        check_events()
        draw_dot()
        pygame.display.update()

def draw_dot():
    horizontal_size = 10
    vertical_size = 10
    pygame.draw.circle(_VARS['surf'], BLACK, (PADLEFTRIGHT, PADTOPBOTTOM, horizontal_size, vertical_size))


def draw_grid(divisions):
    #pygame.draw.line(_VARS['surf'], BLACK, (PADLEFTRIGHT, PADTOPBOTTOM), (WIDTH - PADLEFTRIGHT, PADTOPBOTTOM), 2)
    #pygame.draw.line(_VARS['surf'], BLACK, (PADLEFTRIGHT, PADTOPBOTTOM), (PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    #pygame.draw.line(_VARS['surf'], BLACK, (WIDTH-PADLEFTRIGHT, PADTOPBOTTOM), (WIDTH-PADLEFTRIGHT, HEIGHT-PADTOPBOTTOM), 2)
    #pygame.draw.line(_VARS['surf'], BLACK, (PADLEFTRIGHT, HEIGHT-PADTOPBOTTOM), (WIDTH-PADLEFTRIGHT, HEIGHT-PADTOPBOTTOM), 2)

    horizontal_cellsize = (WIDTH -(PADLEFTRIGHT * 2))/ divisions
    vertical_cellsize = (HEIGHT -(PADTOPBOTTOM * 2))/ divisions

    for x in range(divisions+1):
        pygame.draw.line(_VARS['surf'], BLACK, (PADLEFTRIGHT, PADTOPBOTTOM + vertical_cellsize*x), (WIDTH - PADLEFTRIGHT, PADTOPBOTTOM + vertical_cellsize*x), 1)
        pygame.draw.line(_VARS['surf'], BLACK, (PADLEFTRIGHT + horizontal_cellsize*x, PADTOPBOTTOM), (PADLEFTRIGHT + horizontal_cellsize*x, HEIGHT-PADTOPBOTTOM), 1)
def draw_line():
    pygame.draw.line(_VARS['surf'], BLACK, (0, 0), SCREENSIZE, 10)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()