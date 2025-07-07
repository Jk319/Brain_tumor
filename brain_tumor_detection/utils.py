import numpy as np

def preprocess_image(image):
    image = image.resize((128, 128))  # Match your training size
    image = image.convert('L')  # Grayscale
    image = np.array(image).flatten()  # Flatten to 1D if classical ML
    image = image.reshape(1, -1)  # Model expects 2D (samples, features)
    return image
