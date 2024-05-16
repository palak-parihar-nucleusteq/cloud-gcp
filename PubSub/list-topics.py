import os
from google.cloud import pubsub_v1

# Define the emulator host and port
emulator_host = "localhost:8085"
project_id = 'dummy-project'  # project-id
topic_id = "hello"

# Set the environment variable for the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = emulator_host

publisher = pubsub_v1.PublisherClient()
project_path = f"projects/{project_id}"

for topic in publisher.list_topics(request={"project": project_path}):
    print("topics", topic)
    
topic_path = publisher.topic_path(project_id, "hello")
response = publisher.list_topic_subscriptions(request={"topic": topic_path})
for subscription in response:
    print("subscription: ",subscription)
