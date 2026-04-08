import sys
import os
import unittest
import time

# python -m unittest test_pythagore.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pythagore import Pythagore
import math

class TestPythagore(unittest.TestCase):

    def setUp(self):
        self.a = 3
        self.b = 4
        self.pythagore = Pythagore()
        self.hypotenuse = self.pythagore.hypotenus(self.a, self.b)

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
        self.assertEqual(self.hypotenuse, 5)
        self.assertAlmostEqual(self.pythagore.hypotenus(5, 12), 13)
        self.assertAlmostEqual(self.pythagore.hypotenus(8, 15), 17)

        # Benchmark
        self.benchmark(self.pythagore.hypotenus, 3, 4)

    # -------------------------
    # Test adjacent side
    # -------------------------
    def test_adjacent_side(self):
        self.assertEqual(
            self.pythagore.adjacent_side(self.hypotenuse, self.a),
            self.b
        )
        self.assertAlmostEqual(self.pythagore.adjacent_side(13, 5), 12)
        self.assertAlmostEqual(self.pythagore.adjacent_side(17, 8), 15)

        # benchmark
        self.benchmark(self.pythagore.adjacent_side, 5, 3)

    # -------------------------
    # Test is_rectangle
    # -------------------------
    def test_is_rectangle_true(self):
        self.assertTrue(
            self.pythagore.is_rectangle(self.hypotenuse, self.a, self.b)
        )
        self.assertTrue(self.pythagore.is_rectangle(13, 5, 12))
        self.assertTrue(self.pythagore.is_rectangle(17, 8, 15))

        # benchmark
        self.benchmark(self.pythagore.is_rectangle, 5, 3, 4)

    def test_is_rectangle_false(self):
        self.assertFalse(self.pythagore.is_rectangle(10, 3, 4))
        self.assertFalse(self.pythagore.is_rectangle(5, 5, 5))

    # -------------------------
    # Test float precision
    # -------------------------
    def test_float_precision(self):
        a = math.sqrt(2)
        b = math.sqrt(2)
        c = 2

        self.assertTrue(self.pythagore.is_rectangle(c, a, b))



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)