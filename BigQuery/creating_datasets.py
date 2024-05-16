from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud import bigquery

client_options = ClientOptions(api_endpoint="http://192.168.2.189:9050")
client = bigquery.Client(
  project="test-project",
  client_options=client_options,
  credentials=AnonymousCredentials(),
)

#Creating datasets
dataset_id = "company_d"

client.create_dataset(dataset_id)