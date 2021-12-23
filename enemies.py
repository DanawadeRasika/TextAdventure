class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class RustMonster(Enemy):
    def __init__(self):
        super().__init__(name="Rust Monster", hp=10, damage=2)


class MindFlayer(Enemy):
    def __init__(self):
        super().__init__(name="Mind Flayer", hp=30, damage=15)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=25, damage=20)


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=15, damage=5)