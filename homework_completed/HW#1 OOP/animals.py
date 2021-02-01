class Animal:
    def __init__(self, animal_name, animal_class, weight, age):
        self.animal_name = animal_name
        self.animal_class = animal_class
        self.weight = weight
        self.age = age

    def display_info(self):
        print(f"It is {self.animal_name} and it belongs to {self.animal_class} class\n"
              f"It is {self.age} years old and weighs {self.weight} kg.")

    def eat(self):
        print("Start eating...")

    def sleep(self):
        print("It's time to sleep...")


class Cat(Animal):
    def __init__(self, animal_name, animal_class, weight, age, name):
        super().__init__(animal_name, animal_class, weight, age)
        self.name = name

    def respond_to_the_name(self):
        if self.name != "":
            print("Meow, meow!")

    def play(self):
        print("Start playing...")


class Crucian(Animal):
    def __init__(self, animal_name, animal_class, weight, age, color):
        super().__init__(animal_name, animal_class, weight, age)
        self.color = color

    def display_info(self):
        print(f"It is {self.animal_name} and it belongs to {self.animal_class} class\n"
              f"It is {self.age} years old and weighs {self.weight} kg.\n"
              f"Also it has {self.color} color")

    def breathe_underwater(self):
        print("Start breathe underwater...")


class GoldFish(Crucian):
    def fulfil_the_wish(self):
        print("Start to fulfil wishes...")


class Deer(Animal):
    def __init__(self, animal_name, animal_class, weight, age, horns):
        super().__init__(animal_name, animal_class, weight, age)
        self.horns = horns

    def defend(self):
        print(f"Use the power of {self.horns}")


class RedDeer(Deer):
    def jump_on_fields(self):
        print("Jump, jump, jump")


class ChristmasDeer(Deer):
    def __init__(self, animal_name, animal_class, weight, age, horns, name):
        super().__init__(animal_name, animal_class, weight, age, horns)
        self.name = name

    def pull_the_sled(self):
        print(f"Oh no, again... Come on, {self.name}, come on.")


if __name__ == '__main__':
    lucy = Cat("cat", "mammal", 4, 3, "Lucy")
    lucy.display_info()
    lucy.play()
    lucy.respond_to_the_name()
    print("Is Lucy a Deer? -", isinstance(lucy, Deer), "\n")

    crucian = Crucian("crucian", "fish", 0.8, 1, "silver")
    crucian.display_info()
    crucian.eat()
    crucian.breathe_underwater()
    print("")

    goldfish = GoldFish("goldfish", "fish", 0.5, 2, "gold")
    goldfish.eat()
    goldfish.fulfil_the_wish()
    print("")

    my_deer = ChristmasDeer("Christmas deer", "mammal", 100, 5, "big white horns", "Dasher")
    my_deer.pull_the_sled()
    print(f"Is {my_deer.name} a Deer? -", isinstance(my_deer, Deer))
    print(f"Is RedDeer an Animal -", issubclass(RedDeer, Animal))