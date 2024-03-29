# message_processing/processor.py
import json

def process_message(message):
    try:
        data = json.loads(message)
        # Process message content (parsing, validation, transformation)
        if isinstance(data.get("sensor_id"), int) and isinstance(data.get("value"), float):
            # Assume message processing here
            print("Message processed successfully")
            return "Message processed successfully"
        else:
            print("Invalid message format")
            return "Invalid message format"
    except Exception as e:
        print("Error processing message:", e)
        return "Error processing message"
