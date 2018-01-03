# in_fence checks if a given point lies inside a given fence polygon.
# Parameters are given as an instance of the fence class and a given point as a
# tuple of (x, y).
def in_fence(fence, point, verbose = False):
    # First, find the horozontal line equation that passes through the point.
    # Using the y = mx + c fomat, express as a tuple of (m, c). As the line will
    # always be horizontal, the equation will give constant output (y = n).
    point_horizon_eqn = (point[1], 0)

    # Next, form equations with the list of points given by the Fence object.
    if len(fence.points) < 3:
        raise Exception("The supplied fence has not enough (< 3) points!")
    # Form list of line equations. Last in list will circle back to first point.
    # E.g. fence.points = [(A), (B), (C)], line_eqns = [(AB), (BC), (CA)].
    # Where each element in the line_eqns list is a tuple of (m, c).
    line_eqns = []
    for point_index in range(len(fence.points)):
        point1 = fence.points(point_index)
        # If point1 is the last in the list, point2 is the first element of the
        # list.
        if point_index == (len(fence.points) - 1):
            point2 = fence.points[0]
        else:
            point2 = fence.points(point_index + 1)
        # Delta y over delta x == gradient.
        c = ((point2[1] - point1[1]) / (point2[0] - point1[0]))
        # Find m by substitution using point1.
        m = ((point1[1] - c) / point1[0])
        if vebose == True:
            print("Formed equation y=" + m + "x+" + c, "from point:", point1, "and", point2)
        line_eqns.append((m, c))

# Class to define a fence.
class Fence:
    # Points are given as tuples
    points = None
    def __init__(self):
        self.points = []
    def add_point(self, point):
        self.points.append(point)
    def list_points(self):
        return(self.points)
