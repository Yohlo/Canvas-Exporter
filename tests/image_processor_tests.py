import unittest
import json
import sys

class ImageProcessorTests(unittest.TestCase):
    """
    Unit and Integration testing for ImageProcessor class
    """

    def setUp(self):
        """
        Initializes Template and Azure objects
        """

        # Initialize configuration variables
        url = None
        key = None

        # Load configuration
        with open('../configs/azure.conf') as f:
            conf = json.load(f)

            url = conf['URL']
            key = conf['key1']

        # Check configuration variables
        assert url
        assert key

        # Initialize Azure object
        self.azure = Azure(url, key)

        # Initialize Template
        self.quiz_template = Template()
        self.quiz_template.addBox('score', (1450, 130, 165, 125), 'int')
        self.quiz_template.addBox('username', (1190, 201, 262, 77), 'str')

        # Initialize ImageProcessor
        self.ip = ImageProcessor(self.quiz_template, self.azure)

    def test_processImage(self):
        data = None
        with open('data/quiz_format.png', 'rb') as f:
            data = f.read()

        assert data
        
        image_results = self.ip.processImage(data)

        assert image_results

        assert image_results['score']
        assert image_results['username']

        print(image_results['score'])
        print(image_results['username'])


if __name__ == '__main__':
    sys.path.insert(0, '../')
    from image_processor import ImageProcessor
    from azure import Azure

    sys.path.insert(0, '../models/')
    from template import Template

    unittest.main()
