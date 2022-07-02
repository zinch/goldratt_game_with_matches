import random


class Boy(object):
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

def cast_die():
    return random.randint(1, 6)

def make_move(name):
    n = cast_die()
    print(f"{name} passes {n} matches to the next stage")

if __name__ == "__main__":
    boys = [Boy("Andy"), Boy("Ben"), Boy("Chuck"), Boy("Dave"), Boy("Evan")]

    print(boys)
    counter = 1
    while counter <= 10:
        make_move(random.choice(boys).name)
        print(f"Move {counter}")
        counter += 1

