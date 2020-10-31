class Week():
    """
    Corresponds to a week of fantasy football, with teams and their points, independent of wins being determined
    """
    
    WeekIndex: int #This is the NFL week minus one

    teamScoresDict: dict #points is the key, team is the value

    teamArray: list # array

    def __init__(self, weekIndex):
        self.WeekIndex = weekIndex
        self.teamScoresDict = {}
        self.teamArray = []

    def addTeamToDict(self, points, team):
        self.teamArray.append(team)
        self.teamScoresDict[team] = points

    def getWeekTopMedianScorers(self):
        """Returns the top half of scorers for the week. Not guaranteed to
        be in sorted order

        Returns:
            array: Array of teams objects - half as many as are in league
        """
        self.teamArray = self.mergeSortTeamArray(self.teamArray)

        midpoint = len(self.teamArray) // 2

        return self.teamArray[midpoint:]


    def mergeSortTeamArray(self, array):

        if len(array) == 1:
            return array

        midpoint = len(array) // 2

        leftArray = array[:midpoint]
        rightArray = array[midpoint:]

        leftArray = self.mergeSortTeamArray(leftArray)
        rightArray = self.mergeSortTeamArray(rightArray)

        mergedArray = []

        leftCounter = 0
        rightCounter = 0

        while (leftCounter < len(leftArray)):
            
            if (rightCounter < len(rightArray)):

                if (self.teamScoresDict[leftArray[leftCounter]] < self.teamScoresDict[rightArray[rightCounter]]):
                    mergedArray.append(leftArray[leftCounter])
                    leftCounter += 1
                else:
                    mergedArray.append(rightArray[rightCounter])
                    rightCounter += 1
            else:
                mergedArray.append(leftArray[leftCounter])
                leftCounter += 1

        remainingRightCounter = rightCounter

        for rightCounter in range(remainingRightCounter, len(rightArray)):
            mergedArray.append(rightArray[rightCounter])
        return(mergedArray)
