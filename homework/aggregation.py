class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def display_info(self):
        print(f"It's guitar has {self.strings.amount} {self.strings.metal} strings "
              f"with {self.strings.core} core and {self.strings.caliber} caliber.")


class Strings:
    def __init__(self, caliber, metal, core, amount):
        self.caliber = caliber
        self.metal = metal
        self.core = core
        self.amount = amount


if __name__ == '__main__':
    strings_set = Strings(0.26, "nickel", "hex", 5)
    my_guitar = Guitar(strings_set)
    my_guitar.display_info()
