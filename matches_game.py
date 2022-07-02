import random


def cast_die():
    return random.randint(1, 6)

def make_move(name):
    n = cast_die()
    print(f"{name} passes {n} matches to the next stage")

if __name__ == "__main__":
    boys = ["Andy", "Ben", "Chuck", "Dave", "Evan"]
    print(boys)
    make_move(random.choice(boys))
