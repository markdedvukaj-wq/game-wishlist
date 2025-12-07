# game-wishlist
This is my CSI-1320 Final Project called, Videogame Wishlist Manager. This project allows you to add or remove a list of games you own or do not own and add their prices.

This project demonstrates:
user interaction with input() and print(),
conditional logic (with relational & logical operators)
loops,
arithmetic expressions and multiple data types,
lists and dictionaries,
adding, deleting, and modifying data structures,
reading and writing data from files, and
custom functions and modular design

To run this code in Linux you have to type

python3 gamewishlist.py

Features

View All Games

Displays a list of all games including price and ownership status.

Add a New Game

Prompts the user to enter game information (title, price, owned).

Delete a Game

Removes a game using title search.

Update a Game

Allows modifying the price, owned status, or both.

Budget Analysis

Shows:

Total value of all games

Total cost of wishlist only games

Whether the wishlist fits within the user’s budget

Save and Exit

Writes all changes back to games.txt


Main Menu:

Option 1 allows you to view all games

Option 2 allows you to add a new game

Option 3 allows you to delete a game

Option 4 allows you to update a games price, status, or both

Option 5 allows you to add a budget and see the total cost of the wishlist

Option 6 saves & exits the program


Troubleshooting


Issue	Solution

FileNotFoundError for games.txt	create the file manually or ensure it’s in the project folder

If the price is not updating enter numeric values only (no $)

Game not found during deletion/update	check spelling because search is case insensitive
