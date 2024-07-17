# Image Comparison

This project provides a tool to compare two images using various similarity metrics, including histograms, structural similarity index (SSIM), mean squared error (MSE), mean absolute error (MAE), feature matching, and image hashing.

## Features

- **Histogram Comparison:** Compares the color distribution of the images.
- **SSIM:** Measures the structural similarity between the images.
- **MSE:** Calculates the mean squared error between the images.
- **MAE:** Calculates the mean absolute error between the images.
- **Feature Matching:** Compares the features of the images.
- **Image Hashing:** Compares the hash values of the images.

## How to Use

1. **Make sure you have Python installed on your system.**
2. **Clone this repository:**

    ```sh
    git clone https://github.com/e43b/Image-Comparison/
    ```

3. **Navigate to the project directory:**

    ```sh
    cd Image-Comparison
    ```

## Requirements

The following Python libraries are required to run the tool:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- scikit-image (`scikit-image`)
- imagehash (`imagehash`)
- Pillow (`PIL`)

Install the required libraries using the command:

```bash
pip install -r requirements.txt
```

## Usage

To compare two images, use the following command:

```bash
python main.py <image1> <image2>
```

For example:

```bash
python main.py 1.png 2.png
```

## Example Output

The output will display the similarity metrics for the given images and provide an overall assessment of their similarity.

### Sample Output

![mdf](fox/mdf.png) ![ori](fox/ori.png)

```
Histogram similarity: 0.5765597414419016
Explanation: Values close to 1 indicate high similarity in the color distributions of the images.
---------------------------------------------------------
SSIM similarity: 0.8644391986221096
Explanation: Values range from -1 to 1, where 1 indicates a perfect match. Higher values indicate higher structural similarity.
---------------------------------------------------------
MSE: 106.44129259259259
Explanation: Lower values indicate higher similarity. It's a measure of the average squared difference between the pixels of the images.
---------------------------------------------------------
MAE: 140.07771064814816
Explanation: Lower values indicate higher similarity. It's a measure of the average absolute difference between the pixels of the images.
---------------------------------------------------------
Feature matching similarity: 0.945
Explanation: Higher values indicate higher similarity in feature matching between the images.
---------------------------------------------------------
Image hashing similarity: 0.876
Explanation: Values close to 1 indicate higher similarity. Compares hashes representing the images.
---------------------------------------------------------

Overall assessment:
The images are structurally similar, but differ in color.
```

## Explanation of Metrics

- **Histogram Similarity:** Values close to 1 indicate high similarity in color distributions.
- **SSIM Similarity:** Values range from -1 to 1, where 1 indicates a perfect match. Higher values indicate higher structural similarity.
- **MSE:** Lower values indicate higher similarity. It's a measure of the average squared difference between the pixels of the images.
- **MAE:** Lower values indicate higher similarity. It's a measure of the average absolute difference between the pixels of the images.
- **Feature Matching Similarity:** Higher values indicate higher similarity in feature matching between the images.
- **Image Hashing Similarity:** Values close to 1 indicate higher similarity. Compares hashes representing the images.

## Overview

Based on the comparison metrics, the tool will provide an overall assessment of the similarity between the images.

## Additional Information

- **Discord Server:** [Join Here](https://discord.gg/bEyHhmbRVw)
- **GitHub:** [My GitHub Profile](https://github.com/e43b)
- **Donations:** [Donate Here](https://oxapay.com/donate/40874860)
