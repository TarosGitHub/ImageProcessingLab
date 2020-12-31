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
