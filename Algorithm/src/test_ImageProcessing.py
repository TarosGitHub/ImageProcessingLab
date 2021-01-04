import unittest
import os
import ImageProcessing as ip

IMG_DIR = '../img'
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
        self.assertEqual(0, image._height)
        self.assertEqual(0, image._width)

    def testColorImage(self):
        image = ip.Image(COLOR_IMAGE_PATH)

        self.assertIsNotNone(image._image)
        self.assertEqual(COLOR_IMAGE_HEIGHT, image._height)
        self.assertEqual(COLOR_IMAGE_WIDTH, image._width)

    def testGrayscaleImage(self):
        image = ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)

        self.assertIsNotNone(image._image)
        self.assertEqual(GRAYSCALE_IMAGE_HEIGHT, image._height)
        self.assertEqual(GRAYSCALE_IMAGE_WIDTH, image._width)

    def testWhiteImage(self):
        HEIGHT = 200
        WIDTH = 300
        image = ip.Image(height=HEIGHT, width=WIDTH, grayscale=True)

        self.assertIsNotNone(image._image)
        self.assertEqual(HEIGHT, image._height)
        self.assertEqual(WIDTH, image._width)
        # image.save(IMG_DIR + '/TestImage_init_testWhiteImage.bmp')

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

class TestImage_width(unittest.TestCase):
    """Tests Image.width
    """

    def testGetsWidth(self):
        image = ip.Image(COLOR_IMAGE_PATH)

        self.assertEqual(256, image.width)

class TestImage_height(unittest.TestCase):
    """Tests Image.height
    """

    def testGetsHeight(self):
        image = ip.Image(COLOR_IMAGE_PATH)

        self.assertEqual(256, image.height)

class TestImage_open(unittest.TestCase):
    """Tests Image.open
    """

    def testColorImage(self):
        image = ip.Image()

        image.open(COLOR_IMAGE_PATH)

        self.assertIsNotNone(image._image)
        self.assertEqual(COLOR_IMAGE_HEIGHT, image._height)
        self.assertEqual(COLOR_IMAGE_WIDTH, image._width)

    def testGrayscaleImage(self):
        image = ip.Image()

        image.open(GRAYSCALE_IMAGE_PATH, grayscale=True)

        self.assertIsNotNone(image._image)
        self.assertEqual(GRAYSCALE_IMAGE_HEIGHT, image._height)
        self.assertEqual(GRAYSCALE_IMAGE_WIDTH, image._width)

class TestImage_save(unittest.TestCase):
    """Tests Image.save
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(COLOR_IMAGE_PATH)

        image.save(IMG_DIR + '/TestImage_save_testNormal.bmp')

class TestImage_copy(unittest.TestCase):
    """Tests Image.copy
    """

    def testColorImage(self):
        image = ip.Image(COLOR_IMAGE_PATH)

        copy = image.copy()

        self.assertNotEqual(id(image._image), id(copy._image))
        self.assertEqual(image._height, copy._height)
        self.assertEqual(image._width, copy._width)

    def testGrayscaleImage(self):
        image = ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)

        copy = image.copy()

        self.assertNotEqual(id(image._image), id(copy._image))
        self.assertEqual(image._height, copy._height)
        self.assertEqual(image._width, copy._width)

class TestImage_threshold(unittest.TestCase):
    """Tests Image.threshold
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image = ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)

        output_image = image.threshold(100)

        output_image.save(IMG_DIR + '/TestImage_threshold_testNormal.bmp')
