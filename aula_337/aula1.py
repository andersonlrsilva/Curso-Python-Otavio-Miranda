from PIL import Image
from pathlib import Path


ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'


pil_image = Image.open(ORIGINAL)
