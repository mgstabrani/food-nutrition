from branchbound import find_solution
from data import choose_user_input, load_age_nutrition, load_food, prepare_food_with_ratio


def run():
    age_nutrition = load_age_nutrition()
    food = load_food()

    kategori, budget, prioritas = choose_user_input(age_nutrition)

    if prioritas == 1:
        upper_bound = budget
        profit = age_nutrition[kategori - 1][1]
    else:
        upper_bound = age_nutrition[kategori - 1][1]
        profit = budget

    prepared_food = prepare_food_with_ratio(food, prioritas)
    solusi = find_solution(upper_bound, profit, prepared_food, prioritas)

    uang_used = 0
    kalori = 0
    for i in range(len(solusi)):
        if(solusi[i] == 1):
            uang_used += prepared_food[i][2]
            kalori += prepared_food[i][1]

    print("Total uang yang digunakan: Rp.", int(uang_used))
    print("Total kalori yang didapatkan:", kalori, "kkal")
    print("Kalori per hari yang dibutuhkan:", age_nutrition[kategori - 1][1], "kkal")
    print("Makanan yang didapatkan: ")
    j = 1
    for i in range(len(solusi)):
        if(solusi[i] == 1):
            print(str(j) + ". " + prepared_food[i][0])
            j += 1


if __name__ == "__main__":
    run()