import numpy as np
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    image = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            val = ((x / (width - 1)) + (y / (height - 1))) / 2 * 255
            image[y, x] = int(val)
            
    return image

# הפעלה לדוגמה והצגה
gradient_img = create_gradient_image(255, 255)
plt.imshow(gradient_img, cmap='gray')
plt.title("Gradient Image")
plt.show()