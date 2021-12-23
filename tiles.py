import items, enemies, actions, world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
    
██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗░██████╗  ░█████╗░███╗░░██╗██████╗░  
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║██╔════╝  ██╔══██╗████╗░██║██╔══██╗  
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║╚█████╗░  ███████║██╔██╗██║██║░░██║  
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║░╚═══██╗  ██╔══██║██║╚████║██║░░██║  
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║██████╔╝  ██║░░██║██║░╚███║██████╔╝  
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  

██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║██╔════╝
██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║╚█████╗░
██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║░╚═══██╗
██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░                                                                  
"""

        """Dungeon Master- " You find yourslef in an overgrown old forest. Before you is a Giant Oak tree spreading its claws
        It warns you "Beware !! This forest has been a home to blood of many warriors
        What Do You Do Next?"
        
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class CollectTreasure(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.SelectWeapon(enemy=self.enemy), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class MonsterAlley(MapTile):
    def intro_text(self):
        return """
        This is the Monster Alley. Beware if you have any kind of Metal 
        """

    def modify_player(self, player):
        # Room has no action on player
        pass

class Dungeon(MapTile):
    def intro_text(self):
        return """
        Ahead lies a Dungeon home to dreadful DRAGONS!.
        """
    def modify_player(self, player):
        # Room has no action on player
        pass

class Forest(MapTile):
    def intro_text(self):
        return """
        Walk through the creepy FOREST to face next challenge!.
        """
    def modify_player(self, player):
        # Room has no action on player
        pass


class RustMonster(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.RustMonster())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A RustMonster jumps in front of you, choose your weapon wisely!
            """
        else:
            return """
            The corpse of a Rustmonster rots on the ground.
            """


class MindFlayer(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MindFlayer())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Mindflayer Paralyses you down!
             """
        else:
            return """
             The corpse of a dead Mindfalyer is on the ground.
             """

class Dragon(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Deadly Dragon spreading its Wings wide is angry at you!
             "You have entered his Dungeon and now he wants to kill you!!"
             
                        /                            )
          (                             |\
         /|                              \\
        //                                \\
       ///                                 \|
      /( \                                  )\
      \\  \_                               //)
       \\  :\__                           ///
        \\     )                         // \
         \\:  /                         // |/
          \\ / \                       //  \
           /)   \   ___..-'           (|  \_|
          //     /   _.'              \ \  \
         /|       \ \________          \ | /
        (| _ _  __/          '-.       ) /.'
         \\ .  '-.__            \_    / / \
          \\_'.     > --._ '.     \  / / /
           \ \      \     \  \     .' /.'
            \ \  '._ /     \ )    / .' |
             \ \_     \_   |    .'_/ __/
              \  \      \_ |   / /  _/ \_
               \  \       / _.' /  /     \
               \   |     /.'   / .'       '-,_
                \   \  .'   _.'_/             \
   /\    /\      ) ___(    /_.'           \    |
  | _\__// \    (.'      _/               |    |
  \/_  __  /--'`    ,                   __/    /
  (_ ) /b)  \  '.   :            \___.-'_/ \__/
  /:/:  ,     ) :        (      /_.'__/-'|_ _ /
 /:/: __/\ >  __,_.----.__\    /        (/(/(/
(_(,_/V .'/--'    _/  __/ |   /
 VvvV  //`    _.-' _.'     \   \
   n_n//     (((/->/        |   /
   '--'         ~='          \  |
                              | |_,,,
                 	             \  \  /
                               '.__)


             
             
             """
        else:
            return """
             The corpse of a dead Dragon is on the ground.
             """

class Goblin(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Goblin guarding the pile of Gold is fast asleep!
             Wake it and you will be dead!
             """
        else:
            return """
             The corpse of a dead Dragon is on the ground.
             """


class FindDaggerRoom(CollectTreasure):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class Gems(CollectTreasure):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice an old Chest 
        It has glass like object overflowing. You take a closer look
        Its a Chest of GEMS!.
        """
class Coins(CollectTreasure):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        A Pile of Gold coins is visible right in front of you.
        """

class EndLevel(MapTile):
    def intro_text(self):
        return """
        You have successfully completed the level,
        
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True