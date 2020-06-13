from .pattern import Pattern


class BumpAndRunReversal(Pattern):
    def __init__(self):
        values = [2, 3, 4, 8, 5]
        super(BumpAndRunReversal, self).__init__(values=values)
