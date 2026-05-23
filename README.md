# Monster Data Cleaner

Monster Data Cleaner is a beginner Python project that reads messy fantasy creature data from a JSON file, cleans the records, displays the cleaned data in the terminal, and saves the cleaned results to a new JSON file.

## Features
- Reads monster data from a JSON file
- Cleans extra spaces and inconsistent capitalization
- Converts HP values to integers
- Converts magic-user values into True/False
- Replaces missing values with default text
- Prints cleaned records in a formatted table
- Saves cleaned data to a new JSON file

## Data Fields

Each Monster record contains:
- Name
- Size
- HP
- Location
- Magic User

## Example Input

```json
[" sWord wraith", " MEDIUM", " 45", "grassland", "NO"]
```
## Example Output
```json
["Sword Wraith", "Medium", 45, "Grassland", False]
```

## Python Concepts Used
- Lists & Nested lists
- File input and output
- JSON loading and dumping
- Functions
- Loops
- If/elif/else statements
- Try/ except error handling
- String Methods

## How to Run
1. Place the JSON file in the same directory as main.py
2. Run the program.
3. Enter the JSON file name when prompted.
4. The cleaned data will be saved as cleaned_monster_file.json

## Project Notes
This project was created for an introductory Python course.  It was designed to practice basic programming concepts while using a small data-cleaning workflow.

## Future Improvements

- Add CSV file support
- Add more validation for HP and size values
- Let the user choose the output file name
- Add a summary count of magic users and unknown values
