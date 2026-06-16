import csv
import os
import tempfile
import unittest

from data import load_age_nutrition, load_food, prepare_food_with_ratio


def _write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


class TestLoadAgeNutrition(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.path = os.path.join(self.tmpdir, "age.csv")
        _write_csv(self.path, [["1-3 tahun", "1350"], ["4-6 tahun", "1400"]])

    def test_returns_list_of_rows(self):
        result = load_age_nutrition(self.path)
        self.assertEqual(len(result), 2)

    def test_name_is_string(self):
        result = load_age_nutrition(self.path)
        self.assertIsInstance(result[0][0], str)
        self.assertEqual(result[0][0], "1-3 tahun")

    def test_calory_is_float(self):
        result = load_age_nutrition(self.path)
        self.assertIsInstance(result[0][1], float)
        self.assertEqual(result[0][1], 1350.0)


class TestLoadFood(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.path = os.path.join(self.tmpdir, "food.csv")
        _write_csv(self.path, [["Ayam segar", "75", "30000"], ["Bayam", "16", "3500"]])

    def test_returns_list_of_rows(self):
        result = load_food(self.path)
        self.assertEqual(len(result), 2)

    def test_name_is_string(self):
        result = load_food(self.path)
        self.assertEqual(result[0][0], "Ayam segar")

    def test_calory_and_price_are_float(self):
        result = load_food(self.path)
        self.assertIsInstance(result[0][1], float)
        self.assertIsInstance(result[0][2], float)
        self.assertEqual(result[0][1], 75.0)
        self.assertEqual(result[0][2], 30000.0)


class TestPrepareFoodWithRatio(unittest.TestCase):
    def setUp(self):
        self.food = [
            ["Food A", 100.0, 5000.0],
            ["Food B", 200.0, 6000.0],
            ["Food C", 50.0, 4000.0],
        ]

    def test_appends_ratio_column(self):
        result = prepare_food_with_ratio(self.food, prioritas=2)
        self.assertEqual(len(result[0]), 4)

    def test_ratio_prioritas_2_is_price_over_calory(self):
        result = prepare_food_with_ratio(self.food, prioritas=2)
        for item in result:
            self.assertAlmostEqual(item[3], item[2] / item[1])

    def test_ratio_prioritas_1_is_calory_over_price(self):
        result = prepare_food_with_ratio(self.food, prioritas=1)
        for item in result:
            self.assertAlmostEqual(item[3], item[1] / item[2])

    def test_sorted_ascending_by_ratio(self):
        result = prepare_food_with_ratio(self.food, prioritas=2)
        ratios = [item[3] for item in result]
        self.assertEqual(ratios, sorted(ratios))

    def test_does_not_mutate_original(self):
        original_len = len(self.food[0])
        prepare_food_with_ratio(self.food, prioritas=2)
        self.assertEqual(len(self.food[0]), original_len)


if __name__ == "__main__":
    unittest.main()
