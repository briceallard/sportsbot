from sportsreference.nfl.teams import Teams
from pprint import pprint

if __name__ == "__main__":

    year = input("Enter search year: ")
    teams = Teams(year)

    count = 0

    for team in teams:
        print(team.name, team.abbreviation)
        count = count + 1

    print(count)