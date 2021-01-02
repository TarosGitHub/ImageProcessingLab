from abc import ABCMeta, abstractmethod

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
