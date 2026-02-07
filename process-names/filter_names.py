from datasets import load_dataset
import csv

csv_path = r'D:\Tiny Models\curriculum-learning\process-names\baby-names-frequency_2024.csv'
output_path = r'D:\Tiny Models\curriculum-learning\process-names\top_names_unique_2021_2024.csv'

dataset = load_dataset('csv', data_files=csv_path, split='train')

YEARS = {2021, 2022, 2023, 2024}
GENDERS = {'Boy', 'Girl'}

# name -> { gender, rank }
best_name_entry = {}

for year in YEARS:
    for gender in GENDERS:
        # Filter rows for this year & gender
        filtered = [
            row for row in dataset
            if row['Year'] == year and row['Gender'] == gender
        ]

        # Sort by ranking (lower = better)
        filtered.sort(key=lambda x: x['Ranking by Gender & Year'])

        # Take top 100 entries
        for row in filtered[:100]:
            name = row['First Name'].strip()
            rank = row['Ranking by Gender & Year']

            # If name not seen yet, store it
            if name not in best_name_entry:
                best_name_entry[name] = {
                    'gender': gender,
                    'rank': rank
                }
            else:
                # If seen, keep the better-ranked one
                if rank < best_name_entry[name]['rank']:
                    best_name_entry[name] = {
                        'gender': gender,
                        'rank': rank
                    }

# Count by gender
gender_counts = {'Boy': 0, 'Girl': 0}
for entry in best_name_entry.values():
    gender_counts[entry['gender']] += 1

# Write CSV
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'gender'])
    for name, entry in sorted(best_name_entry.items()):
        writer.writerow([name, entry['gender']])

print(f"Total unique names: {len(best_name_entry)}")
print(f"Boys: {gender_counts['Boy']}")
print(f"Girls: {gender_counts['Girl']}")
print(f"Output written to: {output_path}")
