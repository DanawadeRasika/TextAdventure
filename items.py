# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name  # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt  # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Crossbow(Weapon):
    def __init__(self):
        super().__init__(name="Crossbow",
                         description="Crossbow can target a enemy from far .",
                         value=2,
                         damage=7)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Battleaxe(Weapon):
    def __init__(self):
        super().__init__(name="Battleaxe",
                         description="Battleaxe that can even slit through a rock .",
                         value=7,
                         damage=15)