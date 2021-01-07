import unittest
import os
import ImageProcessing as ip
import ImageProcessingEdgeDetectors as ed

IMG_DIR = '../img'
COLOR_IMAGE_PATH = '../../SIDBA/Color/Lenna.bmp'
COLOR_IMAGE_HEIGHT = 256
COLOR_IMAGE_WIDTH = 256
GRAYSCALE_IMAGE_PATH = '../../SIDBA/Mono/LENNA.bmp'
GRAYSCALE_IMAGE_HEIGHT = 256
GRAYSCALE_IMAGE_WIDTH = 256

class TestDifferenceEdgeDetector_init(unittest.TestCase):
    """Tests DifferenceEdgeDetector.__init__
    """

    def testNormal(self):
        edge_detector = ed.DifferenceEdgeDetector()

        self.assertEqual(edge_detector._difference_ope_x, edge_detector._ope_x)
        self.assertEqual(edge_detector._difference_ope_y, edge_detector._ope_y)
        self.assertEqual(4.0, edge_detector._amplifier)

class TestDifferenceEdgeDetector_detect(unittest.TestCase):
    """Tests DifferenceEdgeDetector.detect
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        edge_detector = ed.DifferenceEdgeDetector()

        output_image = edge_detector.detect(image)

        output_image.save(IMG_DIR + '/TestDifferenceEdgeDetector_detect_testNormal.bmp')

class TestRobertsEdgeDetector_init(unittest.TestCase):
    """Tests RobertsEdgeDetector.__init__
    """

    def testNormal(self):
        edge_detector = ed.RobertsEdgeDetector()

        self.assertEqual(edge_detector._roberts_ope_x, edge_detector._ope_x)
        self.assertEqual(edge_detector._roberts_ope_y, edge_detector._ope_y)
        self.assertEqual(4.0, edge_detector._amplifier)

class TestRobertsEdgeDetector_detect(unittest.TestCase):
    """Tests RobertsEdgeDetector.detect
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        edge_detector = ed.RobertsEdgeDetector()

        output_image = edge_detector.detect(image)

        output_image.save(IMG_DIR + '/TestRobertsEdgeDetector_detect_testNormal.bmp')

class TestSobelEdgeDetector_init(unittest.TestCase):
    """Tests SobelEdgeDetector.__init__
    """

    def testNormal(self):
        edge_detector = ed.SobelEdgeDetector()

        self.assertEqual(edge_detector._sobel_ope_x, edge_detector._ope_x)
        self.assertEqual(edge_detector._sobel_ope_y, edge_detector._ope_y)
        self.assertEqual(4.0, edge_detector._amplifier)

class TestSobelEdgeDetector_detect(unittest.TestCase):
    """Tests SobelEdgeDetector.detect
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        edge_detector = ed.SobelEdgeDetector()

        output_image = edge_detector.detect(image)

        output_image.save(IMG_DIR + '/TestSobelEdgeDetector_detect_testNormal.bmp')

class TestPrewittEdgeDetector_detect(unittest.TestCase):
    """Tests PrewittEdgeDetector.detect
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        edge_detector = ed.PrewittEdgeDetector()

        output_image = edge_detector.detect(image)

        output_image.save(IMG_DIR + '/TestPrewittEdgeDetector_detect_testNormal.bmp')
