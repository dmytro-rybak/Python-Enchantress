ParentClass = type("ParentClass", (), {})

SubClass = type("SubClass", (ParentClass,), {})


class NewClass(SubClass):
    def say_hello(self):
        print("Hello, world!")


if __name__ == '__main__':
    new_object = NewClass()
    new_object.say_hello()
