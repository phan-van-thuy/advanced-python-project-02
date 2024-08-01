from PIL import Image, ImageDraw, ImageFont
import os
import random

class MemeEngine:
    """MemeEngine class for generating memes with text."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme with a quote."""
        img = Image.open(img_path)
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        height = int(width * aspect_ratio)
        img = img.resize((width, height), Image.ANTIALIAS)

        draw = ImageDraw.Draw(img)
        
        # Use a default font
        try:
            font = ImageFont.truetype("arial.ttf", size=20)
        except IOError:
            font = ImageFont.load_default()
        
        text_position = random.choice([(10, 10), (10, height - 30), (width - 150, 10), (width - 150, height - 30)])
        draw.text(text_position, f'{text} - {author}', font=font, fill='white')

        output_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 100000)}.jpg')
        img.save(output_path)
        return output_path
