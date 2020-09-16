import Utils
import json
import csv

from sportsreference.nfl.teams import Teams


def menu():
    closeApp = False

    while closeApp is False:

        print("SportsBot - Main Menu\n")
        print("Search options:")
        print("1. Year")
        print("2. Player")
        print("3. Team")
        print("4. Position")
        print("5. Exit")

        selection = input("\nMenu Choice: ")

        if selection == "1":
            year = input("Enter Search Year: ")
            teams = Teams(year)

            for team in teams:
                filename = './data/{0}_{1}.csv'.format(
                    year, team.abbreviation).lower()

                team.schedule.dataframe_extended.to_csv(filename)

                r = csv.reader(open(filename))
                lines = list(r)

                lines[0][0] = 'game_id'

                print(lines)

                writer = csv.writer(open('./tmp/test.csv', 'w'))
                writer.writerows(lines)

                break

            # Utils.make_json(r'kan.csv', r'kan.json')
