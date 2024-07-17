import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.feature import match_template
import imagehash
from PIL import Image
import sys

def compare_histograms(image1, image2):
    hist1 = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def compare_ssim(image1, image2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    return ssim(gray1, gray2)

def compare_mse(image1, image2):
    mse = np.mean((image1 - image2) ** 2)
    return mse

def compare_mae(image1, image2):
    mae = np.mean(np.abs(image1 - image2))
    return mae

def compare_feature_matching(image1, image2):
    result = match_template(image1, image2)
    return np.max(result)

def compare_image_hash(image1_path, image2_path):
    hash1 = imagehash.average_hash(Image.open(image1_path))
    hash2 = imagehash.average_hash(Image.open(image2_path))
    return 1.0 - (hash1 - hash2) / len(hash1.hash) ** 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <image1> <image2>")
        return

    image1_path = sys.argv[1]
    image2_path = sys.argv[2]

    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None or image2 is None:
        print("Error: One or both image paths are invalid.")
        return

    # Histogram comparison
    hist_similarity = compare_histograms(image1, image2)
    print(f"Histogram similarity: {hist_similarity}")
    print("Explanation: Values close to 1 indicate high similarity in the color distributions of the images.")
    print("---------------------------------------------------------")

    # Structural Similarity Index (SSIM)
    ssim_similarity = compare_ssim(image1, image2)
    print(f"SSIM similarity: {ssim_similarity}")
    print("Explanation: Values range from -1 to 1, where 1 indicates a perfect match. Higher values indicate higher structural similarity.")
    print("---------------------------------------------------------")

    # Mean Squared Error (MSE)
    mse_similarity = compare_mse(image1, image2)
    print(f"MSE: {mse_similarity}")
    print("Explanation: Lower values indicate higher similarity. It's a measure of the average squared difference between the pixels of the images.")
    print("---------------------------------------------------------")

    # Mean Absolute Error (MAE)
    mae_similarity = compare_mae(image1, image2)
    print(f"MAE: {mae_similarity}")
    print("Explanation: Lower values indicate higher similarity. It's a measure of the average absolute difference between the pixels of the images.")
    print("---------------------------------------------------------")

    # Feature matching comparison
    feature_similarity = compare_feature_matching(image1, image2)
    print(f"Feature matching similarity: {feature_similarity}")
    print("Explanation: Higher values indicate higher similarity in feature matching between the images.")
    print("---------------------------------------------------------")

    # Image hashing comparison
    hash_similarity = compare_image_hash(image1_path, image2_path)
    print(f"Image hashing similarity: {hash_similarity}")
    print("Explanation: Values close to 1 indicate higher similarity. Compares hashes representing the images.")
    print("---------------------------------------------------------")

    # Overall assessment
    print("\nOverall assessment:")
    if hist_similarity > 0.9 and ssim_similarity > 0.5 and mse_similarity < 200 and mae_similarity < 200:
        print("The images are quite similar.")
    else:
        print("The images are not very similar.")

if __name__ == "__main__":
    main()
