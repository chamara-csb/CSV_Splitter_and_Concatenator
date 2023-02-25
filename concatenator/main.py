import os
import glob
import pandas as pd

# Set the path to the directory containing the CSV files
path_to_directory = 'CSVs'

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(path_to_directory, '*.csv'))

# Initialize an empty DataFrame to store the concatenated data
concatenated_df = pd.DataFrame()

# Loop through the CSV files and concatenate them into a single DataFrame
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)

# Write the concatenated data to a single CSV file
concatenated_df.to_csv('allData.csv', index=False)
