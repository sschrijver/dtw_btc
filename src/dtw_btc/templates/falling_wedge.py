from .pattern import Pattern


class FallingWedge(Pattern):
    def __init__(self):
        values = [5, 8, 4, 7, 3, 6, 2]
        super(FallingWedge, self).__init__(values=values)
