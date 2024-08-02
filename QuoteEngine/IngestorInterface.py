from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class for all ingestors."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file can be ingested.

        Args:
            path (str): Path to the file.

        Returns:
            bool: True if file can be ingested, otherwise False.
        """
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file and return a list of QuoteModel objects.

        Args:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: List of QuoteModel objects.
        """
        pass
