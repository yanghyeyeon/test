import json
import re

def contains_text(s):
    # 쉼표로 구분된 값 중 숫자 이외의 문자가 있는지 확인
    parts = s.split(',')
    for part in parts:
        if not part.isdigit():  # 숫자가 아닌 부분이 있으면 텍스트로 간주
            return True
    return False  # 숫자만 있으면 False를 반환

def extract_text_notes(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = {
            'top_note': [],
            'base_note': [],
            'middle_note': [],
            'single_note': []
        }
        
        for item in data:
            if isinstance(item, dict):
                for note_type in results.keys():
                    note_value = item.get(note_type, '')
                    if note_value and contains_text(note_value):
                        results[note_type].append({
                            'id': item.get('id'),
                            'value': note_value
                        })
        
        return results
    
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file content is not valid JSON.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == '__main__':
    json_file = 'spices_sortnotes.json'  # 로컬 경로로 수정
    results = extract_text_notes(json_file)
    
    if results:
        for note_type, items in results.items():
            if items:  # 항목이 비어 있지 않으면 출력
                print(f"\n{note_type}:")
                for item in items:
                    print(f"ID: {item['id']}, Value: {item['value']}")
            else:
                print(f"\n{note_type}: No entries with text found.")
    else:
        print("No results to display.")
        
