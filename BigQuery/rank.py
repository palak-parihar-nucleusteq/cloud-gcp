from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.cloud import bigquery

# Define client options
client_options = ClientOptions(api_endpoint="http://localhost:9050")

# Initialize BigQuery client
client = bigquery.Client(
    project="test-project",
    client_options=client_options,
    credentials=AnonymousCredentials(),
)

# Define SQL query
sql_query = """
WITH cte AS (
    SELECT d.dept_name AS Department, 
           e.name AS Employee, 
           e.salary,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS x_row
    FROM company.employee AS e 
    JOIN company.department AS d ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM cte
WHERE x_row <= 3
"""

# Execute query
query_job = client.query(sql_query)

# Fetch results
results = query_job.result()

# Display results
for row in results:
    print(row)
