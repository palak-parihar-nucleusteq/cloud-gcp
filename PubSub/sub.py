import os
from google.cloud import pubsub_v1


# Define the emulator host and port
emulator_host = "localhost:8085"
project_id = 'dummy-project'  # project-id
topic_name = 'hello'
subscription_name = 'hello-subs'

# Set the environment variable for the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = emulator_host

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Create the topic and subscription paths
topic_path = subscriber.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Create the subscription if it doesn't exist
subscription = subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})

print(f"Subscription created: {subscription.name}")

#A callback function to process received messages
def callback(message):
    print(f"Received message: {message}")
    # Process the message here

    # Acknowledge the message after processing
    message.ack()

# Subscribe to the subscription and start pulling messages
subscriber.subscribe(subscription_path, callback=callback)

# Keep the main thread alive to continue receiving messages
print(f"Listening for messages for topic {topic_path}...")
import time
while True:
    time.sleep(5)  # Keep the main thread alive
