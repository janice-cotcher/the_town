class Weapons(object):
    """creates a weapon and its parameters"""
    def __init__(self):
        self.name = ""
        self.rarity = ""
        self.patk_value = 1
        self.matk_value = 0
        self.increase_crit = 0
        self.desc = ""

    def excalibur(self):
        """The Excalibur for the hero"""
        self.name = "Holy Sword Excalibur"
        self.rarity = "Legendary"
        self.patk_value = 1000
        self.value = 9999
        self.increase_crit = 10
        self.desc = "The extremely powerful holy sword, glows as you weave it."

    def default_sword(self):
        """changes the weapon to the default sword"""
        self.name = "Default Sword"
        self.rarity = "Common"
        self.patk_value = 6
        self.desc = "A weak blade, looks old and worn."

    def default_bow(self):
        """changes the weapon to the default bow"""
        self.name = "Default Bow"
        self.rarity = "Common"
        self.patk_value = 4
        self.increase_crit = 3
        self.desc = "An old wooden bow, it seems like it's going to snap"

    def default_staff(self):
        """changes the weapon to the default staff"""
        self.name = "Default Staff"
        self.rarity = "Common"
        self.patk_value = 1
        self.matk_value = 10
        self.desc = "An old staff you found on the ground."

    def default_mace(self):
        """changes the weapon to the default mace"""
        self.name = "Default Mace"
        self.rarity = "Common"
        self.patk_value = 5
        self.desc = "A used mace you got from your parents, functional."

    def magn_staff(self):
        """changes the weapon to the Magnificent Staff"""
        self.name = "Magnificent Staff"
        self.rarity = "Uncommon"
        self.patk_value = 2
        self.matk_value = 20
        self.desc = "A brand new staff, smells of fresh pine."

    def st_blade(self):
        """changes the weapon to the upgraded sword"""
        self.name = "Steel Cutting Blade"
        self.rarity = "Uncommon"
        self.patk_value = 10
        self.desc = "A shiny blade that can cut steel with little effort."

    def longbow(self):
        """changes the weapon to the longbow"""
        self.name = "Longbow"
        self.rarity = "Uncommon"
        self.patk_value = 8
        self.increase_crit = 5
        self.desc = "A large, powerful bow with great range."

    def holy_hammer(self):
        """changes the weapon to the Holy Hammer"""
        self.name = "Holy Hammer"
        self.rarity = "Uncommon"
        self.patk_value = 7
        self.matk_value = 5
        self.desc = "Hammer of the Holy Order, glows with light."
