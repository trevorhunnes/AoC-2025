import unittest

from lobby import get_jolts, get_next_biggest


class TestLobby(unittest.TestCase):
    def test_get_next_biggest(self):
        bank = "9876543211111111111111111111111111111111111111"
        self.assertEqual((1, "9"), get_next_biggest(0, bank, 0))
        self.assertEqual((2, "8"), get_next_biggest(1, bank, 1))
        self.assertEqual((12, "1"), get_next_biggest(11, bank, 11))

    def test_biggest_end(self):
        bank = "1111111111111111111111111111111111111123456789"
        self.assertEqual((39, "2"), get_next_biggest(4, bank, 4))
        self.assertEqual((40, "3"), get_next_biggest(39, bank, 5))

    def test_get_jolts(self):
        bank = "9876543211111111111111111111111111111111111111"
        self.assertEqual(987654321111, get_jolts(bank))


if __name__ == "__main__":
    unittest.main()
