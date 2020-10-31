class Team:
    UserId: str
    DisplayName: str
    MatchupDict: dict
    MedianWin: int

    def __init__(self, userId: str, displayName: str):

        self.UserId = userId
        self.DisplayName = displayName
        self.MatchupDict = {}
        self.MedianWin = 0
    
    def addMatchupToDict(self, weekIndex, matchupId, points):
        self.MatchupDict[weekIndex] = {"matchupId" : matchupId, "points" : points}

    def getPointsForWeek(self, weekIndex):
        return self.MatchupDict[weekIndex]["points"]

    def addMedianWin(self):
        self.MedianWin += 1







