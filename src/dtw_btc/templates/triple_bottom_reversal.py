from .pattern import Pattern


class TripleBottomReversal(Pattern):
    def __init__(self):
        values = [7, 4, 6, 4, 6, 4, 7]
        super(TripleBottomReversal, self).__init__(values=values)
