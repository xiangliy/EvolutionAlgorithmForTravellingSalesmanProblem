__author__ = 'yexl'

import itertools
import datetime
import util
g_city_number = 10;


def exhaustive_iterator(city_Number, distance_table):
    start_time = datetime.datetime.now()
    min_distance = 100000.0
    index = 0

    for path in list(itertools.permutations(range(city_Number), city_Number)):
        #print(path)
        distance = util.get_path_distance(path, distance_table)

        if distance < min_distance:
            min_distance = distance
            print "new distance", min_distance
            print(path)
            print index

        index += 1

    print min_distance
    print index
    end_time = datetime.datetime.now()
    print "runing time", (end_time - start_time).seconds, " seconds"

exhaustive_iterator(g_city_number, util.read_file())
