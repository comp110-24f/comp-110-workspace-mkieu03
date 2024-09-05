"""Having Tea party with Friends."""

__author__: str = "730485068"


def main_planner(guests: int) -> None:
    """main planner for number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treat_count=treats(people=guests))))


def tea_bags(people: int) -> int:
    """Everyone at tea party drinks 2 cups of tea"""
    return people * 2


def treats(people: int) -> int:
    """1.5 treats per person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """teabag .50 each and treat 0.75 each"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
