import csv

#Read age-nutrition.csv
ageFile = open("age-nutrition.csv","r")
ageFile = csv.reader(ageFile)
age_nutrition = []
index = 0
for row in ageFile:        
    age_nutrition.append(row)
    for i in range(1,5):
        age_nutrition[index][i] = float(age_nutrition[index][i])
    index += 1

#Read food.csv
foodFile = open("food.csv","r")
foodFile = csv.reader(foodFile)
food = []
index = 0
for row in foodFile:        
    food.append(row)
    for i in range(1,5):
        food[index][i] = float(food[index][i])
    index += 1