from random import shuffle
import League
import Team
from SimulatedSeason import SimulatedSeason

def main():
    driver = Driver()
    
    print(driver.mainDriver())

class Driver:
    def mainDriver(self):

        leagueId = '605590064432504832'
        year = 2020
        numWeeksCompleted = 8
        numSimulations = 10000

        league = League.League(leagueId,year,numWeeksCompleted)
        league.populateTeams()
        league.populateMatchups()
        league.populateMedianWins()
        league.populateOriginalSeeds()
        
        teamArray = league.teamsDictToArray()

        self.playSimulatedSeasons(numSimulations, teamArray, numWeeksCompleted)
        
        simulationSummary = self.evaluateResults(teamArray, numSimulations)
        
        self.printResults(simulationSummary)


    def playSimulatedSeasons(self, numSeasons, teamArray, numWeeks):
        
        for i in range(numSeasons):
            simSeason = SimulatedSeason(numWeeks, teamArray)
            simSeason.simulateSeason()
            shuffle(teamArray)

    def evaluateResults(self, teamArray, numSimulations):

        sortedTeamArray = self.mergeSortOfSimulatedSeasons(teamArray)

        simulation_summary = []

        for i in range(len(sortedTeamArray)):
            team: Team.Team = sortedTeamArray[i] 
            teamName: str = team.DisplayName #0 - team name
            actualSeed: int = team.ActualSeed #1 - actual seed
            averageSeed: float = round(team.TotalPlayoffSeeds / numSimulations, 2) #2 - average seed
            actualWins: int = team.ActualWins + team.MedianWin #3 - actual wins
            averageWins: float = round(team.MedianWin + (team.TotalSimulatedSeasonWins / numSimulations), 2) #4 - average wins
            playoffPercentage: float = round(100 * (team.TotalPlayoffAppearances / numSimulations), 2) #5 - playoff chance

            simulation_summary.append([teamName,actualSeed,averageSeed,actualWins,averageWins,playoffPercentage])

        return simulation_summary

    def printResults(self, simulation_summary):
        self.formatted_print(["Team", "Current Seed", "Avg Seed", "Wins", "Avg Wins", "% in Playoffs"])
        
        for i in range(len(simulation_summary)):
            self.formatted_print(simulation_summary[i])


    def formatted_print(self, x):
        print(
            '{:>20}'.format(str(x[0])) +
            '{:>15}'.format(str(x[1])) +
            '{:>10}'.format(str(x[2])) + 
            '{:>7}'.format(str(x[3])) +
            '{:>10}'.format(str(x[4])) +
            '{:>15}'.format(str(x[5])))
        

    def mergeSortOfSimulatedSeasons(self, teamArray):
        if (len(teamArray) == 1):
            return teamArray

        midPoint = len(teamArray) // 2

        leftArray = teamArray[midPoint:]
        rightArray = teamArray[:midPoint]

        leftArray = self.mergeSortOfSimulatedSeasons(leftArray)
        rightArray = self.mergeSortOfSimulatedSeasons(rightArray)

        mergedArray = []

        leftCounter = 0
        rightCounter = 0

        while (leftCounter < len(leftArray)):
            if (rightCounter < len(rightArray)):
                if (leftArray[leftCounter].TotalPlayoffSeeds < rightArray[rightCounter].TotalPlayoffSeeds): #Todo this is the eval line
                    mergedArray.append(leftArray[leftCounter])
                    leftCounter += 1
                else:
                    mergedArray.append(rightArray[rightCounter])
                    rightCounter += 1
            else:
                mergedArray.append(leftArray[leftCounter])
                leftCounter += 1
        remainingRightCount = rightCounter
        for rightCounter in range(remainingRightCount, len(rightArray)):
            mergedArray.append(rightArray[rightCounter])
        
        return mergedArray


if __name__ == '__main__':
    main()
    