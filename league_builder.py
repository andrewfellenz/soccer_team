import csv
from random import shuffle

# Defining Teams.
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
    """draft_teams takes a list of players and a team list, uses
    the shuffle method from the random library to randomly
    rearrange the players (while still preserving experience
    levels), and sorts each of them into one of three teams,
    based on experience.
    """
    shuffle(players)
    # Shuffling players to create randomness in the draft.
    for count, player in enumerate(players):
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


def create_file(team):
    """create_file writes all of the player\'s names and info into
    an external file under the heading of their team\'s name.
    """
    team_name = team[0]['Team']
    file.write('\n|{}\n'.format(team_name))
    # First player's 'Team' key is used to write the team name as a header.
    for player in team:
        file.write('|{} \n Guardians: {}. Has played before: {}.\n'.format(
            player['Name'],
            player['Guardian Name(s)'],
            player['Soccer Experience'].capitalize()))


def parent_letter(player):
    """parent_letter creates an individualized letter to the parent(s)
    of each player. It details what team they are on and the date and
    time of the first team practice.
    """
    with open('{}.txt'.format
              (player['Name'].replace(' ', '_').lower()), 'w') as file:
        # Uses player's name with '_' instead of space as file name.
        file.write(
            """Dear {},\n\n    {} has been selected to play for the {}.\
            \nPlease be advised that the first day of practice is\
            \nSaturday, December 1st, 12:30pm, at Springfield Park.\n\
            \nThank you,\
            \n-Coach Drew\n\
            """.format(player['Guardian Name(s)'],
                       player['Name'].split(' ')[0], player['Team']))


if __name__ == "__main__":
    # Calling the functions.

    families = get_families('soccer_players.csv')
    # Setting the families variables to include all the player dictionaries.

    inexperienced_players, experienced_players = sort_players(families)
    # Sorting through players by experience level.

    draft_teams(inexperienced_players, team_list)
    draft_teams(experienced_players, team_list)
    # Drafting the players by experience level into their teams.

    with open("teams.txt", "w") as file:
        # Creating the team.txt file with the team rosters.
        create_file(dragons)
        create_file(raptors)
        create_file(sharks)

    for value in families.values():
        # Printing parent letters for each player.
        parent_letter(value)
