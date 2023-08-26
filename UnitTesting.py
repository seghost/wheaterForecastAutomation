import unittest
from unittest.mock import Mock,patch
from main import get_geo_data,get_weather_data


class TestWeatherApi(unittest.TestCase):

    @patch('requests.get')
    def test_get_geo_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'lat': 41.8755616, 'lon': -87.6244212}]
        mock_get.return_value = mock_response

        geo_data = get_geo_data("Chicago", 1, "your_api_key")

        self.assertEqual(geo_data, [{'lat': 41.8755616, 'lon': -87.6244212}])
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_get_weather_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'weather': [{'description': 'Clear sky'}],
            'main': {'temp': 20}
        }
        mock_get.return_value = mock_response

        weather_data = get_weather_data(41.8755616, -87.6244212, "your_api_key")

        self.assertEqual(weather_data['weather'][0]['description'], 'Clear sky')
        self.assertEqual(weather_data['main']['temp'], 20)
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
