from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap

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
        
        # Wrap text
        wrapped_text = self.wrap_text(text, font, width - 40)  # Adjust for padding

        # Calculate text height and position
        total_text_height = sum([font.getsize(line)[1] for line in wrapped_text])
        total_text_height += font.getsize(wrapped_text[-1])[1]  # Add space for the author

        # Center text vertically
        y_position = (height - total_text_height) // 2

        # Draw wrapped text
        for line in wrapped_text:
            text_width, text_height = draw.textsize(line, font=font)
            x_position = (width - text_width) // 2
            draw.text((x_position, y_position), line, font=font, fill='white')
            y_position += text_height

        # Draw author text
        author_text = f'- {author}'
        author_width, author_height = draw.textsize(author_text, font=font)
        author_x_position = (width - author_width) // 2
        author_y_position = y_position
        draw.text((author_x_position, author_y_position), author_text, font=font, fill='white')
        
        output_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 100000)}.jpg')
        img.save(output_path)
        return output_path

    def wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width."""
        lines = []
        words = text.split()
        current_line = ""
        
        for word in words:
            test_line = f"{current_line} {word}".strip()
            width, _ = font.getsize(test_line)
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines