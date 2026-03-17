from dataclasses import dataclass


@dataclass(slots=True)
class SimpleChunker:
    chunk_size: int = 800
    overlap: int = 100

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
        chunks: list[str] = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start = max(end - self.overlap, end)
        return chunks
