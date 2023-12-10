import unittest
from unittest.mock import patch, call
from PIL import Image
from main import deep_fry, select_image

class TestMain(unittest.TestCase):

    @patch('main.Image.open')
    def test_deep_fry(self, mock_open):
        # Mock the image object
        mock_image = Image.new('RGB', (60, 30), color = 'red')
        mock_open.return_value = mock_image

        # Call the function
        result = deep_fry(mock_image)

        # Assert the function calls
        self.assertEqual(mock_open.call_count, 2)
        self.assertEqual(mock_open.call_args_list, [call('sat-deepfry-image.png'), call('comp-image.png')])

    @patch('main.filedialog.askopenfilename')
    @patch('main.Image.open')
    @patch('main.deep_fry')
    @patch('main.display_image')
    @patch('main.select_button', create=True)
    def test_select_image(self, mock_select_button, mock_display_image, mock_deep_fry, mock_open, mock_askopenfilename):
        # Mock the file dialog return value
        mock_askopenfilename.return_value = 'test.png'

        # Mock the image object
        mock_image = Image.new('RGB', (60, 30), color = 'red')
        mock_open.return_value = mock_image

        # Mock the deep_fry function return value
        mock_deep_fry.return_value = mock_image

        # Call the function
        select_image()

        # Assert the function calls
        mock_askopenfilename.assert_called_once()
        mock_open.assert_called_once_with('test.png')
        mock_deep_fry.assert_called_once_with(mock_image)
        mock_display_image.assert_called_once_with(mock_image)
        mock_select_button.place_forget.assert_called_once()

if __name__ == '__main__':
    unittest.main()
