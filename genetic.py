__author__ = 'yexl'

import random
import util
import datetime

g_count = 0
g_city_number = 24
population_size = 100

class Genetic:
    mutationRate = 0

    def __init__(self):
        self.mutationRate = 10

    def selection(self, pop):
        select_size = 10
        popTemp = Population(select_size, True)

        for i in range(select_size):
            var = random.randint(0, select_size - 1)
            popTemp.tours[i] = pop.tours[var]
        fittest = popTemp.getFittest()
        return fittest

    def crossover(self, parent1, parent2):
        child = Tour()

        start = random.randint(0, len(parent1.tour) - 1)
        end = random.randint(0, len(parent1.tour) - 1)

        for i in range(len(child.tour)):
            if start < end and i > start and i < end:
                child.set_city(i, parent1.get_city(i))
            elif start > end:
                if not (i < start and i > end):
                    child.set_city(i, parent1.get_city(i))

        for i in range(len(parent2.tour)):
            if not child.contain_city(parent2.get_city(i)):
                for j in range(len(parent2.tour)):
                    if child.get_city(j) == None:
                        child.set_city(j, parent2.get_city(i))
                        break

        return child;

    def mutation(self, candidate):
        for i in range(len(candidate.tour)):
            if random.randint(1, 100) < self.mutationRate:
                j = random.randint(0, g_city_number - 1)

                c1 = candidate.get_city(i)
                c2 = candidate.get_city(j)

                candidate.set_city(j, c1)
                candidate.set_city(i, c2)
        return candidate


    def evolve(self, pop):
        newPop = Population(population_size, True)

        elitism = True
        offset = 0

        if elitism:
            newPop.tours[0] = pop.getFittest()
            offset = 1

        count = 0
        for i in range(offset, newPop.size):
            parent1 = self.selection(pop)
            parent2 = self.selection(pop)

            child = self.crossover(parent1, parent2)

            newPop.tours[i] = child

        for i in range(offset, newPop.size):
            newPop.tours[i] = self.mutation(newPop.tours[i])

        return newPop;


class Tour:
    '''a single tour to travel around all cities'''
    tour = []
    fitness = 0;
    distance = 0;

    def __init__(self):
        self.tour = []
        for i in range(g_city_number):
            self.tour.append(None)

    def shuffle_tour(self):
        self.tour = range(g_city_number)
        random.shuffle(self.tour)

    def get_city(self, pos):
        return self.tour[pos]

    def set_city(self, pos, city):
        self.tour[pos] = city
        fitness = 0;
        distance = 0;

    def get_fitness(self):
        if self.fitness == 0:
            global g_count
            g_count += 1
            self.fitness = 1/self.get_distance()
        return self.fitness

    def get_distance(self):
        return util.get_path_distance(self.tour, util.read_file())

    def contain_city(self, city):
        if city in self.tour:
            return True
        else:
            return False


class Population:
    tours = []
    size = 0

    def __init__(self, size, init):
        self.size = size
        if init:
            self.tours = []
            for i in range(size):
                newTour = Tour()
                newTour.shuffle_tour()
                self.tours.append(newTour)

    def getFittest(self):
        fittest = self.tours[0];
        for i in range(self.size):
            if self.tours[i].get_fitness() > fittest.get_fitness():
                fittest = self.tours[i]
        return fittest

def geneticmain():
    pop = Population(population_size, True)
    #print "init best distance", pop.getFittest().get_distance()
    for i in range(1,50):
        gene = Genetic()
        pop = gene.evolve(pop)
        #print "tourment", i, "distance", pop.getFittest().get_distance(), " tour",  pop.getFittest().tour

    return pop.getFittest().tour, pop.getFittest().get_distance()

'''
listresult = []
mindis = 100000
mintour = []
maxdis = 0;
maxtour = []
for i in range(20):
    start_time = datetime.datetime.now()
    tour, length = geneticmain()
    end_time = datetime.datetime.now()
    print "runing time", (end_time - start_time).seconds, " seconds"
    if length < mindis:
        mintour = tour
        mindis = length
    if length > maxdis:
        maxtour = tour
        maxdis = length

    listresult.append(length)
    print i

print "count", g_count
print "---------------------------------------------------------------------------------"
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