from Week import Week

class MedianWins():

    MedianWinnersByWeek: dict
    
    def __init__(self):
        self.MedianWinnersByWeek = {}
    
    def populateMedianWinnersForWeek(self, weekObject: Week):
        """given a week object, pull the median winners from it and populate the dictionary object

        Args:
            weekObject (Week): object to add wins for
        """
        teams = weekObject.getWeekTopMedianScorers()
        self.MedianWinnersByWeek[weekObject.WeekIndex] = teams

    def giveWinsToTeams(self):
        """Go through the median winners object, and update all teams' median wins
        """
        while(len(self.MedianWinnersByWeek) > 0):
            medianWinnersForWeekByScore = self.MedianWinnersByWeek.popitem()

            for j in range(len(medianWinnersForWeekByScore[1])): #TODO - investigate whey the 0 item is the length as opposed to the array
                medianWinnersForWeekByScore[1][j].addMedianWin()



        
