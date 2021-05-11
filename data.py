import csv

#Read age-nutrition.csv
ageFile = open("age-nutrition.csv","r")
ageFile = csv.reader(ageFile)
age_nutrition = []
index = 0
for row in ageFile:        
    age_nutrition.append(row)
    age_nutrition[index][1] = float(age_nutrition[index][1])
    index += 1

#Read food.csv
foodFile = open("food.csv","r")
foodFile = csv.reader(foodFile)
food = []
index = 0
for row in foodFile:        
    food.append(row)
    for i in range(1,3):
        food[index][i] = float(food[index][i])
    index += 1

#User input
for i in range(len(age_nutrition)):
    print(str(i+1) + ". " + age_nutrition[i][0])
kategori = int(input("Pilih kategori usia: "))
budget = int(input("Jumlah budget: "))
# print("1. Kalori")
# print("2. Uang")
# prioritas = int(input("Pilih prioritas: "))
prioritas = 2

#User priority
if(prioritas == 1):
    upperBound = budget
    profit = age_nutrition[kategori-1][1]
    for i in range(len(food)):
        food[i].append(food[i][1]/food[i][2])

elif(prioritas == 2):
    upperBound = age_nutrition[kategori-1][1]
    profit = budget
    for i in range(len(food)):
        food[i].append(food[i][2]/food[i][1])

#Sort food based on pi/wi
def take(elem):
    return elem[3]
food.sort(key=take)