import re
from shapely import Polygon, LineString, Point, union_all, intersection

file_path = "Day15Input.txt"
file = open(file_path)
sensors_and_beacons = re.findall("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)\n", file.read())
file.close()
sensors = [Point(int(x[0]), int(x[1])) for x in sensors_and_beacons]
beacons = [Point(int(x[2]), int(x[3])) for x in sensors_and_beacons]
no_beacon_polys = []
for i in range(len(sensors_and_beacons)):
    s_x, s_y = sensors[i].coords[0][0], sensors[i].coords[0][1]
    b_x, b_y = beacons[i].coords[0][0], beacons[i].coords[0][1]
    d = abs(s_x - b_x) + abs(s_y - b_y)
    points = [(s_x, s_y - d), (s_x - d, s_y), (s_x, s_y + d), (s_x + d, s_y)]
    no_beacon_polys.append(Polygon(points))
union_no_beacon_polys = union_all(no_beacon_polys)

def find_n_no_beacon(union_no_beacon_polys, beacons, y):
    horizontal_line = LineString([(union_no_beacon_polys.bounds[0], y), (union_no_beacon_polys.bounds[2], y)])
    return (int(intersection(horizontal_line, union_no_beacon_polys).length) + 1 - len([p for p in list(set(beacons)) if p.y == y]))

def find_tuning_freq(distress_beacon):
    exterior_points = distress_beacon.exterior.xy
    return (int(((min(exterior_points[0]) + max(exterior_points[0])) / 2) * 4000000 + ((min(exterior_points[1]) + max(exterior_points[1])) / 2)))

def find_distress_beacon_tuning_freq(union_no_beacon_polys, min_bound, max_bound):
    boundary = Polygon([(min_bound, min_bound), (min_bound, max_bound), (max_bound, max_bound), (max_bound, min_bound)])
    distress_beacon = boundary.difference(union_no_beacon_polys)
    if type(distress_beacon) == Polygon: return find_tuning_freq(distress_beacon)
    else:
        possible_beacon = list(distress_beacon.geoms)
        for p in possible_beacon:
            if p.area == 2: return find_tuning_freq(p)

# puzzle answers
print("puzzle 1 answer =", find_n_no_beacon(union_no_beacon_polys, beacons, 2000000))
print("puzzle 2 answer =", find_distress_beacon_tuning_freq(union_no_beacon_polys, 0, 4000000))