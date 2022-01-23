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
