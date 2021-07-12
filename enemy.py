import math


class Enemy(object):
    """Creates an enemy to fight, defines its parameters"""
    def __init__(self):
        self.name = ""
        self.level = 1
        self.hp = 1
        self.maxhp = 1
        self.patk = 1
        self.matk = 0
        self.pdef = 1
        self.mdef = 1
        self.crit_chance = 0
        self.examine = ""
        self.question = ""
        self.threaten = ""
        self.humor = ""

    def reset_hp(self):
        """Reset the hp of the enemy once finished a battle"""
        self.hp = self.maxhp

    def set_level(self, lvl):
        """Set the level of the enemy"""
        self.level = lvl

    def scale_stats(self):
        self.hp = math.ceil(self.hp * (self.level * 0.1))
        self.maxhp = math.ceil(self.maxhp * (self.level * 0.1))
        self.patk = math.ceil(self.patk * (self.level * 0.2))
        self.pdef = math.ceil(self.pdef * (self.level * 0.1))


class TwilightDragon(Enemy):
    """The Twilight Dragon enemy used for the tutorial"""
    def __init__(self):
        super(TwilightDragon, self).__init__()
        self.name = "Twilight Dragon"
        self.level = 100
        self.hp = 200
        self.maxhp = 200
        self.patk = 10000
        self.matk = 50000
        self.pdef = 100
        self.mdef = 100
        self.crit_chance = 35
        self.examine = "A Twilight Dragon, it glows dark purple. Cool."
        self.question = "*ROAR!!!* It roars at you."
        self.threaten = "It breathes purple fire at your feet."
        self.humor = "You swear you heard a chuckle from it."


class Wolf(Enemy):
    """A wolf enemy"""
    def __init__(self):
        super(Wolf, self).__init__()
        self.name = "Wolf"
        self.level = 1
        self.hp = 100
        self.maxhp = 100
        self.patk = 20
        self.pdef = 10
        self.crit_chance = 5
        self.examine = "A grey wolf, it has large fangs."
        self.question = "*It howls*"
        self.threaten = "*It snarls*"
        self.humor = "*It tilts its head*"


class AlphaWolf(Enemy):
    """A wolf enemy, leader of the pack"""
    def __init__(self):
        super(AlphaWolf, self).__init__()
        self.name = "Alpha Wolf"
        self.level = 1
        self.hp = 150
        self.maxhp = 150
        self.patk = 30
        self.pdef = 15
        self.crit_chance = 8
        self.examine = "A big black wolf, looks larger than the others."
        self.question = "I'm here for some good foods."
        self.threaten = "I will crush your cranium."
        self.humor = "It's not even 2018 and it gets offended."


class Gnome(Enemy):
    """A garden gnome"""
    def __init__(self):
        super(Gnome, self).__init__()
        self.name = "Gnome"
        self.level = 1
        self.hp = 300
        self.maxhp = 300
        self.patk = 10
        self.matk = 10
        self.pdef = 15
        self.crit_chance = 3
        self.examine = "It's not a Gnot a Gnelf, it's Gnot a Gnoblin,\
 it's a Gnome! And you've been gnomed!"
        self.question = "*says nothing*"
        self.threaten = "*says nothing*"
        self.humor = "Darn I've been gnomed."


class TheHam(Enemy):
    """Litrally a peice of ham"""
    def __init__(self):
        super(TheHam, self).__init__()
        self.name = "The Ham"
        self.level = 1
        self.hp = 100
        self.maxhp = 100
        self.patk = 25
        self.pdef = 5
        self.crit_chance = 5
        self.examine = "It's a piece of ham."
        self.question = "You ask it how its day was, it says it doesn't\
want to talk about it."
        self.threaten = "I WILL HAM YOU"
        self.humor = "*It explodes, then reforms*"


class DemonicFairy(Enemy):
    """A creepy looking fairy"""
    def __init__(self):
        super(DemonicFairy, self).__init__()
        self.name = "Demonic Fairy"
        self.level = 1
        self.hp = 125
        self.maxhp = 125
        self.patk = 10
        self.pdef = 5
        self.matk = 25
        self.mdef = 10
        self.crit_chance = 3
        self.examine = "You will have nightmares."
        self.question = "I am here for your SOUL!"
        self.threaten = "I am here for your SOUL!"
        self.humor = "I am here for your SOUL!"


class DemonLord(Enemy):
    """The Lord of Demons enemy"""
    def __init__(self):
        super(DemonLord, self).__init__()
        self.name = "Demon Lord"
        self.level = 666
        self.hp = 666
        self.maxhp = 666
        self.patk = 100
        self.matk = 500
        self.pdef = 200
        self.mdef = 150
        self.crit_chance = 20
        self.examine = "Has horns and tail. as name suggests, it is a demon."
        self.question = "It breathes fire, that just raises more questions."
        self.threaten = "Threatining does nothing, it stands at 20 ft tall."
        self.humor = "It laughs, rumbling the ground and echos around you."


class MutilatedTroll(Enemy):
    """The Mutilated Troll enemy used as a bossfight"""
    def __init__(self):
        super(MutilatedTroll, self).__init__()
        self.name = "Mutilated Troll"
        self.level = 120
        self.hp = 10000
        self.maxhp = 10000
        self.patk = 80
        self.matk = 20
        self.pdef = 60
        self.mdef = 20
        self.crit_chance = 60
        self.examine = "It is a troll, but very gibbled. Odd."
        self.question = "It speaks troll as an answer. You don't understand."
        self.threaten = "It cowers in fear."
        self.humor = "It tilts its head in confusion."

class EvilWizard(Enemy):
    """The Mutilated Troll enemy used as a bossfight"""
    def __init__(self):
        super(EvilWizard, self).__init__()
        self.name = "Evil Wizard"
        self.level = 60
        self.hp = 6000
        self.maxhp = 6000
        self.patk = 15
        self.matk = 120
        self.pdef = 15
        self.mdef = 20
        self.crit_chance = 20
        self.examine = "A magical wizard, you can tell it is evil."
        self.question = "It replies 'You cannot question me!'"
        self.threaten = "Nothing you say can threaten him."
        self.humor = "He chortles as you say some magic pun."
