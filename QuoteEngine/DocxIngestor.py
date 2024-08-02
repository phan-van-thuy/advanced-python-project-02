import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor class for parsing DOCX files."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file can be ingested.

        Args:
            path (str): Path to the file.

        Returns:
            bool: True if file can be ingested, otherwise False.
        """
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a DOCX file and return a list of QuoteModel objects.

        Args:
            path (str): Path to the DOCX file.

        Returns:
            List[QuoteModel]: List of QuoteModel objects.
        """
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text:
                body, author = para.text.strip().split(' - ')
                quotes.append(QuoteModel(body, author))
        return quotes
