import json
import os

try:
    # 현재 작업 디렉토리 출력
    print("현재 작업 디렉토리:", os.getcwd())
    print("현재 디렉토리의 파일 목록:", os.listdir())

    # JSON 파일 읽기
    with open('single_note (1).json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    transformed_data = []

    # 각 항목을 변환
    for item in data:
        # base_note 값을 콤마로 분리하여 리스트로 만듦
        note_spice_ids = [id.strip() for id in item['single_note'].split(',') if id.strip()]
        
        # 각 note_spice_id에 대해 새로운 딕셔너리 생성
        for note_spice_id in note_spice_ids:
            transformed_item = {
                'id': item['id'],
                'perfume_id': item['perfume_id'],
                'note_spice_id': note_spice_id,
                'note_type': 'single'  
            }
            transformed_data.append(transformed_item)

    # 변환된 데이터를 JSON 파일로 저장
    with open('transformed_notes.json', 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, indent=2, ensure_ascii=False)

    # 변환 결과 출력
    print(f"\n처리된 총 아이템 수: {len(transformed_data)}")
    print("\n처음 5개 아이템 예시:")
    for item in transformed_data[:5]:
        print(item)

except FileNotFoundError:
    print("Error: 입력 파일을 찾을 수 없습니다.")
    print("파일이 현재 디렉토리에 있는지 확인해주세요.")
except json.JSONDecodeError:
    print("Error: JSON 파일 형식이 올바르지 않습니다.")
except Exception as e:
    print(f"Error: 예상치 못한 오류가 발생했습니다: {str(e)}")