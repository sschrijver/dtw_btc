from .pattern import Pattern


class DoubleTopReversal(Pattern):
    def __init__(self):
        values = [2, 6, 4, 6, 2]
        super(DoubleTopReversal, self).__init__(values=values)
