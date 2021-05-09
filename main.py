from data import *
from branchbound import *

#Get solution
solusi = findSolution(upperBound)

#Get money used and calory
uangUsed = 0
kalori = 0
for i in range(len(solusi)):
    if(solusi[i] == 1):
        uangUsed += food[i][2]
        kalori += food[i][1]

#Print output
print("Total uang yang digunakan: Rp.",int(uangUsed))
print("Total kalori yang didapatkan:",kalori, "kkal")
print("Kalori per hari yang dibutuhkan:", age_nutrition[kategori-1][1], "kkal")
print("Makanan yang didapatkan: ")
j = 1
for i in range(len(solusi)-1):
    if(solusi[i] == 1):
        print(str(j) + ". " + food[i][0])
        j += 1