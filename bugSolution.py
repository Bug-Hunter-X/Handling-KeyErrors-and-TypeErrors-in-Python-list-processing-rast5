def function_with_uncommon_error(data):
    try:
        # Assume data is a list of dictionaries, each with a 'value' key
        result = [item['value'] for item in data if isinstance(item, dict) and 'value' in item]
        return result
    except (KeyError, TypeError) as e:
        # Handle the exception here
        print(f"An error occurred: {e}")
        return []

data = [{'value': 1}, {'value': 2}, {'value': 'three'}]
print(function_with_uncommon_error(data)) #Output: [1, 2, 'three']
data = [{'value': 1}, {'value': 2}, {}] # Missing Key
print(function_with_uncommon_error(data)) #Output: [1, 2]
data = [{'value': 1}, {'value': 2}, 3] # Type Error
print(function_with_uncommon_error(data)) #Output: [1, 2] 