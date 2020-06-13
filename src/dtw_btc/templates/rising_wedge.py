from .pattern import Pattern


class RisingWedge(Pattern):
    def __init__(self):
        values = [2, 6, 3, 7, 4, 8, 5]
        super(RisingWedge, self).__init__(values=values)
