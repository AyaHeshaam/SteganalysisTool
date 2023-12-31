import cv2
import numpy as np

def extract_features(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Basic statistical features
    mean_value = np.mean(image)
    std_deviation = np.std(image)

    # Histogram-based features
    histogram, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    histogram_entropy = -np.sum((histogram / float(image.size)) * np.log2(histogram / float(image.size) + 1e-10))

    return mean_value, std_deviation, histogram_entropy

# Example usage
image_path = 'encoded.png'
mean_value, std_deviation, histogram_entropy = extract_features(image_path)

print(f"Mean Value: {mean_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Histogram Entropy: {histogram_entropy}")