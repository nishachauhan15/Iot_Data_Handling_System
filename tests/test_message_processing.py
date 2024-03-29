# tests/test_message_processing.py
import unittest
from message_processing.processor import process_message

class TestMessageProcessing(unittest.TestCase):
    def test_process_message(self):
        # Test processing of a valid message
        message = '{"sensor_id": 1, "value": 25.5}'
        result = process_message(message)
        self.assertEqual(result, "Message processed successfully")

        # Test processing of an invalid message
        invalid_message = '{"sensor_id": "invalid", "value": "invalid"}'
        result = process_message(invalid_message)
        self.assertEqual(result, "Invalid message format")

# tests/test_database_operations.py
import unittest
from mongodb_integration.database import insert_into_mongodb

class TestDatabaseOperations(unittest.TestCase):
    def test_insert_into_mongodb(self):
        # Test insertion of a message into MongoDB
        message = {"sensor_id": 1, "value": 25.5}
        result = insert_into_mongodb(message)
        self.assertIsNotNone(result)
