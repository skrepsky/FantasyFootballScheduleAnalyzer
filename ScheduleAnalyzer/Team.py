class Team:
    UserId: str
    DisplayName: str
    MatchupDict: dict
    MedianWin: int
    SimulatedSeasonWins: int
    SimulatedSeasonLosses: int
    SimulatedSeasonTies: int
    TotalSimulatedSeasonWins: int
    TotalSimulatedSeasonLosses: int
    TotalSimulatedSeasonTies: int
    TotalPlayoffAppearances: int
    TotalPlayoffSeeds: int
    ActualSeed: int
    ActualWins: int


    def __init__(self, userId: str, displayName: str):

        self.UserId = userId
        self.DisplayName = displayName
        self.MatchupDict = {}
        self.MedianWin = 0
        self.SimulatedSeasonWins = 0
        self.SimulatedSeasonLosses = 0
        self.SimulatedSeasonTies = 0
        self.TotalSimulatedSeasonWins = 0
        self.TotalSimulatedSeasonLosses = 0
        self.TotalSimulatedSeasonTies = 0
        self.TotalPlayoffAppearances = 0
        self.TotalPlayoffSeeds = 0
        self.ActualSeed = 0 #TODO need to update
        self.ActualWins = 0 
    
    def addMatchupToDict(self, weekIndex, matchupId, points):
        self.MatchupDict[weekIndex] = {"matchupId" : matchupId, "points" : points}

    def AddWin(self,wonGame):
        if wonGame:
            self.ActualWins += 1

    def getPointsForWeek(self, weekIndex):
        return self.MatchupDict[weekIndex]["points"]
    def getActualWins(self):
        return self.ActualWins + self.MedianWin
        
    def addMedianWin(self):
        self.MedianWin += 1

    def addSimulatedWin(self):
        self.SimulatedSeasonWins += 1

    def addSimulatedLoss(self):
        self.SimulatedSeasonLosses += 1

    def addSimulatedTie(self):
        self.SimulatedSeasonTies += 1

    def getWinsTotal(self):
        return 1 * self.SimulatedSeasonWins + .5 * self.SimulatedSeasonTies + self.MedianWin

    def addSeedAndReset(self, seed:int, inPlayoffs: bool):
        if (inPlayoffs):
            self.TotalPlayoffAppearances += 1
        
        self.TotalPlayoffSeeds += seed

        self.updateAndResetSimulatedWLT()


    def updateAndResetSimulatedWLT(self):

        self.TotalSimulatedSeasonWins += self.SimulatedSeasonWins
        self.TotalSimulatedSeasonLosses += self.SimulatedSeasonLosses
        self.TotalSimulatedSeasonTies += self.SimulatedSeasonTies

        self.SimulatedSeasonWins = 0
        self.SimulatedSeasonLosses = 0
        self.SimulatedSeasonTies = 0









