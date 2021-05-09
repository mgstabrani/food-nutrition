from data import *

def copyArray(array):
    newArray = []
    for i in range(len(array)):
        newArray.append(array[i])
    return newArray

def simpulBobot(simpul):
    bobot = 0
    for i in range(len(simpul)):
        if(simpul[i] == 1):
            if(prioritas == 1):
                bobot += food[i][2]
            else:
                bobot += food[i][1]
    return bobot

def profitSimpul(simpul):
    profit = 0
    for i in range(len(simpul)):
        if(simpul[i] == 1):
            if(prioritas == 1):
                profit += food[i][1]
            else:
                profit += food[i][2]
    return profit

def simpulWeight(simpul):
    total = 0
    bobot = 0
    for i in range(len(simpul)):
        if(simpul[i] == 1):
            if(prioritas == 1):
                total += food[i][1]
                bobot += food[i][2]
            else:
                total += food[i][2]
                bobot += food[i][1]
    if(len(simpul) < len(food)):
        total += (upperBound-bobot)*food[(len(simpul))][3]
    return total

def findMax(simpul_hidup):
    max_weight = simpulWeight(simpul_hidup[0])
    max_index = 0
    if(prioritas == 1):
        for i in range(1,len(simpul_hidup)):
            if(max_weight < simpulWeight(simpul_hidup[i])):
                max_weight = simpulWeight(simpul_hidup[i])
                max_index = i
    else:
        for i in range(1,len(simpul_hidup)):
            if(max_weight > simpulWeight(simpul_hidup[i])):
                max_weight = simpulWeight(simpul_hidup[i])
                max_index = i
    return max_index

def findSolution(upperBound):
    simpul_hidup = [[0]]
    if(simpulBobot([1]) <= upperBound and profitSimpul([1]) <= profit):
        simpul_hidup.append([1])
    solutionFound = False
    while(solutionFound == False):
        index = findMax(simpul_hidup)
        simpul_expand = simpul_hidup[index]
        if(len(simpul_expand) == len(food)):
            solutionFound = True
        else:
            a = copyArray(simpul_expand)
            b = copyArray(simpul_expand)
            a.append(1)
            b.append(0)
            if(simpulBobot(a) <= upperBound and profitSimpul(a) <= profit):
                simpul_hidup.append(a)
            simpul_hidup.append(b)
            simpul_hidup.pop(index)
    return simpul_expand