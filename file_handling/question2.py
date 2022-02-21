# 2] Create a sample.csv file,
# read the CSV file, and print each row to stdout. Add another column to the CSV and update the CSV file. Again read the updated CSV file and print each row.

# using pandas
# import pandas as pd

# df = pd.read_csv("addresses.csv")
# print(df.head())

# df["new_column"] = "abc"
# df.to_csv("addresses.csv", index=False)
# print(df.head())

# del df['new_column']
# df.to_csv("addresses.csv", index=False)

import csv
  
with open('addresses.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        print(row)

print("\n")

with open("addresses.csv") as file_obj2:
    for row in csv.reader(file_obj2):
        row.append('abc')
        print(row)

