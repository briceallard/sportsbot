from sportsreference.nfl.teams import Teams
import sys

import menu
import update_years as uy
import update_players as up

if __name__ == "__main__":

    selection = menu.get_menu_selection()

    if selection == '1':
        uy.update_years()
    elif selection == '2':
        up.get_player_ids()
    else:
        print('Invalid Selection ...')
        sys.exit()
