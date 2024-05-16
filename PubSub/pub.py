import json
from google.cloud import pubsub_v1
import os
# Define the emulator host and port
emulator_host = "localhost:8085"
project_id = 'dummy-project'  # project-id
topic_name = "hello-123"

# Set the environment variable for the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = emulator_host

# Create a publisher client
publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_name)

for n in range(1, 10):
    # Create your JSON data
    json_data = {
        "message_number": n,
        "content": f"Message number {n}"
    }
    # Serialize JSON data to a byte string
    data_str = json.dumps(json_data)
    data = data_str.encode("utf-8")
    # Publish the message
    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")
