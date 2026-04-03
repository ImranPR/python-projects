import csv
from collections import Counter

word_list = []

# Read CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        for cell in row:
            words = cell.split()
            word_list.extend(words)

# Count words
word_count = Counter(word_list)

# Get top 20
top_words = word_count.most_common(20)

# Print result
for word, count in top_words:
    print(word, count)