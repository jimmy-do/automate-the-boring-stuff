# “You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary
# where the keys are string values describing the item in the inventory and the value is an integer value detailing
# how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42,
# 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.”

# “Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
#
# Total number of items: 62”
#
# Now, also add another function to add more inventory items i.e. increase value of respective keys.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
phat_lewtz = ['gold coin', 'dagger', 'arrow', 'greatsword']


def display_inventory(inventory):
    total = 0
    for items, amount in inventory.items():
        print(f"{items}: {amount}")
        total += amount
    print(f"The total number of items in your inventory is: {total}")


def add_to_inventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1


add_to_inventory(stuff, phat_lewtz)
display_inventory(stuff)
