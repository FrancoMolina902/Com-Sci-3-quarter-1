class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, material):
        super().__init__(material)


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Glass"),
            Beaker("Glass"),
            Beaker("Glass"),
            Beaker("Glass"),
            Beaker("Glass")
        ]


tray = Tray()

print("Tray contains beakers")

del tray

print("Tray deleted")
