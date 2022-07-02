import random
from stock import Stock

def cast_die():
    return random.randint(1, 6)

class Boy(Stock):
    def __init__(self, name, first=False):
        Stock.__init__(self)
        self.name = name
        self.first = first
        self.stock = 0
        self.roll_results = []
        self.scores = []
        self.next = None

    def set_next(self, boy):
        self.next = boy

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def make_move(self):
        matches = cast_die()
        self.roll_results.append(matches)

        if self.first:
            self.stock = matches

        matches_to_send = min(self.stock, matches)
        self.scores.append(matches_to_send - 3.5)

        self.stock -= matches_to_send
        if self.next != None:
            self.next.receive_stock(matches_to_send)

    def total_score(self):
        return sum(self.scores)

