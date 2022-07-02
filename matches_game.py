import random
import sys


class Stock(object):
    def __init__(self):
        self.stock = 0

    def receive_stock(self, value):
        self.stock += value


class Boy(Stock):
    def __init__(self, name, first=False):
        Stock.__init__(self)
        self.name = name
        self.first = first
        self.stock = 0
        self.moves = []
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
        self.moves.append(matches)

        if self.first:
            self.stock = matches

        matches_to_send = min(self.stock, matches)
        self.scores.append(matches_to_send - 3.5)

        self.stock -= matches_to_send
        if self.next != None:
            self.next.receive_stock(matches_to_send)

    def total_score(self):
        return sum(self.scores)

class Production(Stock):
    def __init__(self):
        Stock.__init__(self)

boys = [Boy("Andy", first=True), Boy("Ben"), Boy("Chuck"), Boy("Dave"), Boy("Evan")]

def cast_die():
    return random.randint(1, 6)

def make_move(boy):
    n = cast_die()
    print(f"{boy} passes {n} matches to the next stage")

if __name__ == "__main__":
    moves = 10
    try:
        moves = int(sys.argv[1])
        print(f"Will make {moves} moves")
    except:
        print(f"Will use default number of moves = {moves}")

    print(boys)
    production = Production()

    counter = 1
    for i in range(len(boys) - 1):
        boys[i].set_next(boys[i+1])

    boys[-1].set_next(production)

    while counter <= moves:
        for boy in boys:
            boy.make_move()
        counter += 1

    print(f"Expectd production is {3.5 * moves}")
    print(f"Actual production is {production.stock}\n")
    for boy in boys:
        print(f"{boy} gets score {boy.total_score()} with stock {boy.stock}")
        print(f"\t{boy.moves}")
        print(f"\t{boy.scores}")

