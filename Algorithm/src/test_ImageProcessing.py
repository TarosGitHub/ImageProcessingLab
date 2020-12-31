import unittest
import ImageProcessing as ip

class TestImageProcessing_init(unittest.TestCase):

    def test_no_argument(self):
        image = ip.Image()

    def test_path(self):
        path = '../../SIDBA/Color/Lenna.bmp'
        image = ip.Image(path)
        self.assertIsNotNone(image._image)
        self.assertEqual(path, image._image_path)

class TestImageProcessing_getitem(unittest.TestCase):

    def test_normal(self):
        path = '../../SIDBA/Color/Lenna.bmp'
        image = ip.Image(path)
        image[0, 0] = [99, 98, 97]
        self.assertEqual(99, image[0, 0, 0])
        self.assertEqual(98, image[0, 0, 1])
        self.assertEqual(97, image[0, 0, 2])
