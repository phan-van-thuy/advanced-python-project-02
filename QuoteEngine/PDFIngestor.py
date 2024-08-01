import subprocess
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Ingestor class for parsing PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> list:
        """Parse a PDF file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        try:
            tmp = f'./tmp/{os.path.basename(path)}.txt'
            subprocess.call(['pdftotext', path, tmp])
            with open(tmp, 'r', encoding='utf-8') as file:
                for line in file:
                    if len(line) > 0:
                        parse = line.strip().split(' - ')
                        new_quote = QuoteModel(parse[0], parse[1])
                        quotes.append(new_quote)
            os.remove(tmp)
        except Exception as e:
            print(f"Error reading {path}: {e}")

        return quotes
