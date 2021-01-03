from abc import ABCMeta, abstractmethod
import math

class EdgeDetector(metaclass=ABCMeta):
    """The edge detection class.

    This class is implemented with the Strategy pattern.
    """

    @abstractmethod
    def detect(self, image):
        """Detects the edge of the object in the image.

        Args:
            image (ImageProcessing.Image): The input image.

        Returns:
            ImageProcessing.Image: Returns the output image with the edge detected.
        """
        pass

class GradientEdgeDetector(EdgeDetector):
    """The gradient edge detection class.

    Attributes:
        _d_ope_x (list[3, 3]): The derivative operator in the x direction.
        _d_ope_y (list[3, 3]): The derivative operator in the y direction.
        _amplifier (double):　The tone adjustment factor.
    """

    def __init__(self, d_ope_x, d_ope_y, amplifier=4.0):
        """Initializes GradientEdgeDetector class: The GradientEdgeDetector class constructor.

        Args:
            d_ope_x (list[3, 3]): The derivative operator in the x direction.
            d_ope_y (list[3, 3]): The derivative operator in the y direction.
            amplifier (double, optional):　The tone adjustment factor. 0.0 < amplifier.
        """
        self._d_ope_x = d_ope_x
        self._d_ope_y = d_ope_y
        self._amplifier = amplifier

    @property
    def amplifier(self):
        """Gets the amplifier.

        Returns:
            double: Returns the amplifier.
        """
        return self._amplifier

    @amplifier.setter
    def amplifier(self, value):
        """Sets the amplifier.

        Args:
            value (double): The value of the amplifier.
        """
        self._amplifier = value

    def detect(self, image):
        """Detects the edge of the object in the image.

        TODO: グレースケール画像だけでなくRGB画像にも対応したい
        This process can only be done with grayscale images.

        Args:
            image (ImageProcessing.Image): The input image.

        Returns:
            ImageProcessing.Image: Returns the output image with the edge detected.
        """
        MAX_PIXEL_VALUE = 255
        output_image = image.copy()
        output_image[:, :] = MAX_PIXEL_VALUE # TODO: 白画像の生成はImageクラスのコンストラクタでできるようにした方が良い

        for i in range(1, image.height - 1):
            for j in range(1, image.width - 1):
                fx = float(self._d_ope_x[0][0] * image[i - 1, j - 1] + self._d_ope_x[0][1] * image[i - 1, j] + self._d_ope_x[0][2] * image[i - 1, j + 1]
                           + self._d_ope_x[1][0] * image[i, j - 1] + self._d_ope_x[1][1] * image[i, j] + self._d_ope_x[1][2] * image[i, j + 1]
                           + self._d_ope_x[2][0] * image[i + 1, j - 1] + self._d_ope_x[2][1] * image[i + 1, j] + self._d_ope_x[2][2] * image[i + 1, j + 1])
                fy = float(self._d_ope_y[0][0] * image[i - 1, j - 1] + self._d_ope_y[0][1] * image[i - 1, j] + self._d_ope_y[0][2] * image[i - 1, j + 1]
                           + self._d_ope_y[1][0] * image[i, j - 1] + self._d_ope_y[1][1] * image[i, j] + self._d_ope_y[1][2] * image[i, j + 1]
                           + self._d_ope_y[2][0] * image[i + 1, j - 1] + self._d_ope_y[2][1] * image[i + 1, j] + self._d_ope_y[2][2] * image[i + 1, j + 1])
                strength = self._amplifier * math.sqrt(fx * fx + fy * fy)

                pixel_value = int(strength)
                output_image[i, j] = pixel_value if MAX_PIXEL_VALUE < pixel_value else MAX_PIXEL_VALUE

        return output_image

class GradientDifferenceEdgeDetector(GradientEdgeDetector):
    """The gradient difference edge detection class.
    """

    def __init__(self, amplifier=4.0):
        """Initializes GradientDifferenceEdgeDetector class: The GradientDifferenceEdgeDetector class constructor.

        Args:
            amplifier (double, optional):　The tone adjustment factor. 0.0 < amplifier.
        """
        self._difference_d_ope_x = [[0, 0, 0],
                                    [0, -1, 1],
                                    [0, 0, 0]]
        self._difference_d_ope_y = [[0, 0, 0],
                                    [0, -1, 0],
                                    [0, 1, 0]]
        super().__init__(self._difference_d_ope_x, self._difference_d_ope_y, amplifier)
