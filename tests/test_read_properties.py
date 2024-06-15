########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
import os
import tempfile
import unittest

from unittest import TestCase
from unittest.mock import patch, mock_open
from utils.read_properties import ReadProperties

class TestReadProperties(TestCase):
    
    def setUp(self):
        # Create a temporary properties file for testing.
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.file_path = self.temp_file.name


    def tearDown(self):
        # Remove the temporary file after test
        os.remove(self.temp_file.name)


    def test_read_properties(self):
        # Initialize ReadProperties with the temp file path
        config = ReadProperties(filepath=self.file_path)
        config.read_properties()

        # Test if the properties are read correctly
        self.assertEqual(config.data_dir, '/path/to/data')
        self.assertEqual(config.data_file, 'example.txt')


    @patch('builtins.open', new_callable=mock_open, read_data='data_dir=/another/path\ndata_file=anotherfile.txt\n')
    def test_read_properties_with_mock(self, mock_file):
        # Test reading properties using mocked open
        config = ReadProperties(filepath="dummy/path/to/config.properties")
        config.read_properties()

        # Test if the properties are read correctly from the mock
        self.assertEqual(config.filepath, '/another/path')


    def test_no_file_provided(self):
        # Test behavior when no file path is provided
        config = ReadProperties()
        config.read_properties()

        self.assertIsNone(config.filepath)


    def test_non_existent_file(self):
        # Test behavior with a non-existent file
        config = ReadProperties(filepath="non_existent_file.properties")
        
        with self.assertRaises(FileNotFoundError):
            config.read_properties()


    def test_malformed_file_content(self):
        # Write malformed content to the temporary file
        with open(self.file_path, 'wb') as temp_file:
            temp_file.write(b'invalid content without equals sign\n')

        # Initialize ReadProperties with the temp file path
        config = ReadProperties(filepath=self.file_path)

        # Check if it handles malformed content gracefully
        with self.assertRaises(Exception):
            config.read_properties()


# Run the tests
if __name__ == '__main__':
    unittest.main()