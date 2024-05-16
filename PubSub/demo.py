import os
from google.cloud import pubsub_v1

# Define the emulator host and port
emulator_host = "localhost:8085"
project_id = 'dummy-project'  # project-id

# Set the environment variable for the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = emulator_host

# Create a publisher client
publisher = pubsub_v1.PublisherClient()

# Create a topic
topic_path = publisher.topic_path(project_id, "test-topic")
topic = publisher.create_topic(request={"name": topic_path})

print(f"Topic created: {topic.name}")
