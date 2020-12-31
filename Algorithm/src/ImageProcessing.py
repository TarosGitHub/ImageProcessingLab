from PIL import Image as im
import numpy as np

class Image:
    """Image class.

    Attributes:
        _image (numpy.ndarray): The image data.
        _image_path (string): The path to the image file.
    """
    _image = None
    _image_path = ''

    def __init__(self, path=''):
        """Initializes Image class: The Image class constructor.

        Args:
            path (string, optional): The path to the image file.
        """
        if path:
            self.open(path)

    def open(self, path):
        """Opens the image file specifyed by the argument of path.

        Args:
            path (string): The path to the image file.
        """
        self._image = np.array(im.open(path))
        self._image_path = path
