from sportsreference.nfl.teams import Teams
import sys

import menu
import update_years as uy

if __name__ == "__main__":

    selection = menu.get_menu_selection()

    if selection == '1':
        uy.update_years()
    else:
        print('Invalid Selection ...')
        sys.exit()
