'''
This is another file which generates random books for the library
'''


import csv
from faker import Faker
import random

fake = Faker()

# Generate data for 100 books
books = []
for _ in range(100):
    book = {
        "Name": fake.sentence(nb_words=3),
        "Author": fake.name(),
        "Date of Publication": fake.date_this_century(),
        "Rating on GoodReads": round(random.uniform(3, 5), 2)  # Random rating between 3 and 5
    }
    books.append(book)

# Write data to CSV file
csv_file_path = "data.csv"
fieldnames = ["Name", "Author", "Date of Publication", "Rating on GoodReads"]

with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    writer.writerows(books)

print(f"CSV file '{csv_file_path}' created successfully.")


