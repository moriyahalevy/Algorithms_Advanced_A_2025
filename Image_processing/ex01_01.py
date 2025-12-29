import sys
from PIL import Image

def split_channels(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        
        r, g, b = img.split()
        
        r.show(title="Red Channel")
        g.show(title="Green Channel")
        b.show(title="Blue Channel")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        split_channels(sys.argv[1])
    else:
        print("Please provide an image path.")