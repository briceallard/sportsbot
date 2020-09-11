import Utils


def menu():
    Utils.clear()

    print('SportsBot - Main Menu\n')
    print('Search options:')
    print('1. Year')
    print('2. Player')
    print('3. Team')
    print('4. Position')

    selection = input("\nMenu Choice: ")

    if isMenuChoice(selection, 1, 4):
        print('Selection found')

    print('You selected', selection)


def isMenuChoice(selection, min, max):
    try:
        if min < int(selection) < max:
            return True
        else:
            return False
    except ValueError:
        print('Must enter a number value')
