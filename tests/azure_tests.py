import unittest
import json
import sys

class AzureTests(unittest.TestCase):
    """
    Unit and integration testing for the Azure class
    """

    def setUp(self):
        """
        Initializes Azure object
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

    def test__makeUrl(self):
        """
        Tests the makeUrl method of Azure
        """
        url = self.azure._makeUrl('hwr.post')

        assert url

    def test_recognizeHandwritingFromFile(self):
        """
        Tests the recognizeHandwritingFromFile method of Azure
        """

        result = self.azure.recognizeHandwritingFromFile('data/42_handwritten.png')

        assert result
        assert result['lines'][0]['text'] == '42'


    def test_recognizeHandwriting(self):
        """
        Tests the recognizeHandwriting method of Azure
        """
        data = None
        with open('data/42_handwritten.png', 'rb') as f:
            data = f.read()

        assert data

        result = self.azure.recognizeHandwriting(data)

        assert result
        assert result['lines'][0]['text'] == '42'


if __name__ == '__main__':
    sys.path.insert(0, '../')

    from azure import Azure

    unittest.main()
