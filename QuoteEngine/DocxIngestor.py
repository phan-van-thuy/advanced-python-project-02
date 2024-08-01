# QuoteEngine/DocxIngestor.py
import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text:
                body, author = para.text.strip().split(' - ')
                quotes.append(QuoteModel(body, author))
        return quotes
