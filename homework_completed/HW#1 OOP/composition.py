class Laptop:
    def __init__(self, operating_systems):
        self.operating_systems = operating_systems

    def display_info(self):
        print("Operating systems on this laptop:")
        for os in self.operating_systems:
            print(" ", os)


class OperatingSystem:
    def __init__(self, name, version, bitness, gui):
        self.name = name
        self.version = version
        self.bitness = bitness
        self.gui = gui

    def __str__(self):
        return f"{self.name} {self.version}, {self.bitness}, gui:{self.gui}"


if __name__ == '__main__':
    laptop1 = Laptop([OperatingSystem("Ubuntu", "20.04", "64-bit", "Gnome"),
                     OperatingSystem("Windows", "7", "64-bit", "Windows Aero")])
    laptop1.display_info()
    print("")
    laptop2 = Laptop([OperatingSystem("Linux Mint", "20", "64-bit", "Cinnamon")])
    laptop2.display_info()
