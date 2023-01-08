import unittest
from visu.package.executor.segmentation import Segmentation

class TestSegmentation(unittest.TestCase):
    def test_segmentation(self):
        data = {}
        self.assertEqual(Segmentation(data), False)


if __name__ == '__main__':
    unittest.main()