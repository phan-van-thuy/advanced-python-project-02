from flask import Flask, render_template, request
import requests
from MemeEngine import MemeEngine
from QuoteEngine import TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor, QuoteModel
import os
from PIL import UnidentifiedImageError
import random

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]

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

    images_path = "./_data/photos/vietnam/"
    imgs = [os.path.join(root, name) for root, _, files in os.walk(images_path) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    img_path = './static/temp_image.jpg'
    error_message = None

    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(img_path, 'wb') as file:
            file.write(response.content)

        # Attempt to create a meme with the downloaded image
        path = meme.make_meme(img_path, body, author)
        os.remove(img_path)
        return render_template('meme.html', path=path)

    except requests.RequestException:
        error_message = "Sorry, invalid image URL, please try again."
    except UnidentifiedImageError:
        error_message = "Sorry, the URL does not contain a valid image, please try another URL."
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

    return render_template('meme_form.html', error=error_message)


if __name__ == "__main__":
    app.run()
