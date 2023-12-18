import json
import csv

def process_reviews_in_chunks(file_path, chunk_size):
    counter = 0

    with open(file_path, 'r', encoding='utf-8') as file, open('review_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Rating', 'Count of "very"', 'Count of "extremely"'])

        while True:
            chunk = [next(file) for _ in range(chunk_size)]
            print('chunk' + str(counter))
            counter += 1 
            if not chunk:
                break

            for line in chunk:
                try:
                    item = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue

                review_text = item.get("reviewText", "").lower()
                overall_rating = item.get("overall", 0)

                count_very = review_text.count("very")
                count_extremely = review_text.count("extremely")

                csv_writer.writerow([overall_rating, count_very, count_extremely])

file_path = "amazon_reviews.json"
process_reviews_in_chunks(file_path, 100000)
