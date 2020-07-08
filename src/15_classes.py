# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class Latlon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(Latlon):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super(Waypoint, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{self.name}, {self.lat}, {self.lon}".format(self=self)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, difficulty, size, *args, **kwargs):
        self.difficulty = difficulty
        self.size = size
        super(Geocache, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}".format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
#>>>>>>>  NEED TO CONVERT OBJ TO STR ^19

print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
#>>>>>>>> ^32
print(geocache)
