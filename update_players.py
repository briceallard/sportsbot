import os
import json
import sys

from sportsreference.nfl.roster import Player
from sportsreference.nfl.roster import Roster


def get_player_ids():
    directory = './data/year/'

    years = os.listdir(directory)
    player_list = {}

    for year in years:
        teams = os.listdir('{0}/{1}'.format(directory, year))

        for team in teams:
            roster = Roster(team, year=year)

            for player in roster.players:

                if player.player_id not in player_list:
                    player_list[player.player_id] = player.name

                print('.', end=' ')

        print('{0} completed.'.format(year))

    with open('./data/player_ids.json', 'w+') as outfile:
        json.dump(player_list, outfile)
