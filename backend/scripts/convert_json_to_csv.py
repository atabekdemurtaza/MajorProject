import json
import pandas as pd


def json_to_csv(json_file, csv_file):
    """
    Convert a JSON file to a CSV file.

    Args:
        json_file (str): The path to the input JSON file.
        csv_file (str): The path to the output CSV file.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)
        # Normalize JSON to a flat table, specifying the separator for nested fields
        df = pd.json_normalize(data, sep='_')
        # Save DataFrame to CSV
        df.to_csv(csv_file, index=False)


# Convert JSON files to CSV
json_to_csv('data/json/users.json', 'data/csv/users.csv')
json_to_csv('data/json/products.json', 'data/csv/products.csv')
json_to_csv('data/json/reviews.json', 'data/csv/reviews.csv')
