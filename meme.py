import os
import random
import argparse
from QuoteEngine import TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor, QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme given an image path and a quote.
    
    Args:
        path (str): Path to the image file.
        body (str): Quote body text.
        author (str): Quote author.
        
    Returns:
        str: Path to the generated meme image.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/vietnam/"
        imgs = [os.path.join(root, name) for root, _, files in os.walk(images) for name in files]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            if TextIngestor.can_ingest(file):
                quotes.extend(TextIngestor.parse(file))
            elif DocxIngestor.can_ingest(file):
                quotes.extend(DocxIngestor.parse(file))
            elif PDFIngestor.can_ingest(file):
                quotes.extend(PDFIngestor.parse(file))
            elif CSVIngestor.can_ingest(file):
                quotes.extend(CSVIngestor.parse(file))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme")
    parser.add_argument('--path', type=str, help="Path to an image file")
    parser.add_argument('--body', type=str, help="Quote body to add to the image")
    parser.add_argument('--author', type=str, help="Quote author to add to the image")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
