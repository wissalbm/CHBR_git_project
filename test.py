import csv

def extract_unique_values(csv_file):
    unique_values = []

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Get column headers

        # Initialize a dictionary to store unique values for each column
        unique_values_dict = {header: set() for header in headers}

        # Read each row and update unique values for each column
        for row in reader:
            for idx, value in enumerate(row):
                unique_values_dict[headers[idx]].add(value)

        # Convert unique values to vectors
        for header in headers:
            unique_values.append(list(unique_values_dict[header]))

    return unique_values

csv_file = "pretreatment/files/vecteurcsv_withEntete.csv"
unique_values = extract_unique_values(csv_file)

for idx, column_values in enumerate(unique_values):
    print(f"Column {idx + 1}: {column_values}")
