# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import cv2
import numpy as np


def calc_psnr(img1, img2):
    imax = 255. ** 2
    mse = ((img1.astype(np.float64) - img2) ** 2).sum() / img1.size
    if mse == 0:
        return 10000000 #mozna dac inf  # <class 'numpy.float64'>
    return round(10.0 * np.log10(imax / mse),4)


def calc_mse(img1, img2):
    mse = ((img1.astype(np.float64) - img2) ** 2).sum() / img1.size
    if mse == 0:
        return 0.0
    return round(mse,4)


def calc_ssim(img1, img2):
    ssim_value = ssim(img1, img2)
    return round(ssim_value, 4)


def calc_ssim_color(img1, img2):
    # Convert the images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Check for same size and ratio and report accordingly
    ho, wo, _ = img1.shape
    hc, wc, _ = img2.shape
    ratio_orig = ho / wo
    ratio_comp = hc / wc
    dim = (wc, hc)

    if round(ratio_orig, 2) != round(ratio_comp, 2):
        print("\nImages not of the same dimension.")
        exit()

    # Resize first image if the second image is smaller
    elif ho > hc and wo > wc:
        print("\nResizing original image for analysis...")
        gray1 = cv2.resize(gray1, dim)

    elif ho < hc and wo < wc:
        print("\nCompressed image has a larger dimension than the original.")
        exit()

    if round(ratio_orig, 2) == round(ratio_comp, 2):
        ssim_value = ssim(gray1, gray2)
    return round(ssim_value,4)


if __name__ == '__main__':

    image1 = cv2.imread("lena_mono.png", cv2.IMREAD_UNCHANGED)
    # image2 = cv2.imread("./baboon_col.png", cv2.IMREAD_UNCHANGED)
    ksize = (5, 5)
    image2 = cv2.blur(image1, ksize)
    # image2 = cv2.imread("./baboon_col_noise.png", 3)
    cv2.imshow("image1", image1)
    cv2.imshow("image2", image2)

    ssim_val = calc_ssim(image1, image2)
    psnr_val = calc_psnr(image1, image2)
    mse_val = calc_mse(image1, image2)

    print(f"SSIM: {ssim_val}  PSNR: {psnr_val}  MSE: {mse_val}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
