class Team:
    UserId: str
    DisplayName: str
    MatchupDict: dict
    MedianWin: int
    SimulatedWins: int
    SimulatedLosses: int
    SimulatedTies: int

    def __init__(self, userId: str, displayName: str):

        self.UserId = userId
        self.DisplayName = displayName
        self.MatchupDict = {}
        self.MedianWin = 0
        self.resetSimulatedWLT()
    
    def addMatchupToDict(self, weekIndex, matchupId, points):
        self.MatchupDict[weekIndex] = {"matchupId" : matchupId, "points" : points}

    def getPointsForWeek(self, weekIndex):
        return self.MatchupDict[weekIndex]["points"]

    def addMedianWin(self):
        self.MedianWin += 1

    def addSimulatedWin(self):
        self.SimulatedWins += 1

    def addSimulatedLoss(self):
        self.SimulatedLosses += 1

    def addSimulatedTie(self):
        self.SimulatedTies += 1

    def resetSimulatedWLT(self):
        self.SimulatedWins = 0
        self.SimulatedLosses = 0
        self.SimulatedTies = 0









