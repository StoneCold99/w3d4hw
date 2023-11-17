class Pokemon:
    def __init__(self, Character, Power, Ability, Color, Weight):
        self.Character = Character
        self.Power = Power
        self.Ability = Ability
        self.Color = Color
        self.Weight = Weight

    def Fight(self):
        print("The Pokemon is in BATTLE!!!")

    def Stop(self):
        print("The Pokemon is Recharging")

my_pokey = Pokemon("Arceus", "the power to create a piece of itself to exist outside of its home dimension", "Multitype", "gray", 706)
my_pokey.Fight()
my_pokey.Stop()
print(my_pokey.Character)
print(my_pokey.Power)
print(my_pokey.Ability)
print(my_pokey.Color)
print(my_pokey.Weight)
# OOP is the creation of objects that has both data and functions. It is a computer programming model that organizes software design around data, or objects, rather than functions and logic.

