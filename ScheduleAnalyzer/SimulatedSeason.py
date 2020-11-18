from MedianWins import MedianWins
import Team

class SimulatedSeason():
    
    
    NumWeeks: int
    Teams: list
    
    def __init__(self, numWeeks: int, initialArray: list):
        self.NumWeeks = numWeeks
        self.Teams = initialArray

    def simulateSeason(self):
    
        teamArray = self.Teams
        for i in range(0, self.NumWeeks):
            self.playOutWeek(i, teamArray)
            self.advanceScheduleToNextWeek(teamArray)

        for i in range(len(teamArray)):
            if teamArray[i].DisplayName == 'plammert':
                wins = teamArray[i].MedianWin + teamArray[i].SimulatedSeasonWins
                if wins < 14:
                    print(wins)
                    for weekIndex in range(self.NumWeeks):
                        matchupId = teamArray[i].MatchupDict[weekIndex].matchupId
                        for possibleOpponent in range(len(teamArray)):
                            
                    
        self.evaluateSeason()

    def playOutWeek(self, weekIndex, teamArray):
        
        for i in range(0, len(teamArray), 2):
            team1 = teamArray[i]
            team2 = teamArray[i+1]
            self.calculateWLT(weekIndex, team1, team2)


    def calculateWLT(self,weekIndex, team1: Team.Team, team2: Team.Team):
        team1Points = team1.getPointsForWeek(weekIndex)
        team2Points = team2.getPointsForWeek(weekIndex)
        if (team1Points > team2Points):
            self.updateTeamWLT(team1,team2, None, None)
        elif (team1Points < team2Points):
            self.updateTeamWLT(team2, team1, None, None)
        else:
            self.updateTeamWLT(None,None,team1,team2)


    def updateTeamWLT(self, winningTeam: Team.Team, losingTeam: Team.Team, tyingTeam1: Team.Team, tyingTeam2: Team.Team):
        if (winningTeam is not None):
            winningTeam.addSimulatedWin()
        if (losingTeam is not None):
            losingTeam.addSimulatedLoss()
        if (tyingTeam1 is not None):
            tyingTeam1.addSimulatedTie
        if (tyingTeam2 is not None):
            tyingTeam2.addSimulatedTie


    def advanceScheduleToNextWeek(self,teamArray):
        
        #Index 0 remains fixed 
        newArray = []
        newArray.append(teamArray[0])
        
        # position 1 - n move up 1, with n wrapping around to take index 1
        newArray.append(teamArray[len(teamArray)-1])

        #Handle remaining values
        newArray.extend(teamArray[1:len(teamArray)-2])

        return newArray

    def evaluateSeason(self):

        self.Teams = self.mergeSortBySimulatedWins(self.Teams)

        midPoint = len(self.Teams) // 2
        madePlayoffs = False
        seed = 0

        for i in range (0, len(self.Teams)):
            if i < midPoint:
                madePlayoffs =  False
            else:
                madePlayoffs = True
            seed = len(self.Teams) - i
            self.Teams[i].addSeedAndReset(seed, madePlayoffs)

    def mergeSortBySimulatedWins(self, teamArray: list):

        if (len(teamArray) == 1):
            return teamArray
        midPoint = len(teamArray) // 2

        leftArray = teamArray[midPoint:]
        rightArray = teamArray[:midPoint]

        leftArray = self.mergeSortBySimulatedWins(leftArray)
        rightArray = self.mergeSortBySimulatedWins(rightArray)

        mergeArray = []

        leftCounter = 0
        rightCounter = 0

        while (leftCounter < len(leftArray)):
            if rightCounter < len(rightArray):
                if leftArray[leftCounter].getWinsTotal() < rightArray[rightCounter].getWinsTotal():
                    mergeArray.append(leftArray[leftCounter])
                    leftCounter += 1
                else:
                    mergeArray.append(rightArray[rightCounter])
                    rightCounter += 1
            else:
                mergeArray.append(leftArray[leftCounter])
                leftCounter += 1
        remainingRightCounter = rightCounter

        for rightCounter in range (remainingRightCounter, len(rightArray)):
            mergeArray.append(rightArray[rightCounter])
        
        return mergeArray


            

    





