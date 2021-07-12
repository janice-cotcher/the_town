class Armor(object):
    """Creates a piece of armor and its parameters"""
    def __init__(self):
        self.name = ""
        self.rarity = ""
        self.pdef_value = 0
        self.mdef_value = 0
        self.increase_crit = 0
        self.desc = ""

    def holy_guard(self):
        """Knight armor for the tutorial"""
        self.name = "Holy Guard's Armor"
        self.rarity = "Legendary"
        self.pdef_value = 100
        self.mdef_value = 200
        self.increase_crit = 5
        self.desc = "Armor of the Holy Guard, made of unknown materials."

    def default_plate(self):
        """default plate armor for the paladin class"""
        self.name = "Default Plate Armor"
        self.rarity = "Common"
        self.pdef_value = 20
        self.mdef_value = 5
        self.increase_crit = 0
        self.desc = "An old piece of iron armor, it's pretty heavy."

    def default_leather(self):
        """default leather armor for the archer class"""
        self.name = "Default Leather Armor"
        self.rarity = "Common"
        self.pdef_value = 10
        self.mdef_value = 1
        self.increase_crit = 3
        self.desc = "A worn piece of leather clothing, smells terrible"

    def default_cloth(self):
        """default cloth armor for the mage class"""
        self.name = "Default Cloth Armor"
        self.rarity = "Common"
        self.pdef_value = 5
        self.mdef_value = 15
        self.increase_crit = 0
        self.desc = "A robe with weak enchantments for magic protection"

    def default_chain(self):
        """default chain mail armor for the warrior class"""
        self.name = "Default Chain Mail Armor"
        self.rarity = "Common"
        self.pdef_value = 15
        self.mdef_value = 2
        self.increase_crit = 0
        self.desc = "A rusty piece of chain mail, old and discoloured"

    def hk_armor(self):
        """default plate armor for the paladin class"""
        self.name = "Holy Knight's Armor"
        self.rarity = "Common"
        self.pdef_value = 40
        self.mdef_value = 10
        self.increase_crit = 0
        self.desc = "Armor of the Holy Guard, you feel the light flowing."

    def lux_leather_jkt(self):
        """default leather armor for the archer class"""
        self.name = "Luxury Leather Jacket"
        self.rarity = "Uncommon"
        self.pdef_value = 15
        self.mdef_value = 1
        self.increase_crit = 5
        self.desc = "A fancy leather jacket, feels sturdy."

    def gm_robe(self):
        """default cloth armor for the mage class"""
        self.name = "Grand Mage's Robe"
        self.rarity = "Uncommon"
        self.pdef_value = 8
        self.mdef_value = 30
        self.increase_crit = 0
        self.desc = "The robe of an accomplished mage, has many enchantments."

    def knight_chain(self):
        """default chain mail armor for the warrior class"""
        self.name = "Knight's Chainmail"
        self.rarity = "unommon"
        self.pdef_value = 25
        self.mdef_value = 2
        self.increase_crit = 0
        self.desc = "Durable chainmail, can block many attacks."
