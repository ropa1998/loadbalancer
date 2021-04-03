import itertools


class RoundRobinBalancer():
    def __init__(self, channels):
        self.round_robin = itertools.cycle(channels)

    def get_channel(self):
        return self.round_robin.__next__()
