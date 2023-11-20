import csv

# Specify the path to your CSV file
file_path = '/Users/adityamaindan/Desktop/Dadas/Spares&Parts.csv'

# Function to count rows in a CSV file
def count_rows(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        # Use csv.reader to read the CSV file
        csv_reader = csv.reader(file)
        
        # Use len() to count the number of rows
        row_count = len(list(csv_reader))
        return row_count

# Get the row count
num_rows = count_rows(file_path)

# Print the result
print(f"Number of rows in the CSV file: {num_rows}")
