import requests
import League
from SimulatedSeason import SimulatedSeason

def main():
    driver = Driver()
    
    print(driver.mainDriver())

class Driver:
    def mainDriver(self):
        league = League.League('605590064432504832',2020,8)
        league.populateTeams()
        league.populateMatchups()
        league.populateMedianWins()
        
        simSeason = SimulatedSeason(8,league.teamsDictToArray())
        simSeason.simulateSeason()
        print(simSeason)

if __name__ == '__main__':
    main()
    