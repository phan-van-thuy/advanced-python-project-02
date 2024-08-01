# QuoteEngine/IngestorInterface.py
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class for all ingestors."""

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
