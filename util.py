__author__ = 'yexl'
import csv


def read_cityname_list(listnum):
    # Read data file
    with open('european_cities.csv') as file:
      reader = csv.reader(file,delimiter=';')
      # First row is the city names
      city_names = reader.next()

    list_city_name = []
    for i in listnum:
        list_city_name.append(city_names[i])
    # List the city names
    return list_city_name


def read_file():
    # Read data file
    distance_table = []
    with open('european_cities.csv') as file:
        reader = csv.reader(file,delimiter=';')
        # First row is the city names
        city_names = reader.next()
        # The rest of the rows are the distance table
        for row in reader:
            distance_table.append([float(cell) for cell in row])

    return distance_table


def get_path_distance(path, distance_table):
    distance = 0.0;
    index = 0;
    for city in path:
        begin = city;

        if index == len(path) - 1:
            end = path[0]
        else:
            end = path[index + 1];
        distance += distance_table[begin][end]
        index += 1
    return distance


def get_average(listdata):
    total = 0;
    for i in range(len(listdata)):
        total += listdata[i]

    return total/len(listdata)

def get_deviation(listdata, average):
    deviation = 0;
    for i in range(len(listdata)):
        if average > listdata[i]:
            deviation += average - listdata[i]
        else:
            deviation += listdata[i] - average

    return deviation
