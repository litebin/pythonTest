import unittest


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")

    def setUp(self) -> None:
        print("setUp")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def tearDown(self) -> None:
        print("tearDown")

    def test_sum(self):
        x = 1 + 2
        # print(x)
        self.assertEqual(3, x)


if __name__ == '__main__':
    unittest.main()
