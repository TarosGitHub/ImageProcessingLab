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

class TestGradientDifferenceEdgeDetector_init(unittest.TestCase):
    """Tests GradientDifferenceEdgeDetector.__init__
    """

    def testNormal(self):
        edge_detector = ed.GradientDifferenceEdgeDetector()

        self.assertEqual(edge_detector._difference_d_ope_x, edge_detector._d_ope_x)
        self.assertEqual(edge_detector._difference_d_ope_y, edge_detector._d_ope_y)
        self.assertEqual(4.0, edge_detector._amplifier)

class TestGradientDifferenceEdgeDetector_detect(unittest.TestCase):
    """Tests GradientDifferenceEdgeDetector.detect
    """

    def setUp(self):
        if not os.path.exists(IMG_DIR):
            os.mkdir(IMG_DIR)

    def testNormal(self):
        image =  ip.Image(GRAYSCALE_IMAGE_PATH, grayscale=True)
        edge_detector = ed.GradientDifferenceEdgeDetector()

        output_image = edge_detector.detect(image)

        output_image.save(IMG_DIR + '/TestGradientDifferenceEdgeDetector_detect_testNormal.bmp')
