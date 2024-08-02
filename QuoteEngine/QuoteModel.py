class QuoteModel:
    """A class representing a quote with body and author."""

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel instance.

        Args:
            body (str): Quote body text.
            author (str): Quote author.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """
        Return a string representation of the quote.

        Returns:
            str: Formatted quote string.
        """
        return f'"{self.body}" - {self.author}'
