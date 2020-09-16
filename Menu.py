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
                file_csv = './data/{0}_{1}.csv'.format(
                    year, team.abbreviation).lower()
                file_json = './data/{0}_{1}.json'.format(
                    year, team.abbreviation).lower()

                team.schedule.dataframe_extended.to_csv(file_csv)

                f = open(file_csv, 'r')
                reader = csv.reader(f)
                lines = list(reader)

                lines[0][0] = 'game_id'
                f.close()

                print(lines)

                f = open(file_csv, 'w')
                writer = csv.writer(f)

                for line in lines:
                    writer.writerow(line)
                f.close()

                break

            Utils.csv_to_json(file_csv, file_json)
