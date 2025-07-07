import numpy as np

def preprocess_image(image):
    image = image.resize((128, 128))  # Match training input shape
    image = image.convert('L')        # Convert to grayscale
    image = np.array(image).flatten() # Flatten image
    return image.reshape(1, -1)       # Return as model input
