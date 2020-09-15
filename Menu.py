import Utils
import json

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
            data = {}
            year = input("Enter Search Year: ")
            teams = Teams(year)

            for team in teams:
                # data[year] = {}
                # data[year][team.name] = team.schedule.dataframe_extended
                # print(data)
                # break
                team.schedule.dataframe_extended.to_csv('%s.csv' % team.abbreviation.lower())
                break

            # with open('data.json', 'w') as outfile:
            #     json.dump(data, outfile)
