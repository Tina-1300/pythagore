import sys
import os
import unittest
import time

# python -m unittest test_pythagore.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pythagore import (
    hypotenuse,
    adjacent_side,
    is_rectangle,
    current_version,
    creator
)
import math

class TestPythagore(unittest.TestCase):

    def setUp(self):
        self.a = 3
        self.b = 4
        self.h = hypotenuse(self.a, self.b)

    # -------------------------
    # Benchmark helper
    # -------------------------
    def benchmark(self, func, *args, repeats=100000):
        start = time.perf_counter()
        for _ in range(repeats):
            func(*args)
        end = time.perf_counter()
        print(f"Benchmark {func.__name__}: {(end - start):.6f} sec for {repeats} runs")


    # -------------------------
    # Test hypotenuse
    # -------------------------
    def test_hypotenuse(self):
        self.assertEqual(self.h, 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

        self.benchmark(hypotenuse, 3, 4)

    # -------------------------
    # Test adjacent side
    # -------------------------
    def test_adjacent_side(self):
        self.assertEqual(
            adjacent_side(self.h, self.a),
            self.b
        )

        self.assertAlmostEqual(adjacent_side(13, 5), 12)
        self.assertAlmostEqual(adjacent_side(17, 8), 15)

        self.benchmark(adjacent_side, 5, 3)

    # -------------------------
    # Test is_rectangle
    # -------------------------
    def test_is_rectangle_true(self):
        self.assertTrue(is_rectangle(self.h, self.a, self.b))
        self.assertTrue(is_rectangle(13, 5, 12))
        self.assertTrue(is_rectangle(17, 8, 15))

        self.benchmark(is_rectangle, 5, 3, 4)

    def test_is_rectangle_false(self):
        self.assertFalse(is_rectangle(10, 3, 4))
        self.assertFalse(is_rectangle(5, 5, 5))

    # -------------------------
    # Test float precision
    # -------------------------
    def test_float_precision(self):
        a = math.sqrt(2)
        b = math.sqrt(2)
        c = 2

        self.assertTrue(is_rectangle(c, a, b))

    def test_metadata(self):
        self.assertEqual(current_version(), "1.5.0")
        self.assertIn("Tina", creator())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)