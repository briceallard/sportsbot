import utils
import json
import csv
import os

from sportsreference.nfl.teams import Teams


def update_years():
    min_year = input("Beginning year: ")
    max_year = input("Ending year: ")

    while int(min_year) <= int(max_year):

        teams = Teams(min_year)
        total_teams = len(teams)
        count = 1

        print('Starting data collection ... \n')

        for team in teams:
            if not os.path.exists('./data/year/{0}/{1}'.format(min_year, team.abbreviation).lower()):
                os.makedirs(
                    './data/year/{0}/{1}'.format(min_year, team.abbreviation).lower())

            file_csv = './data/year/{0}/{1}/{0}_{1}.csv'.format(
                min_year, team.abbreviation).lower()
            file_json = './data/year/{0}/{1}/{0}_{1}.json'.format(
                min_year, team.abbreviation).lower()

            f = open(file_csv, 'w+')
            f.close()

            team.schedule.dataframe_extended.to_csv(file_csv)

            f = open(file_csv, 'r')
            reader = csv.reader(f)
            lines = list(reader)

            lines[0][0] = 'game_id'
            f.close()

            f = open(file_csv, 'w')
            writer = csv.writer(f)

            for line in lines:
                writer.writerow(line)
            f.close()

            utils.csv_to_json(file_csv, file_json)

            print('{0}/{1} complete'.format(count, total_teams))
            count += 1

        min_year = utils.year_plus_one(min_year)
