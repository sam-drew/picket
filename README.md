# Picket
[![Build status](https://travis-ci.org/sam-drew/picket.svg?master)](https://travis-ci.org/sam-drew)


Picket is a Python library which aims to make geofencing calculations much easier.


The main object defined in Picket is a Fence. A Fence can have points added to it, and as soon as there are >= 3 points, this forms a boundary, and you can calculate if a given (x, y) or (lat, long) point is within this boundary by using Fence.check_point(point).  
The order in which you add points to a Fence object is important; it does not automatically find the nicest, neatest polygon from a set of points.  


Will add some docs on the maths soon, uses Cramers rule to find intersections between lines.
