import Utils

from sportsreference.nfl.teams import Teams


def menu():
    closeApp = False
    Utils.clear()

    while closeApp == False:

        print('SportsBot - Main Menu\n')
        print('Search options:')
        print('1. Year')
        print('2. Player')
        print('3. Team')
        print('4. Position')
        print('5. Exit')

        selection = input("\nMenu Choice: ")

        if selection == '1':
            year = input('Enter Search Year: ')

            teams = Teams(year)

            for team in teams:
                print(team.name, team.abbreviation)


def isMenuChoice(selection, min, max):
    try:
        if min < int(selection) < max:
            return True
        else:
            return False
    except ValueError:
        print('Must enter a number value')
