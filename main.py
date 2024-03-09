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

# Initialize the game state
game_state = {
    "suspect": None,
    "weapon": None,
    "room": None
}

# Function to update the bot's knowledge based on user input
def update_bot_knowledge(category, items):
    bot_knowledge[category] -= set(items)

# Function to get a suggestion from the bot
def bot_suggestion():
    suggestion = {}
    for category in ["suspect", "weapon", "room"]:
        if game_state[category] is None:
            suggestion[category] = random.choice(list(bot_knowledge[category + "s"]))
        else:
            suggestion[category] = game_state[category]
    return suggestion

# Function to check if the bot has enough information to make an accusation
def can_make_accusation():
    return all(game_state.values())

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

# Function to display the game state
def display_game_state():
    print("\nCurrent game state:")
    for category, item in game_state.items():
        print(f"{category.capitalize()}:", item if item else "Unknown")

# Game loop
print("Welcome to Cluedo!")
print("You will provide information to the bot, and the bot will suggest actions.")

while True:
    display_possibilities()
    display_game_state()

    # Get information from the user
    print("\nEnter the information you have (or press Enter if no new information):")
    for category in ["suspects", "weapons", "rooms"]:
        items = get_items_from_input(category)
        if items:
            update_bot_knowledge(category, items)
            if len(items) == 1:
                game_state[category[:-1]] = items[0]

    # Check if the bot can make an accusation
    if can_make_accusation():
        print("\nThe bot is ready to make an accusation:")
        for category, item in game_state.items():
            print(f"{category.capitalize()}:", item)
        break
    else:
        # Get a suggestion from the bot
        suggestion = bot_suggestion()
        print("\nBot's suggestion:")
        for category, item in suggestion.items():
            print(f"{category.capitalize()}:", item)

        # Get feedback from the user
        feedback = input("Is the suggestion correct? (yes/no/partial): ")
        if feedback.lower() == "yes":
            print("\nThe bot has solved the mystery!")
            break
        elif feedback.lower() == "partial":
            print("Please provide more information about the correct parts of the suggestion.")
            for category in ["suspect", "weapon", "room"]:
                correct = input(f"Is the {category} correct? (yes/no): ")
                if correct.lower() == "yes":
                    game_state[category] = suggestion[category]
        else:
            print("The bot's suggestion is incorrect. Please provide more information.")

print("\nGame over!")
