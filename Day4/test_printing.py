import unittest

from printing import get_count, is_accessable


class TestPrinting(unittest.TestCase):
    def testIsAccessable(self):
        grid = [
            "...",
            ".@.",
            "...",
        ]

        self.assertEqual(True, is_accessable(grid, 1, 1))

    def testIsNotAccessable(self):
        grid = [
            "@@@",
            "@@@",
            "@@@",
        ]

        self.assertEqual(False, is_accessable(grid, 1, 1))
        self.assertEqual(False, is_accessable(grid, 1, 2))
        self.assertEqual(True, is_accessable(grid, 0, 0))

    def testGetCount(self):
        grid = [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]

        self.assertEqual(13, get_count(grid))


if __name__ == "__main__":
    unittest.main()
