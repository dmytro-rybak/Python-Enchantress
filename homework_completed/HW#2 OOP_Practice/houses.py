import random


class Person:
    def __init__(self, name, age, money, house=None, having_home=False):
        self.name = name
        self.age = age
        self.money = money
        self.house = house
        self.having_home = having_home

    def display_info(self):
        if self.having_home:
            print(f"Hi, my name is {self.name}, I'm {self.age} and "
                  f"I have {self.money}$ and beautiful house!")
        else:
            print(f"Hi, my name is {self.name}, I'm {self.age} and "
                  f"I have {self.money}$ and don't having own house...")

    def make_money(self):
        self.money += 4000

    def buy_a_house(self, house):
        if not self.having_home:
            if house.cost <= self.money:
                self.house = house
                self.having_home = True
                self.money -= house.cost
                self.house.owners += 1
                house_list.remove(house)
            else:
                print("You don't have money for this house!")
        else:
            print("You already have own house")

    def upgrade_house(self):
        if self.having_home:
            self.money -= 3000
            self.house.cost += 5000
        else:
            print("You don't having own house!")

    def sell_a_house(self):
        if self.having_home:
            house_list.append(self.house)
            self.money += self.house.cost
            self.house = None
            self.having_home = False
        else:
            print("You don't having own house!")


class House:
    def __init__(self, house_id, area, cost, owners=0):
        self.house_id = house_id
        self.area = area
        self.cost = cost
        self.owners = owners

    def __str__(self):
        return f"#{self.house_id}. House with {self.area} square meters. " \
               f"It cost {self.cost}$. And it had {self.owners} owners"


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name, houses, client: Person, discount):
        self.name = name
        self.houses = houses
        self.client = client
        self.discount = discount

    def display_info_about_houses(self):
        print(f"\nHey, I'm realtor Tomas. I have such houses for sell:")
        print("\t" + "*" * 70)
        for house in house_list:
            print("\t", house)
        print("\t" + "*" * 70 + "\n")

    def give_discount(self, house: House):
        if house.area <= 40:
            house.cost -= realtor_discount

    def steal_money(self):
        number = random.randrange(1, 10)
        if number == 5:
            self.client.money = 0
            print("Ha-ha. I steal your money!")
        else:
            print("No. I'm honest realtor")


if __name__ == '__main__':
    # testing data
    house_list = [House(1, 50, 45000),
                  House(2, 35, 30000),
                  House(3, 80, 100000)]
    realtor_discount = 3000
    person1 = Person("Tyler Jones", 25, 40000)
    realtor = Realtor("Tomas", house_list, person1, realtor_discount)

    # try to buy very expensive house
    realtor.display_info_about_houses()
    house_for_sell = house_list[0]
    person1.display_info()
    person1.buy_a_house(house_for_sell)
    print()

    # successfully buying house
    new_house_for_sell = house_list[1]
    realtor.give_discount(new_house_for_sell)
    person1.buy_a_house(new_house_for_sell)
    person1.display_info()
    print(f"\tHouse: {person1.house}")
    # realtor.display_info_about_houses()

    # upgrade house
    person1.make_money()
    person1.make_money()
    person1.upgrade_house()
    print(f"\tHouse: {person1.house}")
    person1.display_info()
    realtor.display_info_about_houses()

    # sell house
    person1.sell_a_house()
    person1.display_info()

    # steal the money
    realtor.display_info_about_houses()
    person2 = Person("Mike Smith", 20, 25000)
    person2.display_info()
    realtor.client = person2
    realtor.steal_money()
    person2.display_info()
