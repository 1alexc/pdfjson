import json
import os

def convert_unicode_escape_sequences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    def decode_unicode(obj):
        if isinstance(obj, str):
            return obj.encode('utf-8').decode('unicode_escape')
        elif isinstance(obj, list):
            return [decode_unicode(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: decode_unicode(value) for key, value in obj.items()}
        return obj

    converted_data = decode_unicode(data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(converted_data, file, ensure_ascii=False, indent=4)

def main():
    output_data_folder = 'output_data'
    json_files = [
        'Print Personal Independence Payment (PIP)_ What PIP is for - GOV.UK.pdf.json',
        'Print Universal Credit_ What Universal Credit is - GOV.UK.pdf.json'
    ]

    for json_file in json_files:
        file_path = os.path.join(output_data_folder, json_file)
        convert_unicode_escape_sequences(file_path)

if __name__ == '__main__':
    main()