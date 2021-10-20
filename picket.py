# Picket. Calculate if a point is inside a fence.
# Copyright (C) 2017-2018  Sam Drew

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Class to define a fence.
class Fence:
    """
    A Fence object is primarily a way of containing a list of points that form
    a boundary, and providing the ability to add / change points in the fence.
    """

    points = None

    def __init__(self):
        self.points = []

    def add_point(self, point):
        # Add new point to points list.
        self.points.append(point)

    def list_points(self):
        return(self.points)

    def check_point(self, point, debug = False):
        """
        check_point()  checks if a given point lies inside a given fence polygon.
        Parameters are given as an instance of the fence class and a given point as
        a, tuple of (x, y).
        """
        def check_in_bounds(point, line_eqns_index):
            """
            check_in_bounds() checks if a supplied point is within the upper and
            lower x & y bounds of the points that form a given line.

            Takes the point to be checked and the index that points to which line
            is being tested. Knowing the location of the line equation in its list
            we can find the points that it is formed from.

            Returns true if the point is within bound and false if it's outside
            bounds.
            """
            withinX = False;
            withinY = False;

            pointA = self.points[line_eqns_index]
            # If the index is pointing to the last member of the list, the line
            # is made of points that wrap around back to the start of the points
            # list.
            if line_eqns_index + 1 == len(self.points):
                pointB = self.points[0]
            else:
                pointB = self.points[line_eqns_index + 1]

            print(point)
            print(pointA, pointB)
            # Check if point[x] is within pointA[x] and pointB[x].
            if (pointA[0] >= pointB[0]):
                # pointA is more positive than pointB so check if point[x] is
                # between these.
                if (point[0] <= pointA[0] and point[0] >= pointB[0]):
                    withinX = True
            elif (pointA[0] <= pointB[0]):
                # pointA is less positive than pointB.
                if (point[0] >= pointA[0] and point[0] <= pointB[0]):
                    withinX = True

            # Check if point[y] is within pointA[y] and pointB[y].
            if (pointA[1] >= pointB[1]):
                print("pointA[1] >= pointB[1]")
                # pointA is more positive than pointB so check if point[y] is
                # between these.
                if (point[1] <= pointA[1] and point[1] >= pointB[1]):
                    withinY = True
            elif (pointA[1] <= pointB[1]):
                print("pointA[1] <= pointB[1]")
                # pointA is less positive than pointB.
                if (point[1] >= pointA[1] and point[1] <= pointB[1]):
                    withinY = True

            print(withinX, withinY)

            if withinX and withinY:
                return True
            else:
                return False

        # Find numbe of intersections of the fence with the point horizon line on
        # either side of the point.
        def find_intersect(line, point_horizon_eqn):
            """
            find_intersect() returns a coordinate if an intersection exists, and
            False if not.

            Uses Cramers rule to work it out.
            """
            # Calculate the determinant.
            D  = line[0] * point_horizon_eqn[1] - line[1] * point_horizon_eqn[0]
            Dx = line[2] * point_horizon_eqn[1] - line[1] * point_horizon_eqn[2]
            Dy = line[0] * point_horizon_eqn[2] - line[2] * point_horizon_eqn[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return (x, y)
            else:
                return False

        # First, find the horozontal line equation that passes through the point.
        # Using the Ax + By = C fomat, express as a tuple of (A, B, C).
        point_horizon_eqn = (0, 1, point[1])

        # Next, form equations with the list of points given by the Fence object.
        if len(self.points) < 3:
            raise Exception("The supplied fence has not enough (< 3) points!")
        # Form list of line equations. Last in list will circle back to first point.
        # E.g. self.points = [(A), (B), (C)], line_eqns = [(AB), (BC), (CA)].
        # Where each element in the line_eqns list is a tuple of (m, c).
        line_eqns = []
        for point_index in range(len(self.points)):
            point1 = self.points[point_index]
            # If point1 is the last in the list, point2 is the first element of the
            # list.
            if point_index == (len(self.points) - 1):
                point2 = self.points[0]
            else:
                point2 = self.points[point_index + 1]
            # Check if vertical or horizontal line first.
            if point1[1] == point2[1]:
                # Hoizontal
                a = 0
                b = 1
                c = point1[1]
                if debug == True:
                    print("Formed equation", str(a) + "x+" + str(b) + "y=" + str(c), "from points:", point1, "and", point2)
                line_eqns.append((a, b, c))
            elif point1[0] == point2[0]:
                # Vertical
                a = 1
                b = 0
                c = point1[0]
                if debug == True:
                    print("Formed equation", str(a) + "x+" + str(b) + "y=" + str(c), "from points:", point1, "and", point2)
                line_eqns.append((a, b, c))
            else:
                # Non vertical or hoizontal line.
                a = (-1 * ((point2[1] - point1[1]) / (point2[0] - point1[0])))
                b = 1
                # c = y - ax
                c = (point1[1] + (a * point1[0]))
                if debug == True:
                    print("Formed equation", str(a) + "x+" + str(b) + "y=" + str(c), "from points:", point1, "and", point2)
                line_eqns.append((a, b, c))

        if debug == True:
            print("\n")
            print("All equations formed (in order):", line_eqns)
            print("Finding intersections...\n")
#            print("\nx bounds are:", str(self.max_x), str(self.min_x), "y bounds:", str(self.max_y), str(self.min_y))
        intersection_points_left = []
        intersection_points_right = []
        for line_index in range(0, len(line_eqns)):
            intersection_point = find_intersect(line_eqns[line_index], point_horizon_eqn)
            if debug == True:
                print("Intersection point between lines:", line_eqns[line_index], "&", point_horizon_eqn, "is:", intersection_point)
            if intersection_point != False:
                if intersection_point[0] < point[0]:
                    # Intersection point x value is less than point x value.
                    if (intersection_point not in intersection_points_left) and check_in_bounds(intersection_point, line_index) == True:
                        intersection_points_left.append(intersection_point)
                else:
                    # Intersection point x value is greater than point x value.
                    if (intersection_point not in intersection_points_right) and check_in_bounds(intersection_point, line_index) == True:
                        intersection_points_right.append(intersection_point)

        # Check if the number of intersections to the left and right are odd.
        if len(intersection_points_left) > 0 and len(intersection_points_right) > 0:
            if debug == True:
                print("\n")
                print((str(len(intersection_points_left))), "intersection points to the left.")
                print((str(len(intersection_points_right))), "intersection points to the right.")
            if ((len(intersection_points_left) % 2) == 1) and ((len(intersection_points_right) % 2) == 1):
                # Both have odd intersection counts, so the point is in the Fence.
                return(True)
            else:
                print(intersection_points_left, intersection_points_right)
                return(False)
        else:
            print(intersection_points_left, intersection_points_right)
            return(False)

def convertDMSToDD(degrees, minutes, seconds):
    return(degrees + (minutes / 60) + (seconds / 3600))
