from google.cloud import documentai
from src.utils.io_utils import save_json, read_bytes
from src.document_ai.config import PROJECT_ID, LOCATION, PROCESSORS

def process_document(file_path: str, processor_type: str, output_path: str):
    """Document AI로 문서를 처리하고 JSON으로 저장"""
    processor_id = PROCESSORS[processor_type]
    client = documentai.DocumentProcessorServiceClient()
    name = f"projects/{PROJECT_ID}/locations/{LOCATION}/processors/{processor_id}"

    print(f"📄 [{processor_type}] {file_path} 분석 시작...")

    document = {
        "content": read_bytes(file_path),
        "mime_type": "application/pdf",
    }

    result = client.process_document(request={"name": name, "raw_document": document})
    doc = result.document

    # 기본 텍스트 + 필드 + 테이블 등 구조화
    output = {
        "processor": processor_type,
        "text": doc.text[:1000],  # 미리보기용
        "entities": [
            {"type": e.type_, "mention_text": e.mention_text, "confidence": e.confidence}
            for e in doc.entities
        ],
        "pages": [
            {
                "pageNumber": p.page_number,
                "tables": len(p.tables),
                "paragraphs": len(p.paragraphs),
                "blocks": len(p.blocks),
            }
            for p in doc.pages
        ],
    }

    save_json(output, output_path)
    print(f"[{processor_type}] 결과 저장 완료\n")
    return output
