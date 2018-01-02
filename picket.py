# in_fence checks if a given point lies inside a given fence polygon.
# Parameters are given as an instance of the fence class and a given point as a
# tuple of (x, y).
def in_fence(fence, point):
    # First, find the horozontal line equation that passes through the point.
    # Using the y = mx + c fomat, express as a tuple of (m, c). As the line will
    # always be horizontal, the equation will give constant output (y = n).
    point_horizon_eqn = (point[1], 0)

    # Next, form equations with the list of points given by the Fence object.
    if len(fence.points) < 3:
        raise Exception("The supplied fence has not enough (< 3) points!")
    # Form list of line equations. Last in list will circle back to first point.
    # E.g. fence.points = [(A), (B), (C)], line_eqns = [(AB), (BC), (CA)].
    line_eqns = []


# Class to define a fence.
class Fence:
    # Points are given as tuples
    points = None
    def __init__(self):
        self.points = []
    def add_point(self, point):
        self.points.append(point)
