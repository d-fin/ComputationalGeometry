from computationalGeometry.Points import Points 
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
    