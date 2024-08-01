# Meme Generator Project

## Overview
This project generates memes with quotes using a web application and command line interface. It supports ingesting quotes from various file formats including TXT, DOCX, PDF, and CSV, and generates images with captions using the Pillow library.

## Setup Instructions

### Prerequisites
- Python 3.6+
- pip

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/phan-van-thuy/advanced-python-project-02.git
    cd advanced-python-project-02
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv

    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Web Application

1. Start the Flask server:
    ```sh
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000`.

### Generating a Meme via CLI

1. Use the `meme.py` script to generate a meme:
    ```sh
    python meme.py --path ./_data/photos/vietnam/xander_1.jpg --body "Sample Quote" --author "Author"
    ```

## Project Structure
advanced-python-project-02/
│
├── QuoteEngine/
│ ├── init.py
│ ├── IngestorInterface.py
│ ├── TextIngestor.py
│ ├── DocxIngestor.py
│ ├── PDFIngestor.py
│ ├── CSVIngestor.py
│ └── QuoteModel.py
│
├── MemeEngine/
│ ├── init.py
│ └── MemeEngine.py
│
├── _data/
│ ├── DogQuotes/
│ │ ├── DogQuotesCSV.csv
│ │ ├── DogQuotesDOCX.docx
│ │ ├── DogQuotesPDF.pdf
│ │ └── DogQuotesTXT.txt
│ ├── photos/
│ │ └── vietnam/
│ │ ├── xander_1.jpg
│ │ ├── xander_2.jpg
│ │ ├── xander_3.jpg
│ │ └── xander_4.jpg
│ └── SimpleLines/
│ ├── SimpleLines.csv
│ ├── SimpleLines.docx
│ ├── SimpleLines.pdf
│ └── SimpleLines.txt
│
├── templates/
│ ├── base.html
│ ├── meme_form.html
│ └── meme.html
│
├── app.py
├── meme.py
├── requirements.txt
└── README.md


## Sub-modules

### QuoteEngine
- **IngestorInterface.py**: Abstract base class defining the interface for all ingestors.
- **TextIngestor.py**: Ingests quotes from TXT files.
- **DocxIngestor.py**: Ingests quotes from DOCX files.
- **PDFIngestor.py**: Ingests quotes from PDF files.
- **CSVIngestor.py**: Ingests quotes from CSV files.
- **QuoteModel.py**: Defines the QuoteModel class representing a quote with body and author.

### MemeEngine
- **MemeEngine.py**: Handles the creation of memes by adding text to images.

## Dependencies
All dependencies are listed in the `requirements.txt` file and can be installed using:
```sh
pip install -r requirements.txt

