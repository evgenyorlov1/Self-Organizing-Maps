import csv
import random
import math


def main():
    data = load_data()
    matrix = weight_matrix(4,3)
    i=0
    for row in data:
        print "{} row".format(row)
        print "i: ", i
        print "{} weight".format(matrix[i][:-1])
        print "{} pattern".format(data[0])
        #bmu = euclidian_distance(matrix[i][:-1], row)
        i+=1


def load_data():
    result = list()
    with open('iris.csv', 'r') as file:
        data = csv.reader(file, delimiter=',')
        for row in list(data):
            row = [float(i) for i in row]
            result.append(row)
        return result


def weight_matrix(columns, rows):
    #last column for BMU
    matrix = list()
    for i in xrange(rows):
        row = list()
        for j in xrange(columns):
            row.append(random.random())
        row.append(0)
        matrix.append(row)
    return matrix


def euclidian_distance(weight, pattern):
    sum = 0
    for i in xrange(len(weight)):
        sum += math.pow(pattern[i] - weight[i],2)
    return math.sqrt(sum)


#hard lim
def activation_functio(value):
    if value >= 0:
        return 1
    else:
        return 0


def update_weight():
    pass

if __name__ == "__main__":
    main()