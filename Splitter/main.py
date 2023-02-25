import pandas as pd

# Set the desired number of rows per split file
rows_per_file = 40000

# Read in the large CSV file
df = pd.read_csv('PVTSeller.csv')

# Get the total number of rows in the file
total_rows = len(df)

# Calculate the number of split files needed
num_files = total_rows // rows_per_file + 1

# Loop through and create each split file
for i in range(num_files):
    # Calculate the start and end rows for this split file
    start_row = i * rows_per_file
    end_row = min((i + 1) * rows_per_file, total_rows)

    # Create a new DataFrame with the rows for this split file
    split_df = df.iloc[start_row:end_row]

    # Write the split file to disk
    split_df.to_csv(f'splitCSV/file_{i}.csv', index=False)
