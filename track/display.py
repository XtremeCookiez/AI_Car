import pygame

from .track import StraightSegment, TrackSegment, ArcSegment

pygame.init()

BACKGROUND = (34,139,34)
ROAD = (42, 41, 34)
screen = pygame.display.set_mode((800,800))
screen.fill(BACKGROUND)

def DrawStraightSegment(segment:StraightSegment):

    print((segment.BottomLeft(), segment.BottomRight(),
                        segment.TopRight(), segment.TopLeft()))

    pygame.draw.polygon(screen, ROAD, 
                        (segment.BottomLeft(), segment.BottomRight(),
                        segment.TopRight(), segment.TopLeft()))

def DrawArcSegment(segment:ArcSegment):
    pass