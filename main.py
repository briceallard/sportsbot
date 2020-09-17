from sportsreference.nfl.teams import Teams
from pprint import pprint
import sys

import constants
import menu
import update_years as uy
import utils

if __name__ == "__main__":

    selection = menu.get_menu_selection()

    if selection == '1':
        uy.update_years()
    else:
        print('Wrong Selection ...')
        sys.exit()
