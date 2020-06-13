from .pattern import Pattern


class TripleTopReversal(Pattern):
    def __init__(self):
        values = [3, 6, 4, 6, 4, 6, 3]
        super(TripleTopReversal, self).__init__(values=values)
