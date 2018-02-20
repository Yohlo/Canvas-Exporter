import requests
import json

class Azure:
    """
    Azure object handles interactions with the Azure API
    
    Args:
        url (str): The base URL to the Azure endpoint being utilized.
        key (str): The Azure subscription key which provides access to this endpoint.

    Current features include:

    Expanding Functionality:
        To add features, refer to the Azure Cognitive Services API: https://docs.microsoft.com/en-us/azure/#pivot=products&panel=cognitive

        Ideally this class will provide an interface to all Azure cognitive APIs, but the current implementation is tailored towards the Azure computer vision API.
    """
    def __init__(self, url, key):
        self.url = url
        self.key = key

        # TODO: Improve checking validity of url and key
        assert url
        assert key


    def recognizeHandwriting(self, file_path):
        """
        This function returns the handwritten text detected in an image.

        Args:
            file_path (str): Path to the image which will be sent. Must be in format JPEG, PNG, GIF, or BMP. Files size must be less than 4MB. Dimensions must be at least 50x50.

        Returns:
            result (json): JSON object with OCR results from API request.

        References:
            [1] https://westus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/587f2c6a154055056008f200
        """
        text_recognition_url = self.url + "RecognizeText"

        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': self.key}
        params = {'handwriting': True}

        # TODO: Load binary file, send request
