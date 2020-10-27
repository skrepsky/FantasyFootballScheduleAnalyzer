import requests
import Team
import Rosters

class League:
    Teams: list
    IncludeMedianWins: bool
    CurrentYear: int
    LeagueId: str
    NumWeeks: int
    Rosters: Rosters

    
    def __init__(self, leagueId: str, currentYear: int):
        """Initializes the league class

        Args:
            leagueId (str): league id
            currentYear (int): 4 digit year to process
        """
        self.LeagueId = leagueId
        self.CurrentYear = currentYear
        self.IncludeMedianWins = True #TODO - include by default for now
        self.Teams = []
        self.NumWeeks = 17 #TODO - there could be 18 this year, you never know...
        self.Rosters = Rosters.Rosters(leagueId)

    def populateTeams(self):
        """Populate all of the teams for the league, including the Teams object

        Returns:
            Teams: list of Team
        """
        jsonObject = self.getUsersInLeagueAPI()
        self.createTeamsAndPopulateList(jsonObject)
        return self.Teams

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
            self.Teams.append(team)
            
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

        for i in range(0,len(jsonArray)):
            rawMatchup = jsonArray[i]

