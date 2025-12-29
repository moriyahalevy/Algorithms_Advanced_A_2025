from PIL import Image
import sys

def stretch_bw(image_path):
    img = Image.open(image_path).convert('L')
    
    v_min, v_max = img.getextrema()
    
    if v_max > v_min:
        stretched = img.point(lambda p: (p - v_min) * 255 / (v_max - v_min))
    else:
        stretched = img
        
    stretched.show(title="Stretched BW Image")
    stretched.save("ex01_02_result.png")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        stretch_bw(sys.argv[1])