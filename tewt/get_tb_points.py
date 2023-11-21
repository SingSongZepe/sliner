import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_nearest_points(points, p):
    nearest_up = None
    nearest_down = None
    min_distance_up = math.inf
    min_distance_down = math.inf

    for point in points:
        distance = abs(point.y - p.y)

        if point.y < p.y:
            if distance < min_distance_up:
                min_distance_up = distance
                nearest_up = point
        elif point.y > p.y:
            if distance < min_distance_down:
                min_distance_down = distance
                nearest_down = point

    return nearest_up, nearest_down

if __name__ == '__main__':
    points = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4), Point(5, 5)]
    p = Point(3, 1)

    nearest_up, nearest_down = get_nearest_points(points, p)

    print("nearest up:", nearest_up.x, nearest_up.y)
    print("nearest down:", nearest_down.x, nearest_down.y)

