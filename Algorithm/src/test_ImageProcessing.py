import unittest
import ImageProcessing as ip

COLOR_IMAGE_PATH = '../../SIDBA/Color/Lenna.bmp'
COLOR_IMAGE_HEIGHT = 256
COLOR_IMAGE_WIDTH = 256
GRAYSCALE_IMAGE_PATH = '../../SIDBA/Mono/LENNA.bmp'
GRAYSCALE_IMAGE_HEIGHT = 256
GRAYSCALE_IMAGE_WIDTH = 256

class TestImage_init(unittest.TestCase):
    """Tests Image.__init__
    """

    def testNoArgument(self):
        image = ip.Image()

        self.assertEqual(None, image._image)
        self.assertEqual('', image._image_path)
        self.assertEqual(0, image._height)
        self.assertEqual(0, image._width)

    def testColorImage(self):
        image = ip.Image(COLOR_IMAGE_PATH)

        self.assertIsNotNone(image._image)
        self.assertEqual(COLOR_IMAGE_PATH, image._image_path)
        self.assertEqual(COLOR_IMAGE_HEIGHT, image._height)
        self.assertEqual(COLOR_IMAGE_WIDTH, image._width)

    def testGrayscaleImage(self):
        image = ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)

        self.assertIsNotNone(image._image)
        self.assertEqual(GRAYSCALE_IMAGE_PATH, image._image_path)
        self.assertEqual(GRAYSCALE_IMAGE_HEIGHT, image._height)
        self.assertEqual(GRAYSCALE_IMAGE_WIDTH, image._width)

class TestImage_getitem_setitem(unittest.TestCase):
    """Tests Image.__getitem__, __setitem__
    """

    def testColorImage(self):
        image = ip.Image(COLOR_IMAGE_PATH)
        image[0, 0, 0] = 99
        image[0, 0, 1] = 98
        image[0, 0, 2] = 97

        self.assertEqual(99, image[0, 0, 0])
        self.assertEqual(98, image[0, 0, 1])
        self.assertEqual(97, image[0, 0, 2])

    def testGrayscaleImage(self):
        image = ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        image[0, 0] = 99

        self.assertEqual(99, image[0, 0])

class TestImage_open(unittest.TestCase):
    """Tests Image.open
    """

    def testColorImage(self):
        image = ip.Image()

        image.open(COLOR_IMAGE_PATH)

        self.assertIsNotNone(image._image)
        self.assertEqual(COLOR_IMAGE_PATH, image._image_path)
        self.assertEqual(COLOR_IMAGE_HEIGHT, image._height)
        self.assertEqual(COLOR_IMAGE_WIDTH, image._width)

    def testGrayscaleImage(self):
        image = ip.Image()

        image.open(GRAYSCALE_IMAGE_PATH, grayscale=True)

        self.assertIsNotNone(image._image)
        self.assertEqual(GRAYSCALE_IMAGE_PATH, image._image_path)
        self.assertEqual(GRAYSCALE_IMAGE_HEIGHT, image._height)
        self.assertEqual(GRAYSCALE_IMAGE_WIDTH, image._width)
