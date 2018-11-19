# Define a function to pull all the families into a dictionary of dictionaries
# Define a function to divide the players into lists of experienced and inexperienced
# Create the teams: Sharks, Dragons, and Raptors
# Define a function that evenly distributes the players amongst the teams
# Define a function that creates letters for each set of guardians and outputs it
#### to a file named parentFirst_parentLast.txt
# Define a function that creates a file of the team rosters, named teams.txt

#### CODE MUST INCLUDE COMMENTS -- USE DOCSTRINGS AS WELL ####


import csv


def get_families(family_list):
    """get_families takes a CSV file as an argument, opens it for reading/writing,
    takes each row out of the file and converts it into a dictionary (temporarily
    named \"family\"), then adds that dictionary to a master dictionary named
    \"families\". When the function has looped through each \"family\", the master
    dictionary of \"families\" is then returned to the caller.
    """
    with open(family_list, newline='') as csvfile:
        raw_info = csv.DictReader(csvfile, delimiter=',')
        families = dict()
        family = dict()
        count = 0
        for row in raw_info:
            families[count] = {}
            for key, value in row.items():
                families[count][key] = value
            count += 1
        print(families)
        return families


if __name__ == "__main__":
    families = get_families('soccer_players.csv')
