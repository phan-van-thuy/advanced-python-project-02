import random
import os
import requests
from flask import Flask, render_template, request, abort
from QuoteEngine import TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
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
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    img_path = './static/temp_image.jpg'
    response = requests.get(image_url)
    with open(img_path, 'wb') as file:
        file.write(response.content)

    path = meme.make_meme(img_path, body, author)
    os.remove(img_path)
    
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
