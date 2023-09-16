from index import handler
from unittest.mock import patch
import unittest
import json


class TestHandler(unittest.TestCase):
    def setUp(self):
        # Set up any test data or configurations you need
        self.mock_env = "test_environment"
        patch.dict("os.environ", {"ENVIRONMENT": self.mock_env}).start()

    def tearDown(self):
        # Clean up after each test if necessary
        patch.stopall()

    def test_home_page(self):
        # Test the home page
        event = {"rawPath": "/"}
        response = handler(event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"]["Content-Type"], "text/html")
        self.assertIn(f"The Sample Application - {self.mock_env}", response["body"])

    def test_get_all_data(self):
        with open("data.json", mode="r", encoding="utf-8") as data_file:
            data = json.load(data_file)

        event = {"rawPath": "/data"}
        response = handler(event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"]["Content-Type"], "application/json")
        self.assertEqual(response["body"], json.dumps(data))

    def test_get_item_by_id(self):
        with open("data.json", "r") as f:
            data = json.load(f)

        event = {"rawPath": "/1"}
        response = handler(event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"]["Content-Type"], "application/json")

        # Find the expected item in data based on the given ID
        item_id = event["rawPath"][1:]
        expected_item = next((item for item in data if item["id"] == item_id), None)
        self.assertEqual(response["body"], json.dumps(expected_item))

    def test_invalid_id(self):
        event = {"rawPath": "/invalid_id"}
        response = handler(event, None)
        self.assertEqual(response["statusCode"], 404)
        self.assertEqual(response["headers"]["Content-Type"], "application/json")
        self.assertIn(f"id {event['rawPath'][1:]} not found", response["body"])


if __name__ == "__main__":
    unittest.main()
