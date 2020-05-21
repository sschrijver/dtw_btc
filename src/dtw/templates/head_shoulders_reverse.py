from .pattern import Pattern


class HeadAndShouldersReverse(Pattern):
    def __init__(self):
        values = [6, 4, 6, 2, 6, 4, 6]
        super(HeadAndShouldersReverse, self).__init__(values=values)
