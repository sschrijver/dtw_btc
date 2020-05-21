from .pattern import Pattern


class HeadAndShoulders(Pattern):
    def __init__(self):
        values = [4, 6, 4, 8, 4, 6, 4]
        super(HeadAndShoulders, self).__init__(values=values)
