from product import Product


class FoodItem(Product):
    def __init__(self, name, price, is_on_sale, use_by):
        super().__init__(name, price, is_on_sale)
        self.use_by = use_by

    def __str__(self):
        return "{} {}".format(super().__str__()[:-1], self.use_by)


def run_tests():
    fi = FoodItem("Pine Nuts", 7.3, False, "13/07/2014")
    print(fi)
    # fi.blah = "what?"
    # print(dir(fi))
    print(type(3.4))

if __name__ == '__main__':
    run_tests()
