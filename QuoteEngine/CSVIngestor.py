import pandas as pd
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingestor class for parsing CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> list:
        """Parse a CSV file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        try:
            df = pd.read_csv(path, encoding='utf-8')
            for _, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
        except Exception as e:
            print(f"Error reading {path}: {e}")

        return quotes
