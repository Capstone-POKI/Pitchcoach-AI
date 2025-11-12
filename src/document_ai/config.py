import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "pitchcotch")
LOCATION = os.getenv("LOCATION", "us")
PROCESSORS = {
    "OCR": os.getenv("OCR_PROCESSOR_ID", "YOUR_OCR_PROCESSOR_ID"),
    "LAYOUT": os.getenv("LAYOUT_PROCESSOR_ID", "YOUR_LAYOUT_PROCESSOR_ID"),
    "FORM": os.getenv("FORM_PROCESSOR_ID", "YOUR_FORM_PROCESSOR_ID"),
}