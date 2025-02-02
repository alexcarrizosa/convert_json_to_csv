import json
import csv
import sys

def json_to_csv(json_filepath, csv_filepath):
    """
    Converts a JSON file to a CSV file.

    Args:
        json_filepath: The path to the input JSON file.
        csv_filepath: The path to the output CSV file.
    """
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_filepath}")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    if isinstance(data, dict):
        data = [data]  

    if not data:
        print("JSON data is empty.")
        return

    fieldnames = set()
    for item in data:
        fieldnames.update(item.keys())

    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(fieldnames))
        writer.writeheader()

        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_csv_converter.py <json_filepath> <csv_filepath>")
        sys.exit(1)

    json_filepath = sys.argv[1]
    csv_filepath = sys.argv[2]
    json_to_csv(json_filepath, csv_filepath)