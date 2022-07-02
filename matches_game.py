import sys
from stock import Stock
from boy import Boy


class Production(Stock):
    def __init__(self):
        Stock.__init__(self)

boys = [Boy("Andy", first=True), Boy("Ben"), Boy("Chuck"), Boy("Dave"), Boy("Evan")]

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

