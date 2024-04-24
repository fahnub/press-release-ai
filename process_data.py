import json


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def convert_data(original_data):
    formatted_data = []

    for item in original_data:
        prompt = f"Write a press release about '{item['title']}'"

        formatted_entry = {
            "messages": [
                {"role": "system", "content": "Your role is to write Press Releases for Azizi Developments, a real estate company in Dubai."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": item["content"]}
            ]
        }
        formatted_data.append(formatted_entry)
    return formatted_data


def save_as_jsonl(formatted_data, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        for entry in formatted_data:
            file.write(json.dumps(entry) + '\n')


def main():
    input_filename = 'articles.json'
    output_filename = 'articles.jsonl'

    data = load_data(input_filename)
    formatted_data = convert_data(data)
    save_as_jsonl(formatted_data, output_filename)

    print(f"Data has been formatted and saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
