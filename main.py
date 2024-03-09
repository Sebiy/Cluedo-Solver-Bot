import random

# Define the game elements
suspects = ["Colonel Mustard", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Miss Scarlet", "Mrs. White"]
weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]

# Initialize the bot's knowledge
bot_knowledge = {
    "suspects": set(suspects),
    "weapons": set(weapons),
    "rooms": set(rooms)
}

# Function to update the bot's knowledge based on user input
def update_bot_knowledge(category, items):
    bot_knowledge[category] -= set(items)

# Function to get a suggestion from the bot
def bot_suggestion():
    suspect = random.choice(list(bot_knowledge["suspects"]))
    weapon = random.choice(list(bot_knowledge["weapons"]))
    room = random.choice(list(bot_knowledge["rooms"]))
    return {"suspect": suspect, "weapon": weapon, "room": room}

# Function to check if the bot has enough information to make an accusation
def can_make_accusation():
    return len(bot_knowledge["suspects"]) == 1 and len(bot_knowledge["weapons"]) == 1 and len(bot_knowledge["rooms"]) == 1

# Function to get a list of items from user input
def get_items_from_input(category):
    items = []
    while True:
        item = input(f"Enter a {category[:-1]} (or press Enter to finish): ")
        if item == "":
            break
        if item not in eval(category):
            print(f"Invalid {category[:-1]}. Please try again.")
        else:
            items.append(item)
    return items

# Function to display the remaining possibilities
def display_possibilities():
    print("\nRemaining possibilities:")
    for category, items in bot_knowledge.items():
        print(f"{category.capitalize()}:", ", ".join(sorted(items)))

# Game loop
print("Welcome to Cluedo!")
print("You will provide information to the bot, and the bot will suggest actions.")

while True:
    display_possibilities()

    # Get information from the user
    print("\nEnter the information you have (or press Enter if no new information):")
    for category in ["suspects", "weapons", "rooms"]:
        items = get_items_from_input(category)
        if items:
            update_bot_knowledge(category, items)

    # Check if the bot can make an accusation
    if can_make_accusation():
        accusation = {
            "suspect": list(bot_knowledge["suspects"])[0],
            "weapon": list(bot_knowledge["weapons"])[0],
            "room": list(bot_knowledge["rooms"])[0]
        }
        print("\nThe bot is ready to make an accusation:")
        for category, item in accusation.items():
            print(f"{category.capitalize()}:", item)
        break
    else:
        # Get a suggestion from the bot
        suggestion = bot_suggestion()
        print("\nBot's suggestion:")
        for category, item in suggestion.items():
            print(f"{category.capitalize()}:", item)

        # Get feedback from the user
        feedback = input("Is the suggestion correct? (yes/no): ")
        if feedback.lower() == "yes":
            print("\nThe bot has solved the mystery!")
            break
        else:
            print("The bot's suggestion is incorrect. Please provide more information.")

print("\nGame over!")

