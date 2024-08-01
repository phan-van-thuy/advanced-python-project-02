import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor class for parsing TXT files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> list:
        """Parse a TXT file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    if len(line) > 0:
                        parse = line.strip().split(' - ')
                        new_quote = QuoteModel(parse[0], parse[1])
                        quotes.append(new_quote)
        except Exception as e:
            print(f"Error reading {path}: {e}")

        return quotes
