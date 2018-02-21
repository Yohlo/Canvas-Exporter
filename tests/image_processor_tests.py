import unittest

class ImageProcessorTests(unittest.TestCase):
    """
    Unit and integration testing for ImageProcessor class
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

    def test_processImage(self):
        pass

if __name__ == '__main__':
    sys.path.insert(0, '../')
    sys.path.insert(0, '../models/')

    from azure import Azure
    from template import Template

    unittest.main()
