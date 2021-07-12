import time
import math
import random
import json
import os.path

from job import Player, Warrior, Mage, Archer, Paladin, Hero
from weapons import Weapons
from armor import Armor
from enemy import (Enemy,
                   TwilightDragon,
                   Wolf,
                   AlphaWolf,
                   DemonLord,
                   MutilatedTroll,
                   EvilWizard,
                   Gnome,
                   TheHam,
                   DemonicFairy)


def player_info():
    """Creates a dict of all of the player's parameters and creates a neat
    list"""
    stats = {
        "Name": player1.name,
        "Class": player1.job,
        "Level": player1.level,
        "EXP": player1.exp_value,
        "Gold": player1.gold,
        "HP": player1.currenthp,
        "Current Weapon": "{}; {} item\n PATK +{}, MATK +{} Crit% + {}\n {}".format(
            equipped.name,
            equipped.rarity,
            equipped.patk_value,
            equipped.matk_value,
            equipped.increase_crit,
            equipped.desc),
        "Current Armor": "{}; {} item\n PDEF +{}, MDEF +{} Crit% + {}\n {}".format(
            equipped_armor.name,
            equipped_armor.rarity,
            equipped_armor.pdef_value,
            equipped_armor.mdef_value,
            equipped_armor.increase_crit,
            equipped_armor.desc),
        "Max HP": player1.maxhp_value,
        "PATK": player1.patk,
        "MATK": player1.matk,
        "PDEF": player1.pdef,
        "MDEF": player1.mdef,
        "Crit Chance": str(player1.crit_chance) + "%",
     }
    text = "_______________________________\n"
    for i in stats:
        text += str(i) + ": " + str(stats[i]) + "\n"
    text += "_______________________________"
    return text


def print_inv(inva):
    """Print a dictionary in a neat list,
     used for store and player inventory"""
    text = "_______________________________\n"
    for i in inva:
        text += str(i).title() + ": " + str(inva[i]) + "\n"
    text += "_______________________________"
    return text


def equip_item(type):
    """equips an item"""
    if type == "weapon":
        player1.patk += equipped.patk_value
        player1.matk += equipped.matk_value
        player1.crit_chance += equipped.increase_crit
    if type == "armor":
        player1.pdef += equipped_armor.pdef_value
        player1.mdef += equipped_armor.mdef_value
        player1.crit_chance += equipped_armor.increase_crit


def dequip_item(type):
    """dequips an item"""
    if type == "weapon":
        player1.patk -= equipped.patk_value
        player1.matk -= equipped.matk_value
        player1.crit_chance -= equipped.increase_crit
    if type == "armor":
        player1.pdef -= equipped_armor.pdef_value
        player1.mdef -= equipped_armor.mdef_value
        player1.crit_chance -= equipped_armor.increase_crit


def check_input(cmd, commands):
    """check to see if the user input is in the command dictionary"""
    if cmd in commands:
        return True
    else:
        return False


def use_item(cmd):
    """Use an item during battle phase. item must be available and
    quantity must be > 0. Increases HP depending on which item is used."""
    potions = {
        "potion": "",
        "super potion": "",
        "mega potion": "",
        "giga potion": "",
    }
    if cmd == "inv":
        msg = print_inv(inv)
    elif cmd in potions and cmd in inv:
        if inv[cmd] == 0:
            msg = "You don't have that item!"
        elif cmd == "potion":
            player1.currenthp += 10
            inv["potion"] -= 1
            if player1.currenthp >= player1.maxhp_value:
                player1.currenthp = player1.maxhp_value
                msg = "You have been healed to full health!\n"
                msg += "-----------------------------"
            else:
                msg = "You have been healed for 10 HP!\n"
                msg += "You now have {} HP!\n".format(player1.currenthp)
                msg += "-----------------------------"
        elif cmd == "super potion":
            player1.currenthp += 50
            inv["super potion"] -= 1
            if player1.currenthp >= player1.maxhp_value:
                player1.currenthp = player1.maxhp_value
                msg = "You have been healed to full health!\n"
                msg += "-----------------------------"
            else:
                msg = "You have been healed for 50 HP!\n"
                msg += "You now have {} HP!\n".format(player1.currenthp)
                msg += "-----------------------------"
        elif cmd == "mega potion":
            player1.currenthp += 100
            inv["mega potion"] -= 1
            if player1.currenthp >= player1.maxhp_value:
                player1.currenthp = player1.maxhp_value
                msg = "You have been healed to full health!\n"
                msg += "-----------------------------"
            else:
                msg = "You have been healed for 100 HP!\n"
                msg += "You now have {} HP!\n".format(player1.currenthp)
                msg += "-----------------------------"
        elif cmd == "giga potion":
            player1.currenthp += 1000
            inv["giga potion"] -= 1
            if player1.currenthp >= player1.maxhp_value:
                player1.currenthp = player1.maxhp_value
                msg = "You have been healed to full health!\n"
                msg += "-----------------------------"
            else:
                msg = "You have been healed for 1000 HP!\n"
                msg += "You now have {} HP!\n".format(player1.currenthp)
                msg += "-----------------------------"
    else:
        msg = "You don't have that item!"
    return msg


def pattack():
    """The player attacks the enemy"""
    dmg = player1.patk - enemy.pdef
    if dmg <= 0:
        dmg = 1
    crit_factor = random.randint(1, 100)
    if crit_factor <= player1.crit_chance:
        dmg = math.ceil(dmg * 1.5)
        print("Critical Hit!!!")
    enemy.hp -= dmg
    text = "You did {} physical damage!\n".format(dmg)
    text += "The {} has {} HP left!".format(enemy.name, enemy.hp)
    return text


def mattack():
        """The player attacks the enemy with magic"""
        dmg = player1.matk - enemy.mdef
        if dmg <= 0:
            dmg = 1
        crit_factor = random.randint(1, 100)
        if crit_factor <= player1.crit_chance:
            dmg = math.ceil(dmg * 1.5)
            print("Critical Hit!!!")
        enemy.hp -= dmg
        text = "You did {} magical damage!\n".format(dmg)
        text += "The {} has {} HP left!".format(enemy.name, enemy.hp)
        return text


def enemy_pattack():
    """The enemy attacks the player"""
    dmg = enemy.patk - player1.pdef
    if dmg <= 0:
        dmg = 1
    crit_factor = random.randint(1, 100)
    if crit_factor <= enemy.crit_chance:
        dmg = math.ceil(dmg * 1.5)
        print("Critical Hit!!!")
    player1.currenthp -= dmg
    text = "{} did {} physical damage!\n".format(enemy.name, dmg)
    text += "You have {} HP left!".format(player1.currenthp)
    return text


def enemy_mattack():
    """The enemy attacks the player with magic"""
    dmg = enemy.matk - player1.mdef
    if dmg <= 0:
        dmg = 1
    crit_factor = random.randint(1, 100)
    if crit_factor <= enemy.crit_chance:
        dmg = math.ceil(dmg * 1.5)
        print("Critical Hit!!!")
    player1.currenthp -= dmg
    text = "{} did {} magical damage!\n".format(enemy.name, dmg)
    text += "You have {} HP left!".format(player1.currenthp)
    return text


def gain_exp():
    """Adds a calculated amount of EXP/gold and
    levels up the character accordingly and adds gold"""
    gain = random.randint(100, 400)
    gain = math.ceil(gain * (enemy.level / player1.level))
    gold_gain = random.randint(25, 50)
    gold_gain *= player1.level
    player1.add_gold(gold_gain)
    player1.add_exp(gain)
    print("You have gained {} EXP!".format(gain))
    print("You have found {} Gold!".format(gold_gain))
    if player1.exp_value >= 1000:
        dequip_item("weapon")
        dequip_item("armor")
        player1.level_up()
        equip_item("weapon")
        equip_item("armor")
        player1.exp_value -= 1000
        print("You have leveled up to level {}!".format(player1.level))
        print("Here are your new stats: ")
        print(player_info())


def drop_item():
    """Calculates what items can be dropped by what level enemy
    and adds it to the player's inventory based on a percentage."""
    drop_chance = random.randint(1, 100)
    if 1 <= enemy.level < 10:
        if drop_chance <= 30:
            inv["potion"] += 1
            print("You have found a potion!")
    elif 10 <= enemy.level < 20:
        if drop_chance <= 30:
            inv["potion"] += 1
            print("You have found a potion!")
        elif 30 < drop_chance <= 50:
            inv["super potion"] += 1
            print("You have found a super potion!")
    elif 20 <= enemy.level < 35:
        if drop_chance <= 30:
            inv["potion"] += 1
            print("You have found a potion!")
        elif 30 < drop_chance <= 50:
            inv["super potion"] += 1
            print("You have found a super potion!")
        elif 50 < drop_chance <= 65:
            inv["mega potion"] += 1
            print("You have found a mega potion!")
    else:
        if drop_chance <= 30:
            inv["potion"] += 1
            print("You have found a potion!")
        elif 30 < drop_chance <= 50:
            inv["super potion"] += 1
            print("You have found a super potion!")
        elif 50 < drop_chance <= 65:
            inv["mega potion"] += 1
            print("You have found a mega potion!")
        elif 65 < drop_chance <= 75:
            inv["giga potion"] += 1
            print("You have found a giga potion!")


def help():
    """Prints a list of the command"""
    help_commands = {
        "pattack": "Attack the enemy with your weapon.",
        "mattack": "Attack the enemy with magical spells.",
        "item": "Use an item from your inventory",
        "inv": "Display your inventory",
        "stats": "Display your character's parameters",
        "examine": "Examine the enemy.",
        "threaten": "Threaten the enemy.",
        "question": "Question the enemy",
        "humor": "Tell a funny joke",
    }
    text = "_______________________________\n"
    for i in help_commands:
        text += "{}: {}\n".format(i, help_commands[i])
    text += "_______________________________"
    return text


def battle():
    """
    This is the battle phase, the player engages with an enemy.
    The loop checks for valid input and then outputs string and changes values
    according to what the user does. The user will continue to battle until
    either the player or enemy hp is 0. If the enemy hp gets to 0 the player
    gain gold and exp. If the player hp gets to 0 the program types a
    message then quits
    """
    while True:
        print("_______________________________")
        print("What will you do?")
        cmd = input().lower()
        if check_input(cmd, commands):
            if cmd == "item":
                valid = inv["potion"] + inv["super potion"] +\
                inv["mega potion"] + inv["giga potion"]
                if valid == 0:
                    print("You don't own any items!")
                else:
                    print("Type 'inv' to display your inventory")
                    print("What would you like to use?")
                    while True:
                        cmd = input().lower()
                        msg = use_item(cmd)
                        print(msg)
                        if msg != "You don't have that item!" and cmd != "inv":
                            break
                    if enemy.matk != 0:
                        rng = random.randint(1, 2)
                        if rng == 1:
                            print(enemy_pattack())
                            print("-----------------------------")
                            time.sleep(1.5)
                            if player1.currenthp <= 0:
                                death_msg()
                        if rng == 2:
                            print(enemy_mattack())
                            print("-----------------------------")
                            time.sleep(1.5)
                            if player1.currenthp <= 0:
                                death_msg()
                    else:
                        print(enemy_pattack())
                        print("-----------------------------")
                        time.sleep(1.5)
                        if player1.currenthp <= 0:
                            death_msg()
            elif cmd == "inv":
                print(print_inv(inv))
            elif cmd == "pattack":
                print("You attack the enemy with your weapon!")
                print("-----------------------------")
                time.sleep(1.5)
                print(pattack())
                print("-----------------------------")
                time.sleep(1.5)
                if enemy.hp <= 0:
                    drop_item()
                    gain_exp()
                    break
                else:
                    if enemy.matk != 0:
                        rng = random.randint(1, 2)
                        if rng == 1:
                            print(enemy_pattack())
                            print("-----------------------------")
                            time.sleep(1.5)
                            if player1.currenthp <= 0:
                                death_msg()
                        if rng == 2:
                            print(enemy_mattack())
                            print("-----------------------------")
                            time.sleep(1.5)
                            if player1.currenthp <= 0:
                                death_msg()
                    else:
                        print(enemy_pattack())
                        print("-----------------------------")
                        time.sleep(1.5)
                        if player1.currenthp <= 0:
                            death_msg()
            elif cmd == "mattack":
                if player1.matk != 0:
                    print("You attack the enemy with magic!")
                    print("-----------------------------")
                    time.sleep(1.5)
                    print(mattack())
                    print("-----------------------------")
                    time.sleep(1.5)
                    if enemy.hp <= 0:
                        drop_item()
                        gain_exp()
                        break
                    else:
                        if enemy.matk != 0:
                            rng = random.randint(1, 2)
                            if rng == 1:
                                print(enemy_pattack())
                                print("-----------------------------")
                                time.sleep(1.5)
                                if player1.currenthp <= 0:
                                    death_msg()
                            if rng == 2:
                                print(enemy_mattack())
                                print("-----------------------------")
                                time.sleep(1.5)
                                if player1.currenthp <= 0:
                                    death_msg()
                        else:
                            print(enemy_pattack())
                            print("-----------------------------")
                            time.sleep(1.5)
                            if player1.currenthp <= 0:
                                death_msg()
                else:
                    print("You have no magical abilities!")
                    time.sleep(1.5)
            else:
                print(commands[cmd])
                time.sleep(1.5)
        else:
            print("You can't do that!")
            time.sleep(1.5)


def load_items(wep, arm):
    if wep == "Default Sword":
        equipped.default_sword()
    elif wep == "Default Staff":
        equipped.default_staff()
    elif wep == "Default Bow":
        equipped.default_bow()
    elif wep == "Default Mace":
        equipped.default_mace()
    elif wep == "Magnificent Staff":
        equipped.magn_staff()
    elif wep == "Steel Cutting Blade":
        equipped.st_blade()
    elif wep == "Longbow":
        equipped.longbow()
    elif wep == "Holy Hammer":
        equipped.holy_hammer()
    if arm == "Default Plate Armor":
        equipped_armor.default_plate()
    elif arm == "Default Leather Armor":
        equipped_armor.default_leather()
    elif arm == "Default Cloth Armor":
        equipped_armor.default_cloth()
    elif arm == "Default Chain Mail Armor":
        equipped_armor.default_chain()
    elif arm == "Holy Knight's Armor":
        equipped_armor.hk_armor()
    elif arm == "Luxury Leather Jacket":
        equipped_armor.lux_leather_jkt()
    elif arm == "Grand Mage's Robe":
        equipped_armor.gm_robe()
    elif arm == "Knight's Chainmail":
        equipped_armor.knight_chain()


def save_game():
    """Save the game, stores the parameters and inventroy into a text file"""
    stats = {
        "Name": player1.name,
        "Class": player1.job,
        "Level": player1.level,
        "EXP": player1.exp_value,
        "Gold": player1.gold,
        "HP": player1.currenthp,
        "Current Weapon": equipped.name,
        "Current Armor": equipped_armor.name,
        "Max HP": player1.maxhp_value,
        "PATK": player1.patk,
        "MATK": player1.matk,
        "PDEF": player1.pdef,
        "MDEF": player1.mdef,
        "Crit Chance": player1.crit_chance,
        "Battle Count": player1.battle_count
     }
    with open("savegame.txt", "w") as f:
        f.write(json.dumps(stats))
    with open("savegame.txt", "a+") as f:
        f.write("\n" + json.dumps(inv))


def load_game():
    """Loads the game and replaces
    inventory/parameters from that of save file"""
    with open("savegame.txt", "r") as f:
        lines = f.readlines()
        parameters = json.loads(lines[0])
        inv = json.loads(lines[1])
        player1.name = parameters["Name"]
        player1.job = parameters["Class"]
        player1.level = parameters["Level"]
        player1.exp_value = parameters["EXP"]
        player1.gold = parameters["Gold"]
        player1.currenthp = parameters["HP"]
        player1.maxhp_value = parameters["Max HP"]
        player1.patk = parameters["PATK"]
        player1.matk = parameters["MATK"]
        player1.pdef = parameters["PDEF"]
        player1.mdef = parameters["MDEF"]
        player1.crit_chance = parameters["Crit Chance"]
        player1.battle_count = parameters["Battle Count"]
        loaded_wep = parameters["Current Weapon"]
        loaded_ar = parameters["Current Armor"]
        load_items(loaded_wep, loaded_ar)
    return inv


def death_msg():
    """Set of actions that occur when the player dies"""
    print("I guess this is the end...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("YOU HAVE DIED")
    time.sleep(5)
    print("*Please relaunch and load your last save file*")
    time.sleep(3)
    print("Quitting game...")
    time.sleep(3)
    quit()


def def_commands():
    """Defines the commands dictionary so the
     dictionary can be updated with recent stats"""
    commands = {
        "pattack": "",
        "mattack": "",
        "self": player_info(),
        "examine": enemy.examine,
        "question": enemy.question,
        "threaten": enemy.threaten,
        "humor": enemy.humor,
        "help": help(),
        "inv": "",
        "item": ""
    }
    return commands


def drop_equip():
    """Allows a new weapon to be found, if weapon is
    already in use upgrades it"""
    chance = random.randint(1, 100)
    chance2 = random.randint(1, 100)
    if player1.job == "Mage":
        if chance <= 10:
            if equipped.name == "Magnificent Staff":
                dequip_item("weapon")
                equipped.matk_value += 10
                equip_item("weapon")
                print("You have upgraded your weapon!")
            else:
                print("You have found a Magnificent Staff\
 and replaced your old staff")
                dequip_item("weapon")
                equipped.magn_staff()
                equip_item("weapon")
    elif player1.job == "Warrior":
        if chance <= 10:
            if equipped.name == "Steel Cutting Blade":
                dequip_item("weapon")
                equipped.patk_value += 10
                equip_item("weapon")
                print("You have upgraded your weapon!")
            else:
                print("You have found a Steel Cutting Blade\
 and replaced your old sword")
                dequip_item("weapon")
                equipped.st_blade()
                equip_item("weapon")
    elif player1.job == "Archer":
        if chance <= 10:
            if equipped.name == "Longbow":
                dequip_item("weapon")
                equipped.patk_value += 8
                equipped.increase_crit += 1
                equip_item("weapon")
                print("You have upgraded your weapon!")
            else:
                print("You have found a Longbow\
 and replaced your old bow")
                dequip_item("weapon")
                equipped.longbow()
                equip_item("weapon")
    elif player1.job == "Paladin":
        if chance <= 10:
            if equipped.name == "Holy Hammer":
                dequip_item("weapon")
                equipped.patk_value += 6
                eqippped.matk_value += 5
                equip_item("weapon")
                print("You have upgraded your weapon!")
            else:
                print("You have found a Holy Hammer\
 and replaced your old mace")
                dequip_item("weapon")
                equipped_.holy_hammer()
                equip_item("weapon")
    if player1.job == "Mage":
        if chance2 <= 10:
            if equipped_armor.name == "Grand Mage's Robe":
                dequip_item("armor")
                equipped_armor.mdef_value += 5
                equip_item("armor")
                print("You have upgraded your Armor!")
            else:
                print("You have found a Grand Mage's Robe\
 and replaced your old robe")
                dequip_item("armor")
                equipped_armor.gm_robe()
                equip_item("armor")
    elif player1.job == "Warrior":
        if chance2 <= 10:
            if equipped_armor.name == "Knight's Chainmail":
                dequip_item("armor")
                equipped_armor.pdef_value += 5
                equip_item("armor")
                print("You have upgraded your Armor!")
            else:
                print("You have found a Knight's Chainmail\
 and replaced your old armor")
                dequip_item("armor")
                equipped_armor.knight_chain()
                equip_item("armor")
    elif player1.job == "Archer":
        if chance2 <= 10:
            if equipped_armor.name == "Luxury Leather Jacket":
                dequip_item("armor")
                equipped_armor.pdef_value += 3
                equipped_armor.increase_crit += 1
                equip_item("armor")
                print("You have upgraded your Armor!")
            else:
                print("You have found a Luxury Leather Jacket\
 and replaced your old leather armor")
                dequip_item("armor")
                equipped_armor.lux_leather_jkt()
                equip_item("armor")
    elif player1.job == "Paladin":
        if chance2 <= 10:
            if equipped_armor.name == "Holy Guard's Armor":
                dequip_item("armor")
                equipped_armor.pdef_value += 5
                equipped_armor.mdef_value += 2
                equip_item("armor")
                print("You have upgraded your Armor!")
            else:
                print("You have found a Holy Guard's Armor\
 and rpelaced your old armor")
                dequip_item("armor")
                equipped_armor.hk_armor()
                equip_item("armor")


# A list of enemies to fight when battling
enemy_list = {
    1: Wolf(),
    2: AlphaWolf(),
    3: Gnome(),
    4: TheHam(),
    5: DemonicFairy()
}
# Create the base enemy
enemy = Enemy()
# Create the base player
player1 = Player("none")
# Create base weapon
equipped = Weapons()
# Create base Armor
equipped_armor = Armor()
# Create the initial inventory
inv = {
    "potion": 0,
    "super potion": 0,
    "mega potion": 0,
    "giga potion": 0
}
# Commands for the user to use during battle
commands = def_commands()
print("North of Acheron")
print("A text-based RPG")
print("Created by: Vincent Li")
print("_________________________")
while True:
    print("Would you like to start a new game or load a saved one?")
    print("Type 'new game' to start a new game and 'load' to continue.")
    print("Press ctrl + c + ENTER to stop the program at any time.")
    cmd = input().lower()
    """Everything in the first if statement is the tutorial,
     it walks the user through how to play the game.
     If the user already has a save game it loads the game in the next
      elif statements and skips the tutorial"""
    if cmd == "new game" or cmd == "newgame":
        print("Welcome to the world of Phezeron")
        time.sleep(3)
        print("I have high hopes for you...")
        time.sleep(3)
        print("Before you go you must learn how to fight.")
        time.sleep(3)
        print("In this game you type commands to do certain actions.")
        time.sleep(3)
        print("Let's give it a shot, your first enemy is the Twilight Dragon.")
        time.sleep(3)
        print("Don't worry...")
        time.sleep(3)
        print("I'll let you borrow the HERO class for this.")
        time.sleep(3)
        # Initilize the hero class for the tutorial
        player1 = Hero("Arthur")
        # Initialize the equipped weapon
        equipped = Weapons()
        equipped.excalibur()
        equip_item("weapon")
        # Initialize the armor weapon
        equipped_armor = Armor()
        equipped_armor.holy_guard()
        equip_item("armor")
        # Enemy that is currently being fought
        enemy = TwilightDragon()
        # Create a dictionary for the inventory
        inv = {
            "potion": 6,
            "super potion": 0,
            "mega potion": 0,
            "giga potion": 0
        }
        commands = def_commands()
        print("*The Twilight Dragon has appeared*")
        time.sleep(3)
        print("Let's begin, here are your available commands:")
        time.sleep(3)
        print(help())
        print("Press ENTER to continue...")
        input()
        print("You can type 'help' anytime in a battle to see the list.")
        time.sleep(3)
        print("Let's start by attacking, there are 2 types of attacks.")
        time.sleep(3)
        print("Physical attacks which use the 'PATK' parameter")
        print("and magical attacks which use the 'MATK' parameter.")
        time.sleep(3)
        print("Attack the Dragon with your sword! Type 'pattack'")
        while True:
            # cmd will be the var for user input for the whole code
            cmd = input().lower()
            """Walks the user through how to to a physical attack,
            will not proceed until the user
            as succesfully attacked the enemy."""
            if cmd == "pattack":
                print("You attack the enemy with your weapon!")
                print("-----------------------------")
                time.sleep(1.5)
                print(pattack())
                print("-----------------------------")
                time.sleep(1.5)
                rng = random.randint(1, 2)
                if rng == 1:
                    print(enemy_pattack())
                    time.sleep(1.5)
                    break
                if rng == 2:
                    print(enemy_mattack())
                    time.sleep(1.5)
                    break
            else:
                print("Come on! Type 'pattack'!")
        print("///////////////////////////////////")
        print("Good job. Let's try some magic.")
        time.sleep(3)
        print("Type 'mattack' to use a spell!")
        while True:
            cmd = input().lower()
            """Walks the user through how to to a magical attack,
            will not proceed until the user
            as succesfully attacked the enemy."""
            if cmd == "mattack":
                print("You cast a powerful spell!")
                print("-----------------------------")
                time.sleep(1.5)
                print(mattack())
                print("-----------------------------")
                time.sleep(1.5)
                rng = random.randint(1, 2)
                if rng == 1:
                    print(enemy_pattack())
                    time.sleep(1.5)
                    break
                if rng == 2:
                    print(enemy_mattack())
                    time.sleep(1.5)
                    break
            else:
                print("You can do it. Type 'mattack'.")
        print("///////////////////////////////////")
        print("Good. You can now attack enemies.")
        time.sleep(3)
        print("But remember if you attack an enemy it will attack you back.")
        time.sleep(3)
        print("The enemy has a 50% chance of using either")
        print("physical or magical attacks")
        time.sleep(3)
        print("If the enemy has no magic it cannot use a magical attack.")
        time.sleep(3)
        print("That goes for you too.")
        time.sleep(4)
        print("You can do other things as well.")
        time.sleep(3)
        print("You can examine, threaten, question,")
        print("tell a joke and see your stats and inventory")
        time.sleep(3)
        print("Let's examine the Dragon. Type 'examine'.")
        """Walks the user through how to do other misc commands,
        does not proceed until the user has completed the task."""
        while True:
            cmd = input().lower()
            if cmd == "examine":
                print(enemy.examine)
                break
            else:
                print("Type 'examine'!")
        time.sleep(3)
        print("You can also threaten, question and humor the enemies!")
        time.sleep(3)
        print("It's up to you to decide what you want to do!")
        time.sleep(3)
        print("Lets see info about yourself. Type 'self'.")
        """Walks the user through how to display stats,
        does not proceed until the user has completed the task."""
        while True:
            cmd = input().lower()
            if cmd == "self":
                print(player_info())
                break
            else:
                print("Type 'self'!")
        time.sleep(3)
        print("Press ENTER to continue...")
        input()
        print("These are your statistics, increasing")
        print("and decreasing them leads to")
        print("different outcomes in battle.")
        time.sleep(3)
        print("You can also use items!")
        time.sleep(3)
        print("Let's use a potion, type 'item' to get into the item menu,")
        print("then you can type 'inv' to see your inventory or put 'potion'")
        print("to use a potion.")
        """Walks the user through how to use items,
        does not proceed until the user has completed the task."""
        while True:
            cmd = input().lower()
            if cmd == "item":
                print("What would you like to use?")
                while True:
                    cmd = input().lower()
                    msg = use_item(cmd)
                    print(msg)
                    if msg != "You don't have that item!" and cmd != "inv":
                        break
                break
            else:
                print("Type 'item'!")
        commands = def_commands()
        time.sleep(2)
        print("You now know how to use potions!")
        time.sleep(3)
        print("But be careful, enemies attack after you use an item.")
        time.sleep(3)
        print("Use potions when you have low hp to quickly heal!")
        time.sleep(3)
        print("Let's finish the battle, kill the dragon!")
        time.sleep(4)
        print("Remember, type 'help' anytime if you are lost.")
        battle()
        print("Good job! You leveled up!")
        time.sleep(3)
        print("As you defeat enemies you gain EXP.")
        time.sleep(3)
        print("If you get enough, you level up!")
        time.sleep(3)
        print("If you level up, your stats increase and you get stronger!")
        time.sleep(3)
        print("Thats all for battle training. Now make your character!")
        time.sleep(3)
        """The user can now create his/her
        profile and begin playing the game."""
        print("Please enter your hero's name.")
        # The player's name
        name = input().title()
        print("Choose a Class!")
        time.sleep(2)
        print("Warrior: a well rounded physical attacker")
        print("with good damage and HP")
        time.sleep(4)
        print("Mage: a high damage output magic attacker with low HP")
        time.sleep(4)
        print("Archer: a ranged physical attacker with a high")
        print("critical chance.")
        time.sleep(4)
        print("Paladin: a strong physical attacker with some")
        print("magical capabilities, high HP but a relativly low attack")
        while True:
            # The player's chosen class
            job_choice = input()
            """
            Takes the class that the player wants to be
            and creates an instance of the class.
            If a valid class isn't chosen, askes for another input.
            Also equips a specific starting weapon for each class.
            """
            # The currently equipped weapon
            equipped = Weapons()
            equipped_armor = Armor()
            if job_choice.lower() == "warrior":
                player1 = Warrior(name)
                equipped.default_sword()
                equip_item("weapon")
                equipped_armor.default_chain()
                equip_item("armor")
                break
            elif job_choice.lower() == "mage":
                player1 = Mage(name)
                equipped.default_staff()
                equip_item("weapon")
                equipped_armor.default_cloth()
                equip_item("armor")
                break
            elif job_choice.lower() == "archer":
                player1 = Archer(name)
                equipped.default_bow()
                equip_item("weapon")
                equipped_armor.default_leather()
                equip_item("armor")
                break
            elif job_choice.lower() == "paladin":
                player1 = Paladin(name)
                equipped.default_mace()
                equip_item("weapon")
                equipped_armor.default_plate()
                equip_item("armor")
                break
            else:
                print("Please choose a valid class!")
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("You chose {} .".format(player1.job))
        time.sleep(3)
        """Some story and setting, might change it later"""
        print("It is now finally time to start your journey...")
        time.sleep(3)
        print("You start off at your town, which is a busy marketplace.")
        time.sleep(3)
        print("You leave home as you promise your younger sister you would")
        print("find your father who went to go fight some demon lord.")
        time.sleep(3)
        print("You both hope he's still alive...")
        # Give a bit of gold to start
        player1.add_gold(500)
        break
    # Loads the game
    elif cmd == "load":
        while True:
            if os.path.isfile("savegame.txt"):
                print("Save game found!")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                player1 = Player("default")
                equipped = Weapons()
                equipped_armor = Armor()
                inv = load_game()
                print("Welcome back " + player1.name + "!")
                time.sleep(1)
                equip_item("weapon")
                equip_item("armor")
                commands = def_commands()
                break
            else:
                print("You don't have a save game.")
                time.sleep(2)
                print("Make sure there is a file called 'savegame.txt'")
                time.sleep(4)
                print("Quitting the game...")
                time.sleep(5)
                quit()
        break
    else:
        print("Invalid input!!")
        time.sleep(1)
# Commands available while in the town.
town_commands = {
    "store": "Buy and sell items at the store!",
    "self": "Look at your stats.",
    "inv": "Look at your inventory",
    "save": "Save your game.",
    "dungeon": "Fight some monsters!",
    "quit": "Quit the game",
    "help": "Prints a list of helpful commands."
}
# Items available at the store
store_items = {
    "potion": 100,
    "super potion": 250,
    "mega potion": 500,
    "giga potion": 1000
}
""" This is the code for the whole town. This is the main hub for the game.
 The player can buy/sell items, save the game, quit, see information about
 themselves and go to dungeons.
"""
print("Welcome to the town!")
"""CREATE BOSS"""
while True:
    # if the player has done 50 battles, continue to the boss.
    if player1.battle_count >= 50:
        print("The location of the Demon Lord has been discovered!")
        print("Would you like to fight him? (y/n)")
        cmd = input().lower()
        if cmd == "y":
            break
        elif cmd == "n":
            print("Do another dungeon then come back to \
town if you change your mind!")
            time.sleep(1)
            player1.battle_count = 49
        else:
            print("Do you want to?!? (y/n)")
    print("What do you want to do?")
    print("Type 'help' to see commands.")
    print("You can type 'leave' in most menus to go back. ")
    print("________________________________________________")
    cmd = input().lower()
    if check_input(cmd, town_commands):
        if cmd == "store":
            print("Would you like to buy or sell?")
            while True:
                cmd = input().lower()
                if cmd == "buy":
                    while True:
                        print("What would you like to buy?")
                        print(print_inv(store_items))
                        cmd = input().lower()
                        if cmd == "leave":
                            break
                        elif check_input(cmd, store_items):
                            while True:
                                try:
                                    print("How many would you like to buy?")
                                    amount = int(input())
                                    if amount * store_items[cmd] > player1.gold:
                                        print("You don't have enough gold!")
                                    elif amount == 0:
                                        print("Alright Good Bye.")
                                        break
                                    else:
                                        inv[cmd] += amount
                                        cost = amount * store_items[cmd]
                                        player1.add_gold(-cost)
                                        print("That will be {} gold!".format(cost))
                                        print("Thank you for your purchase!")
                                        time.sleep(1)
                                        break
                                except ValueError:
                                    print("That's not a valid number!")
                            break
                        else:
                            print("We don't sell that here!")
                            time.sleep(1)
                    break
                elif cmd == "sell":
                    while True:
                        print("What would you like to sell?")
                        print(print_inv(inv))
                        cmd = input().lower()
                        if cmd == "leave":
                            break
                        elif check_input(cmd, inv):
                            while True:
                                try:
                                    print("How many would you like to sell?")
                                    amount = int(input())
                                    if amount > inv[cmd]:
                                        print("You don't have enough of that item!")
                                    elif amount == 0:
                                        print("Alright Good Bye.")
                                        break
                                    else:
                                        inv[cmd] -= amount
                                        sell_cost = amount * (math.ceil(store_items[cmd] / 2))
                                        player1.add_gold(sell_cost)
                                        print("We will give you " + str(sell_cost) + " gold.")
                                        print("Thank you for your business!")
                                        time.sleep(1)
                                        break
                                except ValueError:
                                    print("That's not a valid number!")
                            break
                        else:
                            print("You don't have that!")
                            time.sleep(1)
                    break
                elif cmd == "leave":
                    break
                else:
                    print("You can't do that!")
        elif cmd == "self":
            print(player_info())
        elif cmd == "inv":
            print(print_inv(inv))
        elif cmd == "dungeon":
            num_batt = random.randint(1, 5)
            current_batt = 0
            while current_batt <= num_batt:
                what_enemy = random.randint(1, 5)
                enemy = enemy_list[what_enemy]
                commands = def_commands()
                lvl_scale = random.randint(player1.level - 3, player1.level + 3)
                if lvl_scale <= 0:
                    lvl_scale = 1
                enemy.set_level(lvl_scale)
                enemy.scale_stats()
                print("A level {} {} has appeared!".format(enemy.level, enemy.name))
                battle()
                player1.add_battle()
                current_batt += 1
                print("You have defeated the {}!".format(enemy.name))
                enemy.reset_hp()
                time.sleep(3)
            player1.reset_hp()
            drop_equip()
            print("You have returned to town.")
        elif cmd == "save":
            print("Saving game...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            save_game()
            print("Game has been saved!")
        elif cmd == "help":
            print(print_inv(town_commands))
        elif cmd == "quit":
            print("Would you like to save? (yes/no)")
            while True:
                cmd = input().lower()
                if cmd == "yes":
                    print("Saving game...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    save_game()
                    print("Game has been saved!")
                    time.sleep(3)
                    quit()
                elif cmd == "no":
                    print("Quitting the game...")
                    time.sleep(3)
                    quit()
                elif cmd == "leave":
                    break
                else:
                    print("That's not a valid input!")
    else:
        print("You can't do that!")
        time.sleep(1)
print("You approach the Demon's castle.")
time.sleep(2)
print("You come across his throne.")
time.sleep(2)
print("You find the Demon along with his two generals.")
time.sleep(2)
print("You must fight the two in order to fight the Demon Lord.")
time.sleep(2)
print("A Lvl. 60 EVIL WIZARD has appeared!")
time.sleep(2)
enemy = EvilWizard()
commands = def_commands()
battle()
print("You have defeated the Evil Wizard!")
time.sleep(2)
print("You still have another to go!")
time.sleep(2)
print("A Lvl. 120 Mutilated Troll has appeared!")
time.sleep(2)
enemy = MutilatedTroll()
commands = def_commands()
battle()
print("You have defeated the Mutilated Troll!")
time.sleep(2)
print("The Demon Lord rises and the final battle begins.")
time.sleep(2)
enemy = DemonLord()
commands = def_commands()
battle()
print("You have defeated the Demon Lord!")
time.sleep(2)
print("You have restored peace to the land and will go down as a hero!")
time.sleep(2)
print("*Your game wil be saved*")
time.sleep(2)
print("Saving Game...")
time.sleep(2)
player1.battle_count = 0
save_game()
print("Credits:")
time.sleep(2)
print("Project Leader: Me")
time.sleep(2)
print("Lead Programmer: Me")
time.sleep(2)
print("Enemy maker guy: Oweeeeeeen")
time.sleep(2)
print("People who worked on the game: Me")
time.sleep(2)
print("Sponsored by: Not at all")
time.sleep(2)
print("Thanks for playing!")
time.sleep(10)
quit()
