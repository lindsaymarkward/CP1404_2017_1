"""Drink class."""


class Drink:
    MINIMUM_ALCOHOL_THRESHOLD = 0.00

    def __init__(self, name="", price=0.0, volume=0.0, alcohol_content=0.0):
        self.name = name
        self.price = price
        self.alcohol_content = alcohol_content
        self.volume = volume

    def __str__(self):
        return "{self.name}, ${self.price:.2f}, {self.volume}mL ({self.alcohol_content}%)".format(self=self)

    def get_alcohol_volume(self):
        return (self.alcohol_content / 100) * self.volume

    def is_alcoholic(self):
        return self.alcohol_content > Drink.MINIMUM_ALCOHOL_THRESHOLD


def run_tests():
    # test default values
    d1 = Drink()
    print(d1)

    # test custom values
    d2 = Drink("Pina Colada", 12.3, 450, 12.5)
    d3 = Drink("Coffee", 4.5, 280, 0)
    print(d2)
    print(d2.is_alcoholic())
    print(d2.get_alcohol_volume())
    print(d3.name, "is alcoholic?", d3.is_alcoholic())


if __name__ == '__main__':
    run_tests()
