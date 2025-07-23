# json_helper.py

def load_json(file_path):
    """Load a JSON file and return its contents."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    """Save data to a JSON file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(file_path, key, value):
    """Update a specific key in a JSON file."""
    data = load_json(file_path)
    data[key] = value
    save_json(data, file_path)

def get_value_from_json(file_path, key):
    """Get a value from a JSON file by key."""
    data = load_json(file_path)
    return data.get(key)