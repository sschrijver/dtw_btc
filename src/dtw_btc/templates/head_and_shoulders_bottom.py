from .pattern import Pattern


class HeadAndShouldersBottom(Pattern):
    def __init__(self):
        values = [6, 4, 6, 2, 6, 4, 6]
        super(HeadAndShouldersBottom, self).__init__(values=values)
