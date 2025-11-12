from src.document_ai.processor import process_document

# 입력/출력 경로
notice_input = "data/input/sample_notice.pdf"
irdeck_input = "data/input/sample_irdeck.pdf"
notice_output = "data/output/docai_notice.json"
irdeck_output = "data/output/docai_irdeck.json"

# OCR + LAYOUT + FORM 파이프라인 실행
for processor in ["OCR", "LAYOUT", "FORM"]:
    process_document(notice_input, processor, f"data/output/notice_{processor.lower()}.json")
    process_document(irdeck_input, processor, f"data/output/irdeck_{processor.lower()}.json")