import sys
if sys.version_info[0] != 3:
    print("Error: this script requires Python 3")
    sys.exit(1)

from sleeper_wrapper import League
import requests
import pandas as pd
from collections import defaultdict
from random import shuffle

def exit_with_error(msg):
    print("Error: " + msg)
    sys.exit(1)

def get_sleeper_data(league_id):


    league_summary = {}

    for week in range(1,13):
        league = League(league_id)
        matchups = league.get_matchups(week)
        users = league.get_users()
        rosters = league.get_rosters()
        scoreboards = league.get_scoreboards(rosters, matchups, users, "pts_ppr", week)
        
        league_summary[week]=scoreboards
        

    # get weekly points for all weeks, all teams
    points = defaultdict(list)
    
    team1="Mr. 200"
    points[team1].append(136.84)
    points[team1].append(138.50)
    points[team1].append(200.04)
    points[team1].append(143.70)
    points[team1].append(153.04)
    points[team1].append(132.70)
    points[team1].append(152.44)
    points[team1].append(132.68)
    points[team1].append(164.62)
    points[team1].append(112.68)
    points[team1].append(136.04)
    points[team1].append(124.30)
    points[team1].append(142.40)

    team1="RuptaGupta's Benchwarmers"
    points[team1].append(129.20)
    points[team1].append(118.60)
    points[team1].append(118.22)
    points[team1].append(136.20)
    points[team1].append(157.34)
    points[team1].append(90.60)
    points[team1].append(90.54)
    points[team1].append(163.92)
    points[team1].append(101.16)
    points[team1].append(96.72)
    points[team1].append(140.68)
    points[team1].append(56.48)
    points[team1].append(110.42)

    team1=''
    points[team1].append(171.26)
    points[team1].append(186.38)
    points[team1].append(147.58)
    points[team1].append(173.98)
    points[team1].append(162.54)
    points[team1].append(168.04)
    points[team1].append(112.22)
    points[team1].append(175.18)
    points[team1].append(114.72)
    points[team1].append(151.12)
    points[team1].append(154.18)
    points[team1].append(137.86)
    points[team1].append(136.42)

    team1="El Ron de Cuba"
    points[team1].append(125.92)
    points[team1].append(143.76)
    points[team1].append(150.04)
    points[team1].append(119.32)
    points[team1].append(102.02)
    points[team1].append(145.20)
    points[team1].append(59.86)
    points[team1].append(102.90)
    points[team1].append(174.48)
    points[team1].append(156.26)
    points[team1].append(98.56)
    points[team1].append(144.18)
    points[team1].append(104.92)

    team1="The OG ABG"
    points[team1].append(123.62)
    points[team1].append(164.32)
    points[team1].append(101.36)
    points[team1].append(100.60)
    points[team1].append(138.84)
    points[team1].append(141.12)
    points[team1].append(145.44)
    points[team1].append(148.96)
    points[team1].append(111.56)
    points[team1].append(92.74)
    points[team1].append(107.98)
    points[team1].append(115.10)
    points[team1].append(120.40)

    team1="The Never Ending Pasta Bowl (R) is back!"
    points[team1].append(78.14)
    points[team1].append(132.62)
    points[team1].append(90.62)
    points[team1].append(152.90)
    points[team1].append(89.70)
    points[team1].append(138.72)
    points[team1].append(122.12)
    points[team1].append(110.98)
    points[team1].append(111.56)
    points[team1].append(116.60)
    points[team1].append(149.22)
    points[team1].append(108.22)
    points[team1].append(136.58)
    points[team1].append(99.88)

    team1="The Dallas Cowboys"
    points[team1].append(141.92)
    points[team1].append(111.36)
    points[team1].append(194.64)
    points[team1].append(80.90)
    points[team1].append(173.84)
    points[team1].append(142.04)
    points[team1].append(101.52)
    points[team1].append(114.16)
    points[team1].append(115.24)
    points[team1].append(154.88)
    points[team1].append(114.96)
    points[team1].append(129.82)
    points[team1].append(65.36)

    team1="Fat Witten"
    points[team1].append(149.40)
    points[team1].append(111.26)
    points[team1].append(123.34)
    points[team1].append(116.40)
    points[team1].append(191.62)
    points[team1].append(110.36)
    points[team1].append(113.86)
    points[team1].append(148.26)
    points[team1].append(100.90)
    points[team1].append(152.18)
    points[team1].append(132.72)
    points[team1].append(119.14)
    points[team1].append(118.66)

    team1="Who wants OG? From me! "
    points[team1].append(107.42)
    points[team1].append(114.46)
    points[team1].append(98.30)
    points[team1].append(104.18)
    points[team1].append(115.22)
    points[team1].append(123.82)
    points[team1].append(159.46)
    points[team1].append(132.70)
    points[team1].append(89.44)
    points[team1].append(92.42)
    points[team1].append(104.90)
    points[team1].append(122.06)
    points[team1].append(144.02)

    team1="the spice is BACK!!"
    points[team1].append(161.04)
    points[team1].append(135.12)
    points[team1].append(140.06)
    points[team1].append(102.42)
    points[team1].append(182.34)
    points[team1].append(131.72)
    points[team1].append(138.24)
    points[team1].append(148.30)
    points[team1].append(158.80)
    points[team1].append(139.70)
    points[team1].append(161.76)
    points[team1].append(141.88)
    points[team1].append(148.64)

    team1="Chairman Mao"
    points[team1].append(123.22)
    points[team1].append(131.24)
    points[team1].append(145.06)
    points[team1].append(116.30)
    points[team1].append(96.86)
    points[team1].append(122.54)
    points[team1].append(97.34)
    points[team1].append(106.04)
    points[team1].append(111.64)
    points[team1].append(113.24)
    points[team1].append(85.78)
    points[team1].append(71.74)
    points[team1].append(109.80)

    team1="Empty Those Tanks"
    points[team1].append(149.96)
    points[team1].append(100.32)
    points[team1].append(172.40)
    points[team1].append(130.70)
    points[team1].append(161.46)
    points[team1].append(100.10)
    points[team1].append(176.26)
    points[team1].append(118.44)
    points[team1].append(142.00)
    points[team1].append(129.12)
    points[team1].append(124.92)
    points[team1].append(142.62)
    points[team1].append(143.16)

    teams = list(points.keys())

    # get actual number of wins
    wins = dict.fromkeys(teams, 0)
    for week in league_summary:
        temp = league_summary[week]
        for match in temp:
            team1=temp[match][0][0]

            team1Score=points[team1][week]

            team2=temp[match][1][0]
            team2Score=points[team2][week]

            if (team2Score > team1Score):
                wins[team2] += 1
            elif (team1Score > team2Score):
                wins[team1] += 1

    return teams, points, wins

# used to advance matchups week to week
# assumed here that home_teams[i] will play away_teams[i]
def advance_round_robin(home_teams, away_teams):
    temp = away_teams[0]

    for i in range(len(away_teams)-1):
        away_teams[i] = away_teams[i+1]
    away_teams[len(away_teams)-1] = home_teams[len(home_teams)-1]

    for i in range(len(away_teams)-1, 1, -1):
        home_teams[i] = home_teams[i-1]
    home_teams[1] = temp

    return home_teams, away_teams
################################## main script #################################

# get raw points data
teams, points, actual_wins = get_sleeper_data(sys.argv[1])
n_playoff_teams = int("6") #TODO pull from league settings
all_weeks = "13" #TODO pull from league settings

# get total points
total_points = dict.fromkeys(teams, 0)
for team in teams:
    total_points[team] = sum(points[team])

#cache off the median wins
median_wins = dict.fromkeys(teams, 0)
for team in teams:
    weekScore = 0
    for week in range(1, int(all_weeks)):
        weekScore = points[team][int(week)-1]
        medianWinCount = 0
        for oppTeam in teams:
            if (oppTeam == team):
                continue
            if points[oppTeam][int(week)-1] < weekScore:
                medianWinCount += 1
        if medianWinCount >= 6:
            median_wins[team] += 1
            print(week)
            print(team)
    actual_wins[team] += median_wins[team]



# get actual seed, break ties with total points
actual_seed = []
for team in teams:
    actual_seed.append([team, actual_wins[team], total_points[team]])
actual_seed.sort(key=lambda tup: (tup[1], tup[2]), reverse=True)

# simulate season with random schedules
n_seasons = 100000
playoff_appearances = dict.fromkeys(teams, 0)
expected_wins = dict.fromkeys(teams, 0)
expected_seed = dict.fromkeys(teams, 0)
n_teams = len(teams)
midpoint = int(n_teams / 2)



for n in range(n_seasons):
    # set up this season's schedule
    shuffle(teams)
    home_teams = teams[0:midpoint]
    away_teams = teams[midpoint:n_teams]

    # simulate regular season
    season_wins = dict.fromkeys(teams, 0)
    for week in all_weeks:
        for home, away in zip(home_teams, away_teams):
            if points[home][int(week)-1] > points[away][int(week)-1]:
                season_wins[home] += 1
            elif points[home][int(week)-1] < points[away][int(week)-1]:
                season_wins[away] += 1
            else: # tie
                season_wins[home] += 0.5
                season_wins[away] += 0.5
        home_teams, away_teams = advance_round_robin(home_teams, away_teams)
    
    for team in season_wins:
        season_wins[team] += median_wins[team]

    # sort by most wins, break ties with total points
    season_stats = []
    for team in teams:
        season_stats.append([team, season_wins[team], total_points[team]])
    season_stats.sort(key=lambda tup: (tup[1], tup[2]), reverse=True)

    # record the seed, wins, and whether or not a team made the playoffs
    for i, tup in enumerate(season_stats):
        expected_seed[tup[0]] += i + 1
        expected_wins[tup[0]] += tup[1]
        if i < int(n_playoff_teams):
            playoff_appearances[tup[0]] += 1

# get average stats
sos = dict.fromkeys(teams, 0)
for i in expected_seed:
    expected_seed[i] = round(expected_seed[i] / n_seasons, 1)
    expected_wins[i] = round(expected_wins[i] / n_seasons, 2)
    sos[i] = round(actual_wins[i] - expected_wins[i], 2)
    playoff_appearances[i] = round(playoff_appearances[i] * 100 / n_seasons, 1)

# create tuple of all season info
season_summary = []
for i, tup in enumerate(actual_seed):
    name = tup[0]
    season_summary.append([
        name.upper(),                                       # 0 - team name
        i+1,                                                # 1 - actual seed
        expected_seed[name],                                # 2 - average seed
        round(expected_seed[name] - i-1, 1),                # 3 - seed diff
        actual_wins[name],                                  # 4 - actual wins
        expected_wins[name],                                # 5 - average wins
        round(actual_wins[name] - expected_wins[name], 2),  # 6 - win diff
        playoff_appearances[name]])                         # 7 - playoff chance

# sort by a condition
season_summary.sort(key=lambda tup: tup[1], reverse=False)

def formatted_print(x):
    print('{:>50}'.format(str(x[0])) +
          '{:>6}'.format(str(x[1])) + 
         '{:>10}'.format(str(x[2])) +
         '{:>11}'.format(str(x[3])) +
          '{:>6}'.format(str(x[4])) + 
         '{:>10}'.format(str(x[5])) +
         '{:>10}'.format(str(x[6])) + 
         '{:>16}'.format(str(x[7])))

# print season summary info
formatted_print(["Team", "Seed", "Avg Seed", "Seed Diff", "Wins", "Avg Wins",
    "Win Diff", "Playoff Chance"])
for team_summ in season_summary:
    formatted_print(team_summ)