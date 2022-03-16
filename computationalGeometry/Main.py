'''
Group: David Finley
       Brett Kessler
       William Collins
       PJ
       
This program runs through the basics of computational geometry.  
'''

from Points import Points 
from LineSegments import LineSegment
from ConvexHull import ConvexHull
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
            distances.append(Points.euclideanDistance(point1, point2))
    
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

if __name__ == '__main__':
    main()