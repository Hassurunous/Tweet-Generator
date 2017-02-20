class Markov(dict):

    def __init__(self, iterable=None):
        """Initialize this Markov object either empty, for filling afterwards, or seeded with a list of items."""
        super(Dictionary, self).__init()
        self.types = 0
