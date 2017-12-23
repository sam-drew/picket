# in_fence checks if a given point lies inside a given fence polygon.
# Parameters are given as an instance of the fence class and a given point as a
# tuple.
def in_fence(fence, point):
    intersection_count = 0
    # First find the min and max x values.
    max_x = 0.0
    max_y = 0.0
    min_x = 0.0
    min_y = 0.0
    for point in fence.points:
        if point[0] > max_x:
            max_x = point[0]
        elif point[0] < min_x:
            min_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
        elif point[1] < min_y:
            min_y = point[1]
    # Point line in the form (m, c)
    point_line_eqn = (0, point[1])
    # For all lines, work out if the point line intersects.
    for index in range(len(fence.points) + 1):
        test_line = (fence.points[index - 1], fence.points[index])
        # Find lines in form y = mx + c
        # x_eqn in form (m, c)
        test_line_eqn = [None, None]
        # Find m
        test_line_eqn[0] = (test_line[0][1] - test_line[1][1]) / (test_line[0][0] - test_line[1][0])
        if test_line_eqn[0] != point_line_eqn[0]:
            # There is a point of intersection, so calculate and return it
            # Find c
            test_line_eqn[1] = test_line[0][1] - (test_line_eqn[0] * test_line[0][0])
            # c2 -c1 / m1 -m2
            intersection_x = (test_line_eqn[1] - point_line_eqn[1]) / (point_line_eqn[0] - test_line_eqn[0])
            intersection_y = (intersection_x * point_line_eqn[0]) + point_line_eqn[1]
            if intersection_x > min_x and intersection_x < max_x and intersection_y > min_y and intersection_y < max_y:
                intersection_count += 1
        else:
            # No intersection; lines are paralel.
            pass
    if intersection_count % 2 == 0:
        # Point is in fence (at least defo for regular shapes)
        return(True)
    else:
        return(False)

# Class to define a fence.
class Fence:
    # Points are given as tuples
    points = None
    def __init__(self):
        self.points = []
    def add_point(self, point):
        self.points.append(point)
