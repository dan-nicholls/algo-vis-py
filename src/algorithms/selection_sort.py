from .algorithm import Algorithm


class SelectionSort(Algorithm):
    def __init__(self, data):
        super().__init__(data)
        self.n = len(self.data)
        self.sorted = False

    def initialise(self):
        self.i = 0
        self.j = 0
        self.min_index = 0
        self.sorted = False

    def step(self):
        if self.i < self.n - 1:
            if self.j < self.n:
                if self.data[self.j] < self.data[self.min_index]:
                    self.min_index = self.j
                self.j += 1
            else:
                if self.min_index != self.i:
                    self.data[self.i], self.data[self.min_index] = (
                        self.data[self.min_index],
                        self.data[self.i],
                    )
                self.i += 1
                self.j = self.i + 1
                self.min_index = self.i

        else:
            self.sorted = True

    def is_sorted(self):
        return self.sorted
