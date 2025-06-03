import os
import re
from PIL import Image
from markdown import markdown

def extract_text_and_images(md_path, assets_base_path):
    with open(md_path, 'r') as f:
        content = f.read()

    # Extract image paths and alt texts
    images = re.findall(r'!\[([^\]]*)\]\((.*?)\)', content)
    image_data = []
    for alt, path in images:
        full_path = os.path.join(assets_base_path, path)
        if os.path.exists(full_path):
            image_data.append((alt, full_path))
    
    # Strip out image markdown for clean text
    text = re.sub(r'!\[.*?\]\(.*?\)', '', content)

    return text, image_data
