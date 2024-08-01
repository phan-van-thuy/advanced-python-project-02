# QuoteEngine/QuoteModel.py
class QuoteModel:
    """A class representing a quote with body and author."""

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" - {self.author}'
