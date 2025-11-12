import json
from pathlib import Path

def save_json(data, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON 저장 완료: {path}")

def read_bytes(file_path):
    with open(file_path, "rb") as f:
        return f.read()