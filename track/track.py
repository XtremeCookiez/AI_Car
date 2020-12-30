import math

class TrackSegment:
    
    def __init__(self, left, bottom, height, width, entryAngle, exitAngle, track_width):
        self.bottom = bottom
        self.left = left
        self.height = height
        self.width = width
        self.track_width = track_width
        self.entryAngle = entryAngle
        self.exitAngle = exitAngle

    def TopRight(self):
        return (self.left + self.width, self.bottom + self.height)

class StraightSegment(TrackSegment):
    
    def __init__(self, left, bottom, track_width, length, angle):
        self.angle = angle
        radians = math.radians(angle)
        height = (length * math.sin(radians)) + (track_width * math.cos(radians))
        right = left + (track_width * math.sin(radians)) + (length * math.cos(radians))
        
        # width = length * math.cos(math.radians(angle))
        super().__init__(left, bottom, height, width, angle, angle, track_width)
    
    def _Vector(self):
        """
        The vector of the length
        """

        radians = math.radians(self.angle)
        return (self.length * math.cos(radians), self.length * math.sin(radians))

    def _WidthVector(self):
        radians = math.radians(self.angle)
        return (self.track_width * math.sin(radians), self.track_width * math.cos(radians))

    def TopLeft(self):
        radians = math.radians(self.angle)
        vector = self._vector()
        return (self.left + vector[0], self.bottom + vector[1])

    def TopRight(self):
        radians = math.radians(self.angle)
        vector = self._vector()
        return (self.left + (self.track_width * math.sin(radians)) + (vector[0]), self.bottom)
    
    def BottomRight(self):
        radians = math.radians(self.angle)
        vector = self._WidthVector()
        return (self.left + vector[0], self.bottom + vector[1])
    
    def BottomLeft(self):
        return (self.left, self.bottom)

class ArcSegment(TrackSegment):
    
    def __init__(self, left, top, track_width, radius, arcAngle, entryAngle):
        self.radius = radius
        self.outer_radius = radius + track_width
        
        length = 2 * math.pi * math.sin(math.radians(arcAngle))

        # TODO: Update with real calculations
        height = radius 
        width = width
        super().__init__(left, top, height, width, entryAngle, entryAngle + arcAngle)
    
    def _ExitAngle(self):
        return (int)(self.entryAngle + self.arcAngle) % 360
