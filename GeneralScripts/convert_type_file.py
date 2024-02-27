import pandas as pd
import csv
def excel_to_csv(excel_file: object, csv_file: object) -> object:
    try:
        # Read the Excel file using the read_excel function from pandas
        df = pd.read_excel(excel_file)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

        # Print a success message
        print(f'The Excel file "{excel_file}" has been converted to CSV as "{csv_file}".')
    except Exception as e:
        print(f"An error occurred: {e}")


def csv_to_excel(csv_file, excel_file):
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(csv_file)

    # Write DataFrame to Excel file
    df.to_excel(excel_file, index=False)

    print("CSV file converted to Excel successfully!")