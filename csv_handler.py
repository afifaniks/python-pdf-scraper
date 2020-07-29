import csv
import os
import sys


def store_to_csv(data):
    csv_file_name = "bvd.csv"
    # Create CSV if not exists
    if not os.path.isfile(csv_file_name):
        columns = ['Utility Type',
                   'State Name',
                   'Company Legal Name',
                   'Address of Principal Office',
                   'Year of Report',
                   'Operating Revenue (Total Current Year to Date Balance for Quarter/Year)',
                   'Operating Revenue (Total Prior Year to Date Balance for Quarter/Year)',
                   'Title of the Report',
                   'Hyperlink',
                   'Timestamp']

        with open(csv_file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(columns)

    # Appending data
    with open(csv_file_name, 'a+') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

    print("Finished Writing")

# Get terminal arguments if any
row = sys.argv[1:]

row = ["Gas", "Nevada", "Test Company", "Test Address", 2020, 200, 500, "Test Title", "https://link", "Today"]

store_to_csv(row)