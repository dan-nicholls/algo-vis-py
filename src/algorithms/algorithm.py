from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, data, settings):
        self.data = data
        self.current_step = 0
        self.settings = settings

    @abstractmethod
    def initialise(self):
        """Set up the initial state for the algorithm."""
        pass

    @abstractmethod
    def step(self):
        """Perform a single step of the algorithm"""
        pass

    @abstractmethod
    def is_sorted(self):
        """Check if data is fully sorted."""
        pass

    def reset(self, data):
        """Reset the algorithm with new data."""
        self.data = data
        self.current_step = 0
        self.initialise()

    @abstractmethod
    def get_highlighted_indexes(self):
        pass
