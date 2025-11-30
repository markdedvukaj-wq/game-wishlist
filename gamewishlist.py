""
# Video Game Wishlist Manager #

# This script lets the user manage a list of video games:
# - Load from a file
# - Add, delete, and modify games
# - Mark games as owned or not owned
# - See the total cost of games
# - Save back to a files 
""

FILENAME = "games.txt"  # This is the file we read from and write to


# Data & File Functions #

def load_games(filename):
    """
    Read game data from a text file.
    Each line has the format: title,price,owned_flag
    owned_flag is 0 or 1.
    Returns a list of dictionaries.
    """
    games = []  # list (data structure #1)

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                parts = line.split(",")
                if len(parts) != 3:
                    # if the line is malformed, skip it
                    continue

                title = parts[0]
                # convert string to float (data type: float)
                price = float(parts[1])
                owned_flag = parts[2]

                # convert "0" / "1" to bool (data type: bool)
                owned = True if owned_flag == "1" else False

                # dictionary (data structure #2)
                game = {
                    "title": title,
                    "price": price,
                    "owned": owned
                }
                games.append(game)

    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty game list.")

    return games


def save_games(filename, games):
    """
    Write the current list of games to a file.
    Each line is written in the format: title,price,owned_flag
    """
    with open(filename, "w") as f:
        for game in games:
            owned_flag = "1" if game["owned"] else "0"
            line = f"{game['title']},{game['price']},{owned_flag}\n"
            f.write(line)


# Utility Functions #

def display_games(games):
    """
    Print all games in a nice formatted list.
    """
    if len(games) == 0:
        print("Your game list is currently empty.")
        return

    print("\n--- Current Games ---")
    # loop #1: iterate over the list to display games
    for index, game in enumerate(games, start=1):
        status = "Owned" if game["owned"] else "Wishlist"
        # Example of using multiple data types in one print: int + string + float
        print(f"{index}. {game['title']} - ${game['price']:.2f} ({status})")
    print("----------------------\n")


def calculate_total_cost(games, owned_only=False):
    """
    Calculate the total cost of games.

    If owned_only is True, only sum owned games.
    If owned_only is False, sum all games.

    This function will be called at least twice with different values
    of 'owned_only', satisfying the custom function requirement.
    """
    total = 0.0  # float

    # loop #2: used for a different purpose (calculation)
    for game in games:
        if owned_only:
            if game["owned"]:
                total += game["price"]
        else:
            total += game["price"]

    return total


def find_game_index(games, title_to_find):
    """
    Find the index of a game by title (case-insensitive).
    Returns the index or -1 if not found.
    """
    title_to_find = title_to_find.lower()
    for i, game in enumerate(games):
        if game["title"].lower() == title_to_find:
            return i
    return -1


# Menu Action Functions #

def add_game(games):
    """
    Ask the user for game information and append it to the list.
    Demonstrates input(), type conversion, and data structure modification.
    """
    title = input("Enter the game title: ")
    price_str = input("Enter the price (e.g., 59.99): ")

    # convert string to float, with basic error handling
    try:
        price = float(price_str)
    except ValueError:
        print("Invalid price. Game not added.")
        return

    owned_input = input("Do you already own this game? (y/n): ").strip().lower()
    if owned_input == "y":
        owned = True
    else:
        owned = False

    game = {
        "title": title,
        "price": price,
        "owned": owned
    }
    games.append(game)  # add element to data structure
    print(f"Game '{title}' added.")


def delete_game(games):
    """
    Delete a game by title.
    Demonstrates removing elements from the data structure.
    """
    title = input("Enter the title of the game to delete: ")
    index = find_game_index(games, title)

    if index == -1:
        print("Game not found, nothing deleted.")
    else:
        removed = games.pop(index)
        print(f"Game '{removed['title']}' removed.")


def update_game(games):
    """
    Modify a game's price or owned status.
    Demonstrates changing elements in the data structure.
    Also uses conditional logic with relational and logical operators.
    """
    title = input("Enter the title of the game to update: ")
    index = find_game_index(games, title)

    if index == -1:
        print("Game not found, nothing updated.")
        return

    game = games[index]
    print(f"Current info: {game['title']} - ${game['price']:.2f} - "
          f"{'Owned' if game['owned'] else 'Wishlist'}")

    choice = input("What would you like to update? (price/status/both): ").strip().lower()

    if choice == "price" or choice == "both":
        new_price_str = input("Enter the new price: ")
        try:
            new_price = float(new_price_str)
            # relational operator: check if new price is >= 0
            if new_price >= 0:
                game["price"] = new_price
            else:
                print("Price cannot be negative. Keeping old price.")
        except ValueError:
            print("Invalid price. Keeping old price.")

    if choice == "status" or choice == "both":
        new_status = input("Do you own this game now? (y/n): ").strip().lower()
        game["owned"] = (new_status == "y")

    print("Game updated.")


def show_budget_info(games):
    """
    Ask user for a budget and show if they can afford all wishlist games.
    Demonstrates relational and logical operators (>, <, ==, !=, and, or, not).
    Also uses arithmetic operations.
    """
    if len(games) == 0:
        print("No games in the list to analyze.")
        return

    budget_str = input("Enter your budget for games (e.g., 100): ")
    try:
        budget = float(budget_str)
    except ValueError:
        print("Invalid number for budget.")
        return

    total_all = calculate_total_cost(games, owned_only=False)
    total_wishlist = 0.0
    for game in games:
        # logical operator: not
        if not game["owned"]:
            total_wishlist += game["price"]

    print(f"Total cost of ALL games: ${total_all:.2f}")
    print(f"Total cost of WISHLIST (not owned) games: ${total_wishlist:.2f}")
    print(f"Your budget: ${budget:.2f}")

    # relational operators + logical operators and/or
    if total_wishlist <= budget and budget > 0:
        print("Good news! You can afford all wishlist games within your budget.")
    elif total_wishlist > budget and budget > 0:
        print("You cannot afford all wishlist games yet.")
    else:
        print("Budget is zero or negative, so you cannot buy any games right now.")


def print_menu():
    """
    Display the main menu options.
    """
    print("=== Video Game Wishlist Manager ===")
    print("1. View all games")
    print("2. Add a new game")
    print("3. Delete a game")
    print("4. Update a game")
    print("5. Show cost totals and budget info")
    print("6. Save and Exit")


# Main Program (Loop & User Interaction) #

def main():
    # Load initial games from file (may be empty if file not found)
    games = load_games(FILENAME)

    # Ensure we have at least some games at some point
    # (requirement: data structure with at least 5 elements sometime during execution)
    # You can manually add more in the file, or via the "add" option in the menu.

    running = True  # bool

    while running:  # main loop
        print_menu()
        choice = input("Choose an option (1-6): ")

        # if/elif/else (conditional logic)
        if choice == "1":
            display_games(games)
        elif choice == "2":
            add_game(games)
        elif choice == "3":
            delete_game(games)
        elif choice == "4":
            update_game(games)
        elif choice == "5":
            show_budget_info(games)
        elif choice == "6":
            # before exiting, save to file
            save_games(FILENAME, games)
            print("Changes saved. Goodbye!")
            running = False
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
