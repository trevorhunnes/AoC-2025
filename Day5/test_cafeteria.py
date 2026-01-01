import unittest

from cafeteria import get_count, get_ranges, split_database


class TestCafeteria(unittest.TestCase):
    def testSplitDatabase(self):
        database = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
        self.assertEqual(
            (["3-5", "10-14", "16-20", "12-18"], ["1", "5", "8", "11", "17", "32"]),
            split_database(database),
        )

    def testGetRanges(self):
        ranges = ["3-5", "10-14", "16-20", "12-18"]
        self.assertEqual(
            {3, 4, 5, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 15}, get_ranges(ranges)
        )

    def testGetCount(self):
        range_set = {3, 4, 5, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 15}
        ingredient_ids = ["1", "5", "8", "11", "17", "32"]
        self.assertEqual(3, get_count(range_set, ingredient_ids))


if __name__ == "__main__":
    unittest.main()
