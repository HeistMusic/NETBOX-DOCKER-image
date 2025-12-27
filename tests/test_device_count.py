import unittest
from unittest.mock import patch, Mock
from api.device_count import get_devices


class TestDeviceCountAPI(unittest.TestCase):

    @patch("api.device_count.requests.get")
    def test_get_devices_with_status(self, mock_get):
        """
        Test retrieving devices filtered by status using mocked API response.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {"status": {"value": "active"}},
                {"status": {"value": "active"}},
            ],
            "next": None,
        }

        mock_get.return_value = mock_response

        devices = get_devices(
            "http://localhost:8000",
            "dummy-token",
            status="active"
        )

        self.assertEqual(len(devices), 2)

    @patch("api.device_count.requests.get")
    def test_api_error_handling(self, mock_get):
        """
        Test API error handling when a non-200 response is returned.
        """
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_get.return_value = mock_response

        with self.assertRaises(RuntimeError):
            get_devices(
                "http://localhost:8000",
                "invalid-token"
            )


if __name__ == "__main__":
    unittest.main()
