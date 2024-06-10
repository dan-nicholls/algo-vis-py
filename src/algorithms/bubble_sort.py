from .algorithm import Algorithm


class BubbleSort(Algorithm):
    def __init__(self, data):
        super().__init__(data)
        self.n = len(self.data)
        self.sorted = False

    def initialise(self):
        # Initialise pointers
        self.i = 0
        self.j = 0
        self.sorted = False

    def step(self):
        if self.i < self.n - 1:
            if self.j < self.n - 1 - self.i:
                if self.data[self.j] > self.data[self.j + 1]:
                    self.data[self.j], self.data[self.j + 1] = (
                        self.data[self.j + 1],
                        self.data[self.j],
                    )
                self.j += 1
            else:
                self.j = 0
                self.i += 1
        else:
            self.sorted = True

    def is_sorted(self):
        return self.sorted

    def get_highlighted_indexes(self):
        return {self.j: "red", self.i: "orange"}
