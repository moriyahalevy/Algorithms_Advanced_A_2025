from PIL import Image
import sys

def stretch_channel(channel):
    # חישוב ומתיחה לכל צבע בנפרד 
    c_min, c_max = channel.getextrema()
    if c_max > c_min:
        return channel.point(lambda p: (p - c_min) * 255 / (c_max - c_min))
    return channel

def stretch_rgb(image_path):
    img = Image.open(image_path).convert('RGB')
    
    r, g, b = img.split()
    
    r_s = stretch_channel(r)
    g_s = stretch_channel(g)
    b_s = stretch_channel(b)
    
    result = Image.merge('RGB', (r_s, g_s, b_s))
    result.show()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        stretch_rgb(sys.argv[1])