from pilot_coach.infrastructure.ingestion.chunker import SimpleChunker
from pilot_coach.infrastructure.ingestion.metadata_extractor import MetadataExtractor
from pilot_coach.infrastructure.ingestion.pdf_loader import PDFLoader


class UpsertPipeline:
    def __init__(self) -> None:
        self.loader = PDFLoader()
        self.chunker = SimpleChunker()
        self.metadata_extractor = MetadataExtractor()

    def prepare(self, file_path: str) -> list[dict]:
        text = self.loader.load(file_path)
        chunks = self.chunker.chunk(text)
        return [
            {
                "page_content": chunk,
                "metadata": self.metadata_extractor.extract(chunk),
            }
            for chunk in chunks
        ]
