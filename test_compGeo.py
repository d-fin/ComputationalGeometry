from computationalGeometry.Points import Points 
from computationalGeometry.ConvexHull import ConvexHull
import random 

points = []

def test_Points():
    for i in range(0, 50):
        points.append(Points(random.randint(-100, 100), random.randint(-100, 100)))


def test_euclideanDistance():
    points = [ (-6, 3), (8, 5), (4, -3), (9, -2), (-7, 6) ]
    distance = []

    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]
            distance.append(Points.euclideanDistance(point1, point2))
    
    assert distance.index(min(distance), 0, len(distance)) == 3

def test_convexHull():
    x = [ (4, 7), (-2, -5), (10, -4), (-3, 5), (9, 8), (-2, -7), (6, 1), (2, 4), (-6, 8), (-3, 9) ]
    ans = [ (-6, -8), (10, -4), (9, 8), (-3, 9), (6, -8) ]
    points = []
    ch = ConvexHull()
    for i in x:
        points.append(Points(i[0], i[1]))

    pointsOnHull = ch.get_hull_points()
    
    for j in range(0, len(pointsOnHull)):
        assert pointsOnHull[j] == ans[j]
    
