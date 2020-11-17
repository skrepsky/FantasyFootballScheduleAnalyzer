import requests
import MedianWins
import Team
import Rosters
import Week

class League:
    TeamsDict: dict
    IncludeMedianWins: bool
    CurrentYear: int
    LeagueId: str
    NumWeeks: int
    Rosters: Rosters
    Weeks: list
    MedianWins: MedianWins

    
    def __init__(self, leagueId: str, currentYear: int, asOfWeek: int):
        """Initializes the league class

        Args:
            leagueId (str): league id
            currentYear (int): 4 digit year to process
        """
        self.LeagueId = leagueId
        self.CurrentYear = currentYear
        self.IncludeMedianWins = True #TODO - include by default for now
        self.TeamsDict = {}
        self.NumWeeks = asOfWeek
        self.Rosters = Rosters.Rosters(leagueId)
        self.Weeks = [] 
        self.initializeAllWeeks(self.NumWeeks)
        self.MedianWins= MedianWins.MedianWins()


    def initializeAllWeeks(self, numWeeks):
        """Initialize all weeks objects for later population

        Args:
            numWeeks (int): The number of weeks in the season
        """

        for i in range (numWeeks):
            self.Weeks.append(Week.Week(i))


    def populateTeams(self):
        """Populate all of the teams for the league, including the Teams object

        Returns:
            Teams: list of Team
        """
        jsonObject = self.getUsersInLeagueAPI()
        self.createTeamsAndPopulateList(jsonObject)
        return self.TeamsDict

    def populateMatchups(self):
        """Populates the matchups objects for the league
        """
        jsonObject = self.getMatchupsInLeagueAPI()
        self.createMatchupsAndLink(jsonObject)

    def getUsersInLeagueAPI(self):
        """Call sleeper's API to get all users for the league
        Returns:
            response: JSON object of users for leagues
        """
        response = requests.get("https://api.sleeper.app/v1/league/" + self.LeagueId + "/users")
        return response.json()

    def createTeamsAndPopulateList(self, jsonObject: dict):
        """creates the teams objects and populates the lists

        Args:
            jsonObject (dict): json object of teams
        """
        for i in range(0,len(jsonObject)):
            rawTeam = jsonObject.pop()
            userId = rawTeam['user_id']
            displayName = rawTeam['display_name']
            team = Team.Team(userId, displayName)
            self.TeamsDict[team.UserId] = team
            
    def getMatchupsInLeagueAPI(self):
        """Call sleeper to get the matchups

        Returns:
            list: list of json objects
        """
        responseArray = []
        for week in range(1, self.NumWeeks + 1): #1 to +1 because we are working with a specific week
            response = requests.get("https://api.sleeper.app/v1/league/" + self.LeagueId + "/matchups/" + str(week))
            responseArray.append(response.json())
        return responseArray
    
    def createMatchupsAndLink(self, jsonArray):
        """This populates each team record with matchups and points

        Args:
            jsonArray (dict): object that contains all matchups for the league
        """
        for weekIndex in range(len(jsonArray)):
            rawMatchup = jsonArray[weekIndex]
            for j in range(len(rawMatchup)):
                rosterId = rawMatchup[j]['roster_id']
                points = rawMatchup[j]['points']
                matchupId = rawMatchup[j]['matchup_id']
                ownerId = self.Rosters.GetOwnerFromRosterId(rosterId)
                team = self.TeamsDict[ownerId]
                team.addMatchupToDict(weekIndex, matchupId, points)
                self.Weeks[weekIndex].addTeamToDict(points, team)
                team.AddWin(self.wonMatchup(j, rawMatchup))
    def wonMatchup(self, index, matchup):
        
        matchupId = matchup[index]['matchup_id']
        points = matchup[index]['points']
        for i in range(len(matchup)):
            if index == i:
                continue
            elif matchupId == matchup[i]['matchup_id']:
                if matchup[i]['points'] < points:
                    return True
                else:
                    return False
        return False

    def populateMedianWins(self):
        """Take the weeks object, and populate the median wins object with the info
        """
        if (self.IncludeMedianWins):
            for i in range (len(self.Weeks)):
                week = self.Weeks[i]
                self.MedianWins.populateMedianWinnersForWeek(week)

            self.MedianWins.giveWinsToTeams()

    def teamsDictToArray(self):
        """Take the dictionary and pass back an array of just teams
        """

        teamArray = []

        arrays = list(self.TeamsDict.items())

        for i in range(len(arrays)):
            team = arrays[i][1]
            teamArray.append(team)

        return teamArray

    def populateOriginalSeeds(self):
        teamArray = self.teamsDictToArray()

        teamArray = self.mergeSortTeamByWins(teamArray)

        for i in range(len(teamArray)):
            teamArray[i].ActualSeed = (i + 1)


    def mergeSortTeamByWins(self, teamArray):

        if (len(teamArray) == 1):
            return teamArray
        
        midPoint = len(teamArray) // 2

        leftArray = teamArray[midPoint:]
        rightArray = teamArray[:midPoint]

        leftArray = self.mergeSortTeamByWins(leftArray)
        rightArray = self.mergeSortTeamByWins(rightArray)

        mergedArray = []

        leftCounter = 0
        rightCounter = 0

        while (leftCounter < len(leftArray)):
            if (rightCounter < len(rightArray)):
                if (leftArray[leftCounter].getActualWins() > rightArray[rightCounter].getActualWins()):
                    mergedArray.append(leftArray[leftCounter])
                    leftCounter += 1
                else:
                    mergedArray.append(rightArray[rightCounter])
                    rightCounter += 1
            else:
                mergedArray.append(leftArray[leftCounter])
                leftCounter += 1
        remainingRightCounter = rightCounter
        for rightCounter in range(remainingRightCounter, len(rightArray)):
            mergedArray.append(rightArray[rightCounter])
            rightCounter += 1

        return mergedArray










