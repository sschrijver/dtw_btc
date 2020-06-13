from .pattern import Pattern


class DoubleBottomReversal(Pattern):
    def __init__(self):
        values = [6, 2, 4, 2, 6]
        super(DoubleBottomReversal, self).__init__(values=values)
