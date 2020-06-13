from .pattern import Pattern


class SymmetricalTriangle(Pattern):
    def __init__(self):
        values = [8, 2, 7, 3, 6, 4, 5]
        super(SymmetricalTriangle, self).__init__(values=values)
