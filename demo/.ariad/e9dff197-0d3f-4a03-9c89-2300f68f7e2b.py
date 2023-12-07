def data_reporter(data):
    # Generate a detailed report of the data
    for item in data:
        print(f"ID: {item['id']}, Processed Value: {item['processed_value']}")
