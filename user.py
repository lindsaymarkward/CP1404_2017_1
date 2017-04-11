STARTING_TACOS = 5


class User:
    def __init__(self, name):
        self.name = name
        self.tacos = STARTING_TACOS
        self.score = 0

    def __str__(self):
        return "{self.name} has score: {self.score}, {self.tacos} tacos left.".format(
            self=self)

    def give_taco(self, other_user, number_of_tacos):
        if number_of_tacos > self.tacos:
            number_of_tacos = self.tacos
        self.tacos -= number_of_tacos
        other_user.score += number_of_tacos


def run_tests():
    u1 = User("Lindsay")
    u2 = User("Jeff")
    print(u1)
    print(u2)
    u1.give_taco(u2, 13)
    print(u1)
    print(u2)


if __name__ == '__main__':
    run_tests()
