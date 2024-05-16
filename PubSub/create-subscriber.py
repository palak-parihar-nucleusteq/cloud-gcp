import os
from google.cloud import pubsub_v1

# Define the emulator host and port
emulator_host = "localhost:8085"
project_id = "dummy-project"  # project-id
topic_name = "hello"  # topic name
subscription_name = "hello-subs"  # subscription name

# Set the environment variable for the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = emulator_host

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Create a topic path
topic_path = subscriber.topic_path(project_id, topic_name)

# Create a subscription path
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Create the subscription if it does not exist
try:
    subscription = subscriber.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )
    print(f"Subscription created: {subscription.name}")
except Exception as e:
    print(f"Error creating subscription: {e}")
