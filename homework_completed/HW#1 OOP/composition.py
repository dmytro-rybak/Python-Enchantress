class Laptop:
    def __init__(self):
        os1 = OperatingSystem("Ubuntu", "20.04", "64-bit", "GNOME")
        os2 = OperatingSystem("Windows", "7", "64-bit", "Windows Aero")
        self.operating_systems = [os1, os2]

    def printOS(self):
        print(self.operating_systems)
        for os in self.operating_systems:
            print(f"{os.name} {os.version}, {os.bitness}, gui:{os.gui}")


class OperatingSystem:
    def __init__(self, name, version, bitness, gui):
        self.name = name
        self.version = version
        self.bitness = bitness
        self.gui = gui


if __name__ == '__main__':
    laptop = Laptop()
    laptop.printOS()
