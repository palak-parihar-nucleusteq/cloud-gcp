import pandas as pd

# Replace 'file_path.xlsx' with the path to your Excel file
# df = pd.read_excel(r'C:\Users\palak\OneDrive\Desktop\GCP\sample_xls.xls')
df = pd.read_excel(r'C:\Users\palak\OneDrive\Desktop\GCP\no_dupes.xls')

# Display all entries in the dataframe
# print(df.to_string())

specific_row = df[(df['Age'] == 32) &(df['Gender'] == 'Female') & (df['Last Name'] == 'Abril')]

print(specific_row.to_string())

# df_without_duplicates = df.drop_duplicates()

# Save the DataFrame without duplicates to a new Excel file
# df_without_duplicates.to_excel(r'C:\Users\palak\OneDrive\Desktop\GCP\no_dupes.xls', index=False)

# df_without_duplicates = df.drop_duplicates()

# Save the DataFrame without duplicates to a new Excel file
# df_without_duplicates.to_excel('file_path_without_duplicates.xlsx', index=False)