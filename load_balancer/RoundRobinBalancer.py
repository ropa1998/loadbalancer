import itertools


class RoundRobinBalancer():
    def __init__(self, channels):
        self.max_retries = len(channels)
        self.round_robin = itertools.cycle(channels)

    def get_channel(self):
        next__ = self.round_robin.__next__()
        return next__

    def get_max_retries(self):
        return self.max_retries
