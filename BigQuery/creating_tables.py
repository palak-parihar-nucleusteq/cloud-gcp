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

dataset_name = "company"
#Schema for department table
table_dept = "department"
dept_schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("dept_name", "STRING", mode="REQUIRED")
]

table_ref = client.dataset(dataset_name).table(table_dept)
table = bigquery.Table(table_ref, schema=dept_schema)

table = client.create_table(table)
print(f"Created table {table.full_table_id}")

rows_to_insert = [
    {"id": "2", "dept_name":"Sales"},
    {"id": "1", "dept_name":"IT"}
]

errors = client.insert_rows_json(table, rows_to_insert)

if errors:
    print("Encountered errors while inserting rows: {}".format(errors))
else:
    print("Rows inserted successfully!")
    
#Quering department table

departments = client.query(query="SELECT * FROM company.department", job_config=QueryJobConfig())

for row in departments:
        print(row)
        

#Creating employees table

emp_table = "employee"

emp_schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("salary", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("departmentId", "INTEGER", mode="REQUIRED")
]

table_ref = client.dataset(dataset_name).table(emp_table)
table = bigquery.Table(table_ref, schema=emp_schema)

table = client.create_table(table)
print(f"Created table {table.full_table_id}")

rows_to_insert = [
    {"id": 1, "name":"Joe", "salary":"85000", "departmentId":1},
    {"id": 2, "name":"Henry", "salary":"80000", "departmentId":2},
    {"id": 3, "name":"Sam", "salary":"60000", "departmentId":2},
    {"id": 4, "name":"Max", "salary":"90000", "departmentId":1},
    {"id": 5, "name":"Janet", "salary":"69000", "departmentId":1},
    {"id": 6, "name":"Randy", "salary":"85000", "departmentId":1},
    {"id": 7, "name":"Will", "salary":"70000", "departmentId":1}
]

errors = client.insert_rows_json(table, rows_to_insert)
        
if errors:
    print("Encountered errors while inserting rows: {}".format(errors))
else:
    print("Rows inserted successfully!")


# 5. Query the table

result = client.query(query="SELECT * FROM company.employee", job_config=QueryJobConfig())

for row in result:
        print(row)