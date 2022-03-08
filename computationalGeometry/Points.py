'''
@author: David
'''

''' Points class creates an object for an x and y coordinate.
    Other functions include a print function and a function to return the points as a tuple.
 '''
class Points:
    def __init__(self, x, y):
        self.xPoint = x
        self.yPoint = y 
        
    def printPoints(self):
        print(f'X coordinate: {self.xPoint}\nY coordinate: {self.yPoint}')
        
    def getPoints(self):
        return (self.xPoint, self.yPoint)

    def euclideanDistance(coordinate1, coordinate2):
        return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)
  
