# Define a function to pull all the families into a dictionary of dictionaries
# Define a function to divide the players into lists based on experience
# Create the teams: Sharks, Dragons, and Raptors
# Define a function that evenly distributes the players amongst the teams
# Define a function that creates letters for each set of guardians
#     and outputs fit to a file named parentFirst_parentLast.txt
#     This file must contain the player's name, the team's name, and
#     it must start with "Dear {}" guardian(s) name.
# Define a function that creates a file of the team rosters, named teams.txt

# CODE MUST INCLUDE COMMENTS -- USE DOCSTRINGS AS WELL #


import csv
from random import shuffle


dragons = []
raptors = []
sharks = []
team_list = [
    dragons,
    raptors,
    sharks
]


def get_families(family_list):
    """get_families takes a CSV file as an argument, opens it for reading/writing,
    takes each row out of the file and converts it to a dictionary,
    then adds that dictionary to a master dictionary named \"families\".
    When the function has looped through each \"family\", the master
    dictionary of \"families\" is then returned to the caller.
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
    """sort_players takes a list of families, sorts
    through the [\"Soccer Experience\"] key
    of each player, and determines whether
    to place them in the list of experienced
    or inexperienced players. These lists are
    then returned to the caller.
    """
    inexperienced_players = [value for value in family_list.values()
                             if value['Soccer Experience'] == 'NO']
    experienced_players = [value for value in family_list.values()
                           if value['Soccer Experience'] == 'YES']
    return inexperienced_players, experienced_players


def draft_teams(players, team_list):
    """draft_teams takes a list players and a team list uses
    the shuffle method from the random library to randomly
    rearrange the players (while still preserving experience
    levels), and sorts each of them into one of three teams,
    based on experience.
    """
    shuffle(players)
    count = 1
    for player in players:
        if count % 3 == 0:
            # Adds player to the sharks team.
            team_list[2].append(player)
            player['Team'] = 'Sharks'
        elif count % 2 == 0:
            # Adds player to the raptors team.
            team_list[1].append(player)
            player['Team'] = 'Raptors'
        else:
            # Adds player to the dragons team.
            team_list[0].append(player)
            player['Team'] = 'Dragons'
        count += 1


def create_file(team):
    """create_file writes all of the player\'s names and info into
    an external file under the heading of their team\'s name.
    """
    team_name = team[0]['Team']
    file.write('\n|{}\n'.format(team_name))
    for player in team:
        file.write('|{} \n Guardians: {}. Has played before: {}.\n'.format(
            player['Name'],
            player['Guardian Name(s)'],
            player['Soccer Experience'].capitalize()))


# def parent_letter(player):
#     with open('{}_{}.txt'.format( placeholder ), 'w') as file:


if __name__ == "__main__":
    families = get_families('soccer_players.csv')
    inexperienced_players, experienced_players = sort_players(families)
    draft_teams(inexperienced_players, team_list)
    draft_teams(experienced_players, team_list)

    with open("teams.txt", "w") as file:
        create_file(dragons)
        create_file(raptors)
        create_file(sharks)
