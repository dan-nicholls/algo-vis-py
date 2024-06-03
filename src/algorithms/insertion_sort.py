from .algorithm import Algorithm


class InsertionSort(Algorithm):
    def __init__(self, data):
        super().__init__(data)
        self.n = len(self.data)
        self.sorted = False

    def initialise(self):
        self.i = 0
        self.j = 0
        self.sorted = False

    def step(self):
        if self.i <= self.n - 1:
            if (self.j <= self.i) and (self.j >= 0):
                if self.data[self.j] > self.data[self.j + 1]:
                    self.data[self.j], self.data[self.j + 1] = (
                        self.data[self.j + 1],
                        self.data[self.j],
                    )
                    self.j -= 1
                else:
                    self.i += 1
                    self.j = self.i - 1

            else:
                self.i += 1
                self.j = self.i - 1

        else:
            self.sorted = True

    def is_sorted(self):
        return self.sorted
