import requests
import Team
class League:
    Teams: list
    IncludeMedianWins: bool
    CurrentYear: int
    LeagueId: str
    NumWeeks: int

    def __init__(self, leagueId: str, currentYear: int):
        self.LeagueId = leagueId
        self.CurrentYear = currentYear
        self.IncludeMedianWins = True #TODO - include by default for now
        self.Teams = []
        self.NumWeeks = 17 #TODO - there could be 18 this year, you never know...

    def populateTeams(self):
        jsonObject = self.getUsersInLeagueAPI()
        self.createTeamsAndPopulateList(jsonObject)
        return self.Teams

    def populateMatchups(self):
        jsonObject = self.getMatchupsInLeagueAPI()
        self.createMatchupsAndLink(jsonObject)

    def getUsersInLeagueAPI(self):
        response = requests.get("https://api.sleeper.app/v1/league/" + self.LeagueId + "/users")
        return response.json()

    def createTeamsAndPopulateList(self, jsonObject: dict):

        for i in range(0,len(jsonObject)):
            rawTeam = jsonObject.pop()
            userId = rawTeam['user_id']
            displayName = rawTeam['display_name']
            team = Team.Team(userId, displayName)
            self.Teams.append(team)
            
    def getMatchupsInLeagueAPI(self):
        responseArray = []
        for week in range(1, self.NumWeeks + 1): #1 to +1 because we are working with a specific week
            response = requests.get("https://api.sleeper.app/v1/league/" + self.LeagueId + "/matchups/" + str(week))
            responseArray.append(response.json())
        return responseArray
    
    def createMatchupsAndLink(self, jsonArray):
        for i in range(0,len(jsonArray)):
            rawMatchup = jsonArray[i]

