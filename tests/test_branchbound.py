import unittest

from branchbound import (
    copy_array,
    find_max,
    find_solution,
    profit_simpul,
    simpul_bobot,
    simpul_weight,
)

FOOD = [
    ["Food A", 100.0, 3000.0, 30.0],
    ["Food B", 200.0, 5000.0, 25.0],
    ["Food C", 150.0, 6000.0, 40.0],
]


class TestCopyArray(unittest.TestCase):
    def test_returns_equal_contents(self):
        original = [1, 0, 1]
        result = copy_array(original)
        self.assertEqual(result, original)

    def test_returns_independent_copy(self):
        original = [1, 0]
        result = copy_array(original)
        result.append(1)
        self.assertEqual(len(original), 2)


class TestSimpulBobot(unittest.TestCase):
    def test_prioritas_2_sums_calories_of_selected(self):
        simpul = [1, 0, 1]
        result = simpul_bobot(simpul, FOOD, prioritas=2)
        self.assertEqual(result, 100.0 + 150.0)

    def test_prioritas_1_sums_prices_of_selected(self):
        simpul = [1, 1, 0]
        result = simpul_bobot(simpul, FOOD, prioritas=1)
        self.assertEqual(result, 3000.0 + 5000.0)

    def test_empty_selection_returns_zero(self):
        simpul = [0, 0, 0]
        self.assertEqual(simpul_bobot(simpul, FOOD, prioritas=2), 0)


class TestProfitSimpul(unittest.TestCase):
    def test_prioritas_2_sums_prices_of_selected(self):
        simpul = [1, 0, 0]
        result = profit_simpul(simpul, FOOD, prioritas=2)
        self.assertEqual(result, 3000.0)

    def test_prioritas_1_sums_calories_of_selected(self):
        simpul = [0, 1, 0]
        result = profit_simpul(simpul, FOOD, prioritas=1)
        self.assertEqual(result, 200.0)

    def test_empty_selection_returns_zero(self):
        simpul = [0, 0, 0]
        self.assertEqual(profit_simpul(simpul, FOOD, prioritas=2), 0)


class TestSimpulWeight(unittest.TestCase):
    def test_full_simpul_no_fractional_extension(self):
        simpul = [1, 0, 1]
        result = simpul_weight(simpul, FOOD, prioritas=2, upper_bound=500.0)
        self.assertEqual(result, 3000.0 + 6000.0)

    def test_partial_simpul_extends_with_fractional(self):
        simpul = [1]
        result = simpul_weight(simpul, FOOD, prioritas=2, upper_bound=300.0)
        remaining = (300.0 - 100.0) * FOOD[1][3]
        expected = 3000.0 + remaining
        self.assertAlmostEqual(result, expected)


class TestFindSolution(unittest.TestCase):
    def setUp(self):
        self.food = [
            ["Rice", 355.0, 12000.0, 33.80],
            ["Corn", 129.0, 8000.0, 62.01],
            ["Chicken", 75.0, 30000.0, 400.0],
        ]

    def test_returns_list_same_length_as_food(self):
        result = find_solution(
            upper_bound=800.0, profit=50000.0, food=self.food, prioritas=2
        )
        self.assertEqual(len(result), len(self.food))

    def test_each_element_is_0_or_1(self):
        result = find_solution(
            upper_bound=800.0, profit=50000.0, food=self.food, prioritas=2
        )
        for val in result:
            self.assertIn(val, (0, 1))

    def test_selected_calories_do_not_exceed_upper_bound(self):
        upper_bound = 500.0
        result = find_solution(
            upper_bound=upper_bound, profit=50000.0, food=self.food, prioritas=2
        )
        total_calories = sum(
            self.food[i][1] for i in range(len(result)) if result[i] == 1
        )
        self.assertLessEqual(total_calories, upper_bound)

    def test_selected_price_does_not_exceed_profit_budget(self):
        profit = 20000.0
        result = find_solution(
            upper_bound=800.0, profit=profit, food=self.food, prioritas=2
        )
        total_price = sum(
            self.food[i][2] for i in range(len(result)) if result[i] == 1
        )
        self.assertLessEqual(total_price, profit)

    def test_zero_budget_selects_nothing(self):
        result = find_solution(
            upper_bound=800.0, profit=0.0, food=self.food, prioritas=2
        )
        self.assertEqual(sum(result), 0)


if __name__ == "__main__":
    unittest.main()
