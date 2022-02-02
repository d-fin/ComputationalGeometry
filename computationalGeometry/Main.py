'''
Group: David Finley
       Brett Kessler
       William Collins
       PJ
       
This program runs through the basics of computational geometry.  
'''
from Points import Points 
from LineSegments import LineSegment
import random 

def main():
    ''' Creating point objects and checking for duplicates. 
    for now I just create 5 points with random integers.
    if duplicate is found it does not add the point/ '''
    points = []
    for i in range(0, 5):
        rand1 = random.randint(-10, 10)
        rand2 = random.randint(-10, 10)
        if len(points) != 0:
            for i in points:
                duplicateCheck = (rand1, rand2)
                obj = i.getPoints()
                if obj == duplicateCheck:
                    break 
                else:
                    point = Points(rand1, rand2)
                    points.append(point)
                    break
        else:
            point = Points(rand1, rand2)
            points.append(point)
    
    ''' Calculating the points with the shortest distance '''
    distances = []
    pairsOfPoints = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            point1 = points[i].getPoints()
            point2 = points[j].getPoints()
            pair = [point1, point2]
            pairsOfPoints.append(pair)
            distances.append(euclideanDistance(point1, point2))
    
    index = distances.index(min(distances), 0, len(distances))
    smallestDistance = int(distances[index])
    smallestDistanceWithPoints = pairsOfPoints[index]
    print(f'Smallest distance between two points: {smallestDistance}\nPoints: {smallestDistanceWithPoints}')

    ''' ---------------------------------------------------------------------------------------------------- '''
    ''' Bretts part '''
    
    ''' Calculating the convex hull to find the smallest convex polyhedron '''
    ch = ConvexHull()
    for _ in range(50):
        ch.add(Points(random.randint(-100, 100), random.randint(-100, 100)))
    print("Points on hull:", ch.get_hull_points())
    

''' The function below calculates the distances between the points provided '''
def euclideanDistance(coordinate1, coordinate2):
        return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)
    
''' This function calculates to find the smallest convex polyhedron/polygon containing all the points '''
class ConvexHull(object):  
    
    def __init__(self):
        self._points = []
        self._hull_points = []

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        Negative if p1 is clockwise of p2.
        :param p1:
        :param p2:
        :return: integer
        '''
        difference = (
            ((p2.xPoint - origin.xPoint) * (p1.yPoint - origin.yPoint))
            - ((p1.xPoint - origin.xPoint) * (p2.yPoint - origin.yPoint))
        )

        return difference

    def compute_hull(self):
        '''
        Computes the points that make up the convex hull.
        :return:
        '''
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.xPoint
        for p in points[1:]:
            if p.xPoint < min_x:
                min_x = p.xPoint
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

if __name__ == '__main__':
    main()