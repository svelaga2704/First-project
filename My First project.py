import csv

# Read the CSV file
with open('C:\First project\dinoDatasetCSV.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Example transformation: Uppercase a column named 'Name'
for row in rows:
    if 'Name' in row:
        row['Name'] = row['Name'].upper()

# Add a new column based on existing data
for row in rows:
    if 'Age' in row:
        row['AgeCategory'] = 'Adult' if int(row['Age']) >= 18 else 'Child'

# Write the transformed data to a new CSV
with open('transformed_dinoDataset.csv', mode='w', newline='', encoding='utf-8') as outfile:
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("Transformation complete. Saved to 'transformed_dinoDataset.csv'")
