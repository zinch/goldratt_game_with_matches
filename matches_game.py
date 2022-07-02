import random


class Boy(object):
    def __init__(self, name, first=False):
        self.name = name
        self.first = first
        self.stock = 0
        self.moves = []
        self.scores = []

    def set_next(self, boy):
        self.next = boy

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def make_move(self):
        if self.first:
            matches = cast_die()
        else:
            matches = max(self.stock, cast_die())
        print(f"{self.name} casts {matches}")
        self.moves.append(matches)
        self.scores.append(matches - 3.5)


boys = [Boy("Andy", first=True), Boy("Ben"), Boy("Chuck"), Boy("Dave"), Boy("Evan")]

def cast_die():
    return random.randint(1, 6)

def make_move(boy):
    n = cast_die()
    print(f"{boy} passes {n} matches to the next stage")

if __name__ == "__main__":

    print(boys)
    counter = 1
    for i in range(len(boys) - 1):
        boys[i].set_next(boys[i+1])
    while counter <= 10:
        for boy in boys:
            boy.make_move()
        print(f"Move {counter}")
        counter += 1

    for boy in boys:
        print(boy)
        print(f"\t{boy.moves}")
        print(f"\t{boy.scores}")

