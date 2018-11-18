import csv


def get_families(family_list):
    with open(family_list, newline='') as csvfile:
        raw_info = csv.DictReader(csvfile, delimiter=',')
        families = dict()
        family = dict()
        count = 0
        for row in raw_info:
            families[count] = {}
            for key, value in row.items():
                families[count][key] = value
            count +=1
        print(families)
        return families


families = get_families('soccer_players.csv')
