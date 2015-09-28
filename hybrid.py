__author__ = 'yexl'
import hillclimb
import genetic

import random
import util
g_city_number = 24
population_size = 100
lamarckian = True
baldwinian = False

class Genetic:
    mutationRate = 0

    def __init__(self):
        self.mutationRate = 10

    def selection(self, pop):
        select_size = 10
        popTemp = genetic.Population(select_size, True)

        for i in range(select_size):
            var = random.randint(0, select_size - 1)
            popTemp.tours[i] = pop.tours[var]
        fittest = popTemp.getFittest();
        return fittest

    def crossover(self, parent1, parent2):
        child = genetic.Tour()

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
        newPop = genetic.Population(population_size, True)

        elitism = True
        offset = 0

        if elitism:
            newPop.tours[0] = pop.getFittest()
            offset = 1

        for i in range(offset, newPop.size):
            parent1 = self.selection(pop)
            parent2 = self.selection(pop)

            child = self.crossover(parent1, parent2)

            newPop.tours[i] = child

        for i in range(offset, newPop.size):
            newPop.tours[i] = self.mutation(newPop.tours[i])

        #Lamarckian
        if lamarckian:
            for i in range(offset, newPop.size):
                tour, distance = hillclimb.hill_climb(newPop.tours[i].tour)
                if distance < newPop.tours[i].get_distance():
                    newPop.tours[i].tour = tour

        #baldwinian
        if baldwinian:
            for i in range(offset, newPop.size):
                tour, distance = hillclimb.hill_climb(newPop.tours[i].tour)
                if distance < newPop.tours[i].get_distance():
                    fitness = 1/distance
                    newPop.tours[i].fitness = fitness

        return newPop;


def hybridmain():
    pop = genetic.Population(population_size, True)
    #print "init best distance", pop.getFittest().get_distance()
    for i in range(1,30):
        gene = Genetic()
        pop = gene.evolve(pop)
        #print "tourment", i, "distance", pop.getFittest().get_distance(), " tour",  pop.getFittest().tour
    return  pop.getFittest().tour, pop.getFittest().get_distance()

listresult = []
mindis = 100000
mintour = []
maxdis = 0;
maxtour = []
for i in range(10):
    print i
    tour, length = hybridmain()
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
print listresult
print "deviation ", util.get_deviation(listresult, util.get_average(listresult))


