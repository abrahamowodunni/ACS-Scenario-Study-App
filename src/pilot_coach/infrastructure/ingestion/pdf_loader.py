from pathlib import Path

from pypdf import PdfReader


class PDFLoader:
    def load(self, file_path: str) -> str:
        reader = PdfReader(Path(file_path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)
