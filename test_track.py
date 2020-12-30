import track
from track import display

trackSegments = []

trackSegments.append(track.StraightSegment(100,100, 20, 150, 0))
trackSegments.append(track.StraightSegment(250,90, 40, 150, 0))


for item in trackSegments:
    if type(item) == track.StraightSegment:
        display.DrawStraightSegment(item)

while True:
    for event in display.pygame.event.get():
        if event.type == display.pygame.QUIT:
            display.pygame.quit()
            quit()

    display.pygame.display.update()
# trackSegments.append(track.StraightSegment(100,250, 25, 150, 90))
