# bookbot
## Overview
BookBot is my first project! Thank you for checking out this repository and trying out the bot. I will work on this bot from time to time and add more features.

This bot was coded completely in Python3. It is designed to take in a .txt book file, count the words and characters, and report how many words were used and how many times each character was used.

## Acknowledgments
Credit to [Boot.dev](boot.dev) for the courses and guided project.

## Setup
This bot is designed to run in Linux.

Once you've downloaded the files, you need books for the bot to read. The required additions to your directory will be:

- A books/ directory, go ahead and create one!
- .txt files with book text in them. The book used when creating this bot was Mary Shelley's Frankenstein, which you can access [here.](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) Simply copy all of the text and paste it into a file called "frankenstein.txt."
- If you're using other books, go into main.py and change the "bookpath" variable in main() to "books/(yourbooktitle).txt.

## How To Use
- In the shell, navigate to the bookbot directory.
- Once there, run main.py using Python 3.
- The bookbot will count how many words there are in your book.
- The bookbot will also count how many times each character is used, sorted by most frequent to least frequent.

## Patch Notes
### 1.0.0
- Created a bot that reads and analyzes Mary Shelley's "Frankenstein".

## Wanted Features
- The bot greets the user.
- Modular Reports
- - The bot asks the user to type in the name of a book in books/.
- - The bot looks up and runs a report for the book entered.
- - The bot returns an error message if the book isn't found.
- Book List
- - The bot also informs the user about the "list books" query.
- - When "list books" is entered, print the name of each book in the bot's library.
