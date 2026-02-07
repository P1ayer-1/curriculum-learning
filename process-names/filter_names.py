from datasets import load_dataset
import csv

csv_path = r'D:\Tiny Models\curriculum-learning\process-names\baby-names-frequency_2024.csv'
output_path = r'D:\Tiny Models\curriculum-learning\process-names\top_names_2021_2024.csv'

dataset = load_dataset('csv', data_files=csv_path, split='train')

YEARS = {2021, 2022, 2023, 2024}
GENDERS = {'Boy', 'Girl'}

# Set to store unique (name, gender)
name_set = set()

for year in YEARS:
    for gender in GENDERS:
        # Filter rows for year + gender
        filtered = [
            row for row in dataset
            if row['Year'] == year and row['Gender'] == gender
        ]

        # Sort by ranking column (lowest = best rank)
        filtered.sort(key=lambda x: x['Ranking by Gender & Year'])

        # Take top 100 rows (ties already handled by ordering)
        top_100 = filtered[:100]

        for row in top_100:
            name = row['First Name'].strip()  # remove trailing spaces
            name_set.add((name, gender))

# Write to CSV
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'gender'])
    for name, gender in sorted(name_set):
        writer.writerow([name, gender])

print(f"Wrote {len(name_set)} unique names to {output_path}")