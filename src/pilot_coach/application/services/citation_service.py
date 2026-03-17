from pilot_coach.domain.models.citation import Citation


class CitationService:
    def build_citations(self, docs: list[dict]) -> list[Citation]:
        citations: list[Citation] = []
        for doc in docs:
            metadata = doc.get("metadata", {})
            citations.append(
                Citation(
                    source_title=metadata.get("source_title", "FAA Source"),
                    section=metadata.get("section"),
                    page=metadata.get("page"),
                    acs_code=metadata.get("acs_code"),
                )
            )
        return citations
