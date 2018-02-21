import io

from PIL import Image
from models.template import Template
from azure import Azure

class ImageProcessor:
    """
    Handles processing of images. Takes images and boxes on them, and sends them to Azure for processing, returning the result.

    Args:
        template (Template): The template to use when processing the image
        service (Azure): A wrapper for a Computer Vision webservice
    """
    def __init__(self, template, service):
        self.template = template
        self.service = service

    def processImage(self, image):
        """
        Applies template to given image, returning values found

        Args:
            image (binary): binary for an image

        Returns:
            crops (dictionary): mapping from the template box names to values found in that box
        """

        image_handle = io.BytesIO(image)
        image = Image.open(image_handle)

        crops = {}
        # crop out each box, and run it through image recognition
        for box in self.template.boxes:
            area = box['descr']
            datatype = box['datatype']
            subimage = image.crop(box=(area[0], area[1], area[0]+area[2], area[1]+area[3]))
            subimagebytes = io.BytesIO()
            subimage.save(subimagebytes, 'png')
            subimage.save(box['name'] + '.png')
            subimagebytes.seek(0)
            raw_result = self.service.recognizeHandwriting(subimagebytes.read())
            print(raw_result)
            if raw_result['lines'] == []:
                crops[box['name']] = None
            else:
                crops[box['name']] = self._processResult(raw_result['lines'][0]['text'], datatype)

        return crops

    def _processResult(self, result, datatype):
        """
        Converts given result to given datatype

        Args:
            result (str): text parsed from image
            datatype (str): desired type to convert text parsed from image to
        """
        return {
            'int': lambda res: int(res),
            'str': lambda res: res,
        }[datatype](result)
