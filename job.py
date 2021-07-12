import math


class Player(object):
    def __init__(self, name):
        """Creates a player and its stats"""
        self.name = name
        self.job = ""
        self.level = 1
        self.exp_value = 0
        self.maxhp_value = 100
        self.currenthp = 100
        self.patk = 1
        self.matk = 0
        self.mdef = 1
        self.pdef = 1
        self.crit_chance = 10
        self.gold = 0
        self.battle_count = 0

    def level_up(self):
        """Levels up the character"""
        self.level += 1
        self.patk = math.ceil(self.patk * 1.1)
        self.matk = math.ceil(self.matk * 1.1)
        self.pdef = math.ceil(self.pdef * 1.05)
        self.mdef = math.ceil(self.mdef * 1.1)
        self.maxhp_value += 10
        self.currenthp = self.maxhp_value

    def add_exp(self, exp):
        """adds exp when defeating an enemy"""
        self.exp_value += exp

    def add_maxhp(self, add_maxhp):
        """sets the value of maximum hit points"""
        self.maxhp_value += add_maxhp

    def set_currenthp(self, set_hp):
        """Sets current hit points +/- depending on if hit or healed"""
        self.currenthp = set_hp

    def add_patk(self, add_patk):
        """Adds a value of physical attack to the player"""
        self.patk += add_patk

    def add_pdef(self, add_matk):
        """Adds a value of physical defence to the player"""
        self.pdef += add_matk

    def add_matk(self, add_matk):
        """Adds a value of magical attack to the player"""
        self.matk += add_matk

    def add_mdef(self, add_matk):
        """Adds a value of magical defence to the player"""
        self.mdef += add_matk

    def add_crit(self, add_crit):
        """Adds a value of critical chance to the player"""
        self.crit_chance += add_crit

    def add_gold(self, add_gold):
        """Adds a value of gold to the player"""
        self.gold += add_gold

    def add_battle(self):
        """Adds 1 to battle count"""
        self.battle_count += 1

    def reset_hp(self):
        """Resets HP to full"""
        self.currenthp = self.maxhp_value


class Warrior(Player):
    """The warrior class, high physical attack and hp"""
    def __init__(self, name):
        super(Warrior, self).__init__(name)
        self.job = "Warrior"
        self.maxhp_value = 150
        self.currenthp = 150
        self.patk = 30
        self.matk = 0
        self.crit_chance = 10
        self.pdef = 15


class Mage(Player):
    """The mage class, high magic attack"""
    def __init__(self, name):
        super(Mage, self).__init__(name)
        self.job = "Mage"
        self.maxhp_value = 100
        self.currenthp = 100
        self.patk = 1
        self.matk = 45
        self.crit_chance = 10
        self.mdef = 20
        self.pdef = 5


class Archer(Player):
    """The archer class, fast ranged physical attacker"""
    def __init__(self, name):
        super(Archer, self).__init__(name)
        self.job = "Archer"
        self.maxhp_value = 110
        self.currenthp = 110
        self.patk = 40
        self.matk = 0
        self.crit_chance = 25
        self.pdef = 10


class Paladin(Player):
    """The paladin class, high hp and low attack, can heal"""
    def __init__(self, name):
        super(Paladin, self).__init__(name)
        self.job = "Paladin"
        self.maxhp_value = 200
        self.currenthp = 200
        self.patk = 15
        self.matk = 10
        self.crit_chance = 10
        self.pdef = 25
        self.mdef = 10


class Hero(Player):
    """The hero class, strongest class of them all"""
    def __init__(self, name):
        super(Hero, self).__init__(name)
        self.job = "Hero"
        self.maxhp_value = 200000
        self.currenthp = 200000
        self.patk = 5000
        self.matk = 2000
        self.crit_chance = 50
        self.pdef = 2500
        self.mdef = 1000
