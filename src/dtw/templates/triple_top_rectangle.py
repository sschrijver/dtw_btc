from .pattern import Pattern


class TripleTopRectangle(Pattern):
    def __init__(self):
        values = [4,6,46,4,6]
        super(TripleTopRectangle, self).__init__(values=values)
