import json

# 파일 로드
with open("spice.json", "r", encoding="utf-8") as f:
    spices = json.load(f)

with open("top_note.json", "r", encoding="utf-8") as f:
    top_notes = json.load(f)

with open("base_note.json", "r", encoding="utf-8") as f:
    base_notes = json.load(f)

with open("middle_note.json", "r", encoding="utf-8") as f:
    middle_notes = json.load(f)

with open("single_note.json", "r", encoding="utf-8") as f:
    single_notes = json.load(f)

# 스파이스 이름과 ID 매핑 생성
spice_map = {spice["name_kr"]: spice["id"] for spice in spices}

# 매칭 함수 정의
def replace_notes_with_ids(notes, note_key):
    for note in notes:
        if note_key in note and note[note_key]:
            # 노트 필드를 쉼표로 분리한 뒤 ID로 매핑
            note_list = [n.strip() for n in note[note_key].split(",")]
            updated_list = [
                str(spice_map[n]) if n in spice_map else n for n in note_list
            ]
            note[note_key] = ",".join(updated_list)
    return notes

# 각 노트 데이터에 대해 처리
top_notes = replace_notes_with_ids(top_notes, "top_note")
base_notes = replace_notes_with_ids(base_notes, "base_note")
middle_notes = replace_notes_with_ids(middle_notes, "middle_note")
single_notes = replace_notes_with_ids(single_notes, "single_note")

# 결과 통합
sorted_notes = {
    "top_note": top_notes,
    "base_note": base_notes,
    "middle_note": middle_notes,
    "single_note": single_notes,
}

# 결과 저장
with open("spices_sortnotes.json", "w", encoding="utf-8") as f:
    json.dump(sorted_notes, f, ensure_ascii=False, indent=4)

print("spices_sortnotes.json 파일이 생성되었습니다.")
