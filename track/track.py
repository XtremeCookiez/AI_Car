import math

class TrackSegment:
    
    def __init__(self, left, top, height, width, entryAngle, exitAngle):
        self.top = top
        self.left = left
        self.height = height
        self.width = width
    
    def Bottom(self):
        return self.top - self.height
    
    def Right(self):
        return self.left + self.width

class StraightSegment(TrackSegment):
    
    def __init__(self, left, top, length, angle):
        height = length * math.sin(math.radians(angle))
        width = length * math.cos(math.radians(angle))
        super().__init__(left, top, height, width, angle, angle)

class ArcSegment(TrackSegment):
    
    def __init__(self, left, top, radius, arcAngle, entryAngle):
        self.radius = radius
        
        # TODO: Update with real calculations
        height = radius 
        width = radius 
        super().__init__(left, top, height, width, entryAngle, entryAngle + arcAngle)
    
    def _ExitAngle(self):
        return (int)(self.entryAngle + self.arcAngle) % 360
