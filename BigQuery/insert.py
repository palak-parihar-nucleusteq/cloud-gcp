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


# 2. Create a dataset

client.create_dataset("company")


# 3. Create a table

# Define the schema for the table
schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("first_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("last_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("address", "STRING", mode="NULLABLE")
]

# Create a new table instance
table_ref = client.dataset("company").table("users")
table = bigquery.Table(table_ref, schema=schema)


# 4. Insert test data into the table

rows_to_insert = [
        {"id": "1", "first_name": "Adam", "last_name": "Smith", "address": "12 Main Street"},
        {"id": "2", "first_name": "Jacques", "last_name": "Dupont", "address": "12 rue de la Ville"},
        {"id": "3", "first_name": "Antonio", "last_name": "Perez", "address": "12 calle Madrid"}
    ]

errors = client.insert_rows_json(table, rows_to_insert)

if errors:
    print("Encountered errors while inserting rows: {}".format(errors))
else:
    print("Rows inserted successfully!")


# 5. Query the table

result = client.query(query="SELECT * FROM company.users where id = 1", job_config=QueryJobConfig())

for row in result:
        print(row)