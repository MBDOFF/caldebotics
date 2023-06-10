import csv
import random
import time

MAX_DATA_ENTRIES = 50

while True:
    # Generate random data
    temperature = random.randint(0, 100)
    humidity = random.randint(0, 100)

    # Read existing data from the CSV file
    existing_data = []
    try:
        with open('data.txt', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                existing_data.append(row)
    except FileNotFoundError:
        pass

    # Remove excess data if more than MAX_DATA_ENTRIES
    if len(existing_data) >= MAX_DATA_ENTRIES:
        existing_data = existing_data[-(MAX_DATA_ENTRIES - 1):]

    # Append the new data
    existing_data.append([temperature, humidity])

    # Write updated data to the CSV file
    with open('data.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['temperature', 'humidity'])
        writer.writerows(existing_data)

    # Wait for 2 seconds
    time.sleep(2)
