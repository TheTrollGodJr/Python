import csv

# Input and output file paths
input_file_path = 'C:/Users/thetr/Documents/Glados/list.txt'
output_csv_path = 'output.csv'

# Read lines from the input text file
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Write to the output CSV file
with open(output_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='|')

    # Write header
    csv_writer.writerow(['AudioPath', 'Transcript'])

    # Write data rows
    for line in lines:
        parts = line.strip().split('|')
        csv_writer.writerow(parts)

print(f'Conversion completed. CSV file saved at: {output_csv_path}')