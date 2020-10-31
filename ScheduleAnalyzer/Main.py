import requests
import League

def main():
    driver = Driver()
    
    print(driver.mainDriver())

class Driver:
    def mainDriver(self):
        league = League.League('605590064432504832',2020,8)
        league.populateTeams()
        league.populateMatchups()
        league.populateMedianWins()

if __name__ == '__main__':
    main()
    