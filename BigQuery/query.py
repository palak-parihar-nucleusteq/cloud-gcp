# 1. Create a BigQuery instance

from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig

client_options = ClientOptions(api_endpoint="http://localhost:9050")
client = bigquery.Client(
  project="test-project",
  client_options=client_options,
  credentials=AnonymousCredentials(),
)
# 1. Query the table

result = client.query(query="SELECT * from company.department", job_config=QueryJobConfig())

for row in result:
        print(row)