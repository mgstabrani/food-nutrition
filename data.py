import csv

def load_age_nutrition(path="age-nutrition.csv"):
    age_nutrition = []
    with open(path, "r") as age_file:
        age_reader = csv.reader(age_file)
        for row in age_reader:
            age_nutrition.append([row[0], float(row[1])])
    return age_nutrition


def load_food(path="food.csv"):
    food = []
    with open(path, "r") as food_file:
        food_reader = csv.reader(food_file)
        for row in food_reader:
            food.append([row[0], float(row[1]), float(row[2])])
    return food


def choose_user_input(age_nutrition):
    for i in range(len(age_nutrition)):
        print(str(i + 1) + ". " + age_nutrition[i][0])

    kategori = 0
    while kategori < 1 or kategori > len(age_nutrition):
        kategori = int(input("Pilih kategori usia: "))

    budget = 0
    while budget <= 0:
        budget = int(input("Jumlah budget: "))

    prioritas = 2
    return kategori, budget, prioritas


def prepare_food_with_ratio(food, prioritas):
    prepared_food = []
    for item in food:
        current = item[:]
        if prioritas == 1:
            current.append(current[1] / current[2])
        else:
            current.append(current[2] / current[1])
        prepared_food.append(current)
    prepared_food.sort(key=lambda elem: elem[3])
    return prepared_food