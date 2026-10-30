class Warrior:

    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:

    def special_move(self):
        print("Mage casts a powerful spell")

class Archer:

    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

Warrior1 = Warrior()
Mage1 = Mage()
Archer1 = Archer()

characters = [Warrior1, Mage1, Archer1]

for character in characters:
    perform_move(character)
