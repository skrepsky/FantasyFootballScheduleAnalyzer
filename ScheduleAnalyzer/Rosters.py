import Team
import requests

class Rosters():

    RosterDict: dict
    
    def __init__(self, leagueId):
        self.RosterDict = {}
        jsonObject = self.callRostersAPI(leagueId)
        self.populateRosters(jsonObject)

    def callRostersAPI(self, leagueId):
        """calls the sleeper api to get the rosters

        Args:
            leagueId (str): League id

        Returns:
            dict: json object with all rosters
        """
        response = requests.get("https://api.sleeper.app/v1/league/" + leagueId + "/rosters")
        return response.json()

    def populateRosters(self,jsonObject):
        """Given the json object, populate our rosters dictionary

        Args:
            jsonObject (dict): A dict of json objects
        """
        for i in range(len(jsonObject)):
            self.RosterDict[jsonObject[i]["roster_id"]] = jsonObject[i]["owner_id"]

