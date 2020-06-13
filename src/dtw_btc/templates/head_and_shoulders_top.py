from .pattern import Pattern


class HeadAndShouldersTop(Pattern):
    def __init__(self):
        values = [4, 6, 4, 8, 4, 6, 4]
        super(HeadAndShouldersTop, self).__init__(values=values)
