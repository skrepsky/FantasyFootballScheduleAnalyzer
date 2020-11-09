class Team:
    UserId: str
    DisplayName: str
    MatchupDict: dict

    def __init__(self, userId: str, displayName: str):

        self.UserId = userId
        self.DisplayName = displayName

    
    def addMatchupToDict(self, week, matchupId, points):
        self.MatchupDict.update(week, MatchupId = matchupId, Points = points)




