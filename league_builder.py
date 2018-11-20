# Define a function to pull all the families into a dictionary of dictionaries
# Define a function to divide the players into lists of experienced and inexperienced
# Create the teams: Sharks, Dragons, and Raptors
# Define a function that evenly distributes the players amongst the teams
# Define a function that creates letters for each set of guardians and outputs it
#### to a file named parentFirst_parentLast.txt
# Define a function that creates a file of the team rosters, named teams.txt

#### CODE MUST INCLUDE COMMENTS -- USE DOCSTRINGS AS WELL ####


import csv


DRAGONS = {}
RAPTORS = {}
SHARKS = {}


def get_families(family_list):
    """get_families takes a CSV file as an argument, opens it for reading/writing, 
    takes each row out of the file and converts it into a dictionary (temporarily
    named \"family\"), then adds that dictionary to a master dictionary named 
    \"families\". When the function has looped through each \"family\", 
    the master dictionary of \"families\" is then returned to the caller.
    """
    with open(family_list, newline='') as csvfile:
        raw_info = csv.DictReader(csvfile, delimiter=',')
        families = dict()
        family = dict()
        count = 1
        for row in raw_info:
            families[count] = {}
            for key, value in row.items():
                families[count][key] = value
            count += 1
        return families


def sort_players(family_list):
    """sort_players takes a list of families, sorts through the [\"Soccer Experience\"]
    key of each player, and determines whether to place them in the list of experienced
    or inexperienced players. These lists are then returned to the caller.
    """
    inexperienced_players = [value for value in family_list.values() if value['Soccer Experience'] == 'NO']
    experienced_players = [value for value in family_list.values() if value['Soccer Experience'] == 'YES']
    return inexperienced_players, experienced_players


if __name__ == "__main__":
    families = get_families('soccer_players.csv')
    sort_players(families)
 
