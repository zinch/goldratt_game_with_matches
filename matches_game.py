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
        moves = min(moves, int(sys.argv[1]))
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
        print(f"\t{boy.roll_results}")
        print(f"\t{boy.scores}")


    with open("game_chart.csv", "w", encoding="utf-8") as f:
        first_column_width = 15
        participant_len = 10
        total_len = first_column_width + (participant_len + 2) * len(boys) 

        def horizontal_line():
            f.write(f"{'_' * total_len}\n")

        def upper_line():
            f.write("\u203E" * total_len)
            f.write("\n")

        names = "  ".join(map(lambda b: b.name.center(participant_len), boys))
        horizontal_line()
        f.write(f"{' ' * (first_column_width)}{names}\n")
        upper_line()
        move = "".join(map(str, list(range(1, moves))))
        if moves == 10:
            move = move + "0"
        else:
            move = move + str(moves)

        move = move.ljust(participant_len + 2)
        all_moves = move * len(boys)

        f.write(f"{'Move nr'.ljust(first_column_width)}{all_moves}\n")
        upper_line()

        def array_to_string(boy, field_getter):
            return "".join(map(str, field_getter(boy))).ljust(participant_len + 2)

        def scores_as_string(boy):
            return array_to_string(boy, lambda b: b.roll_results)

        all_scores = "".join(map(scores_as_string, boys))
        f.write(f"{'Roll result'.ljust(first_column_width)}{all_scores}\n")
        upper_line()

        def matches_moved_as_string(boy):
            return array_to_string(boy, lambda b: b.matches_moved)
        all_matches_moved = "".join(map(matches_moved_as_string, boys))

        f.write(f"{'Matches moved'.ljust(first_column_width)}{all_matches_moved}\n")
        upper_line()

