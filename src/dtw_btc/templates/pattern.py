class Pattern:
    def __init__(self, values: list):
        self.values = values

    def get_pattern(self):
        if not self.values:
            raise ValueError('values is not set. Please revisit the Pattern inheritance!')
        return self.values

    def get_min_max(self):
        return min(self.values), max(self.values)
