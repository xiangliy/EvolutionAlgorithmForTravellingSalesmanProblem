__author__ = 'yexl'
import random
import util
g_city_number = 24;


def generate_pair(length):
    x = range(length)
    random.shuffle(x)

    y = range(length)
    random.shuffle(y)

    for i in x:
        for j in y:
            yield (i,j)


def swap_cities(tour):
    for i, j in generate_pair(len(tour)):
        if i < j:
            copy=tour[:]
            copy[i] = tour[j]
            copy[j] = tour[i]
            yield copy


def hill_climb(init_tour):
    cur_iterator = 0
    max_iterator = 100
    min_distance = 100000;

    best_tour = init_tour

    while cur_iterator < max_iterator:
        flag = False
        for newtour in swap_cities(init_tour):
            if cur_iterator > max_iterator:
                break
            cur_iterator += 1
            distance = util.get_path_distance(newtour, util.read_file())
            if distance < min_distance:
                best_tour = newtour
                min_distance = distance
                flag = True
                break
        if flag == False:
            break

        #print best_tour
        #print min_distance
        #print cur_iterator

    return best_tour, min_distance


def hillclimbmain():
    init_tour = range(g_city_number)
    random.shuffle(init_tour)
    distance_table = util.read_file()
    best_tour, min_distance = hill_climb(init_tour)

    for i in range(10):
        #print i, "----------------------------------"
        tour, distance = hill_climb(init_tour)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    #print "best tour", best_tour
    #print "min distance", min_distance

    return tour,min_distance

'''
listresult = []
mindis = 100000
mintour = []
maxdis = 0;
maxtour = []
for i in range(20):
    tour, length = hillclimbmain()
    if length < mindis:
        mintour = tour
        mindis = length
    if length > maxdis:
        maxtour = tour
        maxdis = length

    listresult.append(length)

print "min tour", mintour
print "min citylist", util.read_cityname_list(mintour)
print "min length", mindis
print "max tour", maxtour
print "max citylist", util.read_cityname_list(maxtour)
print "max length", maxdis
print "tour", i, "length ", length
print "average length ", util.get_average(listresult)
print "deviation ", util.get_deviation(listresult, util.get_average(listresult))
'''