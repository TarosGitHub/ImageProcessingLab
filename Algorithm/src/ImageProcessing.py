from PIL import Image as im
import numpy as np

class Image:
    """Image class.

    Attributes:
        _image (numpy.ndarray): The image data.
        _width (int): The width of the image.
        _height (int): The height of the image.

    Note:
        The coordinate system of the image is as follows:
             z
           /
          /
        O/_________________x
        |
        |
        |
        |
        |
        y
        The side O-x is the width of the image.
        The side O-y is the height of the image.
        The side O-z is the RGB array of the pixel specifyed by x and y: [R, G, B]. In case grayscale images, the argument doesn't exist.
    """

    def __init__(self, path='', height=0, width=0, grayscale=False):
        """Initializes Image class: The Image class constructor.

        # TODO: pathを指定した場合はheight, widthは無視されるなどの引数のパターンは要説明

        Args:
            path (string, optional): The path to the image file.
            height (int, optional): The height of the image.
            width (int, optional): The width of the image.
            grayscale (bool, optional): Opens the image file in grayscale.
        """
        self._image = None
        self._height = 0
        self._width = 0

        if path:
            self.open(path, grayscale)
        else:
            if height != 0 and width != 0 and grayscale:
                # TODO: RGB画像にも対応する
                # TODO: 黒画像などにも対応する(最後の* 255の部分) → 黒画像の場合には np.zeros((256, 256), np.uint8)
                # 白画像を作成する
                self._image = np.ones((height, width), np.uint8) * 255
                self._height = self._image.shape[0]
                self._width = self._image.shape[1]

    def __getitem__(self, index):
        """The reference operator getting image data.

        Args:
            index (tuple(x, y, z)): The image index.
                                    x is the index of x coordinate.
                                    y is the index of y coordinate.
                                    z is the index of the RGB array of the pixel: [R, G, B]. In case grayscale images, the argument doesn't exist.

        Returns:
            int: Returns the value of the specifyed R or G or B.
        """
        return self._image[index]

    def __setitem__(self, index, value):
        """The reference operator setting image data.

        Args:
            index (tuple(x, y, z)): The image index.
                                    x is the index of x coordinate.
                                    y is the index of y coordinate.
                                    z is the index of the RGB array of the pixel: [R, G, B]. In case grayscale images, the argument doesn't exist.
            value (int): The value between 0 and 255 to set.

        TODO: return self._image[index] しなくていい？
        """
        self._image[index] = value

    @property
    def width(self):
        """Gets the width of the image.
        """
        return self._width

    @property
    def height(self):
        """Gets the height of the image.
        """
        return self._height

    def open(self, path, grayscale=False):
        """Opens the image file specifyed by the argument of path.

        Args:
            path (string): The path to the image file.
            grayscale (bool, optional): Opens the image file in grayscale.
        """
        if grayscale:
            self._image = np.array(im.open(path).convert('L'))
        else:
            self._image = np.array(im.open(path))
        self._height = self._image.shape[0]
        self._width = self._image.shape[1]

    def save(self, path):
        """Saves the image in the specified path.

        Args:
            path (string): The path to save the image.
        """
        im.fromarray(self._image).save(path)

    def copy(self):
        """Copies the Image object.

        This copy is a deep copy.

        Returns:
            Image: Returns a deep copy of this Image object.
        """
        copy = Image()
        copy._image = self._image.copy()
        copy._height = self._height
        copy._width = self._width

        return copy

    def threshold(self, threshold, high=255, low=0):
        """Executes threshold processing.

        This process can only be done with grayscale images.

        Args:
            threshold (int): The threshold. 0 <= threshold <= 255.
            high (int, optional): This is set if the pixcel value is greater than the threshold. 0 <= high <= 255.
            low (int, optional): This is set if the pixcel value is less than or equal to the threshold. 0 <= low <= 255.

        Returns:
            Image: Returns the image executed threshold processing.
        """
        output_image = self.copy()

        for i in range(0, self._height):
            for j in range(0, self._width):
                if self._image[i, j] <= threshold:
                    output_image[i, j] = low
                else:
                    output_image[i, j] = high

        return output_image
