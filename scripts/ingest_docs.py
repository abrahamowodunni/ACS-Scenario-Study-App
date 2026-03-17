from pathlib import Path

from pilot_coach.infrastructure.ingestion.upsert_pipeline import UpsertPipeline


def main() -> None:
    pipeline = UpsertPipeline()
    raw_dir = Path("data/raw")
    pdfs = list(raw_dir.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in data/raw")
        return

    for pdf in pdfs:
        docs = pipeline.prepare(str(pdf))
        print(f"Prepared {len(docs)} chunks from {pdf.name}")


if __name__ == "__main__":
    main()
