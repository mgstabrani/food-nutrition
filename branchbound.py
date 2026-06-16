def copy_array(array):
    return array[:]


def simpul_bobot(simpul, food, prioritas):
    bobot = 0
    for i in range(len(simpul)):
        if(simpul[i] == 1):
            if(prioritas == 1):
                bobot += food[i][2]
            else:
                bobot += food[i][1]
    return bobot


def profit_simpul(simpul, food, prioritas):
    profit = 0
    for i in range(len(simpul)):
        if(simpul[i] == 1):
            if(prioritas == 1):
                profit += food[i][1]
            else:
                profit += food[i][2]
    return profit


def simpul_weight(simpul, food, prioritas, upper_bound):
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
        total += (upper_bound-bobot)*food[(len(simpul))][3]
    return total


def find_max(simpul_hidup, food, prioritas, upper_bound):
    max_weight = simpul_weight(simpul_hidup[0], food, prioritas, upper_bound)
    max_index = 0
    if(prioritas == 1):
        for i in range(1,len(simpul_hidup)):
            if(max_weight < simpul_weight(simpul_hidup[i], food, prioritas, upper_bound)):
                max_weight = simpul_weight(simpul_hidup[i], food, prioritas, upper_bound)
                max_index = i
    else:
        for i in range(1,len(simpul_hidup)):
            if(max_weight > simpul_weight(simpul_hidup[i], food, prioritas, upper_bound)):
                max_weight = simpul_weight(simpul_hidup[i], food, prioritas, upper_bound)
                max_index = i
    return max_index


def find_solution(upper_bound, profit, food, prioritas):
    simpul_hidup = [[0]]
    if(simpul_bobot([1], food, prioritas) <= upper_bound and profit_simpul([1], food, prioritas) <= profit):
        simpul_hidup.append([1])
    solutionFound = False
    while(solutionFound == False):
        index = find_max(simpul_hidup, food, prioritas, upper_bound)
        simpul_expand = simpul_hidup[index]
        if(len(simpul_expand) == len(food)):
            solutionFound = True
        else:
            a = copy_array(simpul_expand)
            b = copy_array(simpul_expand)
            a.append(1)
            b.append(0)
            if(simpul_bobot(a, food, prioritas) <= upper_bound and profit_simpul(a, food, prioritas) <= profit):
                simpul_hidup.append(a)
            simpul_hidup.append(b)
            simpul_hidup.pop(index)
    return simpul_expand