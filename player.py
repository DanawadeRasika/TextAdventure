import random
import items, world

weapon_selected= None
class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Battleaxe(), items.Crossbow()]  # Inventory on startup
        self.hp = 100  # Health Points
        self.location_x, self.location_y = world.starting_position  # (0, 0)
        self.victory = False  # no victory on start up

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0  # Greater than zero value then you are still alive

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def select_weapon(self,enemy):
        print("\nChoose from any of the below weapon.\n")

        weapon_list= []
        for item in self.inventory:
            if isinstance(item,items.Weapon):
                weapon_list.append(item)
        i=1
        for weapon in weapon_list:
            print(i,".", weapon.name, sep='')
            i+=1

        while True:
            itemChoice = int(input("""\nSelect from your choice of weapon:""")) - 1
            if itemChoice not in range(0,len(weapon_list)):
                print("\nInvalid weapon choice")
                continue
            break
        print('\n')
        print(weapon_list[itemChoice].name, "equipped.\n")
        self.currentweapon = weapon_list[itemChoice]




    #def attack(self, enemy):

        """max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    self.currentweapon = i"""

        print("You use {} against {}!".format(self.currentweapon, enemy.name))
        enemy.hp -= self.currentweapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def attack(self, enemy):
        """weapon_list = []
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapon_list.append(item)
        itemChoice=1
        print(weapon_list[itemChoice].name, "equipped.\n")
        self.currentweapon = weapon_list[itemChoice]"""
        global weapon_selected
        if weapon_selected == None:
            for item in self.inventory:
                weapon_selected = item
            print("You use {} against {}!".format(weapon_selected, enemy.name))
            enemy.hp -= weapon_selected.damage
            if not enemy.is_alive():
                print("You killed {}!".format(enemy.name))
            else:
                print("{} HP is {}.".format(enemy.name, enemy.hp))
        else:
            print("You use {} against {}!".format(self.currentweapon, enemy.name))
            enemy.hp -= self.currentweapon.damage
            if not enemy.is_alive():
                print("You killed {}!".format(enemy.name))
            else:
                print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)