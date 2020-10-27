import requests
import League

def main():
    driver = Driver()
    
    print(driver.mainDriver())

class Driver:
    def mainDriver(self):
        league = League.League('605590064432504832',2020)
        league.populateTeams()
        league.populateMatchups()

if __name__ == '__main__':
    main()
    