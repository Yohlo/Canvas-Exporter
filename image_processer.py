from PIL import Image
from models.template import Template

class ImageProcesser:
    """
    Handles processing of images. Takes images and boxes on them, and sends them to Azure for processing, returning the result.

    Args:
        template (Template|None): The template to use when processing the image
    """
    def __init__(self, template=None):
        self.template = template

