import numpy as np
from PIL import Image

# Load grayscale image
image = Image.open("input.jpg").convert("L")
pixels = np.array(image, dtype=np.float32)

# Define pattern (y, x) -> weight
pattern = [
    (0, 1, 0.5),
    (1, -1, 0.2),
    (1, 1, 0.2),
    (2, 0, 0.1)
]

height, width = pixels.shape

# Loop through pixels
for y in range(height):
    for x in range(width):
        old_pixel = pixels[y, x]
        new_pixel = 0 if old_pixel < 128 else 255
        error = old_pixel - new_pixel
        pixels[y, x] = new_pixel

        # Spread error
        for dy, dx, weight in pattern:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width:
                pixels[ny, nx] += error * weight

# Save result
Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8)).save("output.png")
