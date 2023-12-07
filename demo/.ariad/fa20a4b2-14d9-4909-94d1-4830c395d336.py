def data_processor(data):
    # More complex data processing
    return [{"id": item["id"], "processed_value": item["value"] * 2} for item in data]
