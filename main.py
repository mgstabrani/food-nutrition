import argparse

from branchbound import find_solution
from data import choose_user_input, load_age_nutrition, load_food, prepare_food_with_ratio


def build_arg_parser(age_nutrition):
    parser = argparse.ArgumentParser(
        prog="food-nutrition",
        description="Optimize food selection by budget and daily calory need.",
    )
    parser.add_argument(
        "--category", "-c",
        type=int,
        choices=range(1, len(age_nutrition) + 1),
        metavar=f"1-{len(age_nutrition)}",
        help="Age category number (see list below).",
    )
    parser.add_argument(
        "--budget", "-b",
        type=int,
        help="Budget in Rupiah (positive integer).",
    )
    return parser


def run():
    age_nutrition = load_age_nutrition()
    food = load_food()

    parser = build_arg_parser(age_nutrition)
    args = parser.parse_args()

    if args.category is not None and args.budget is not None:
        if args.budget <= 0:
            parser.error("--budget must be a positive integer.")
        kategori, budget, prioritas = args.category, args.budget, 2
    else:
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