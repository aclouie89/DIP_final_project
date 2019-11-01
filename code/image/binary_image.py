import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                pixel_val = image[row, col]
                if pixel_val >= 0 and pixel_val < 256:
                    hist[pixel_val] = hist[pixel_val] + 1
                else:
                    print("Found erroneous pixel value: " + str(pixel_val) + " at " + str(row) + ", " + str(col))

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        # init counters
        max_lo = 0
        max_hi = 0
        lo_cnt = 0
        hi_cnt = 0
        # init threshold
        threshold = len(hist) // 2
        # find the avg prob val before and after threshold
        for x in range(len(hist)):
            if x < threshold:
                max_lo = max_lo + x * hist[x]
                lo_cnt = lo_cnt + hist[x]
            else:
                max_hi = max_hi + x * hist[x]
                hi_cnt = hi_cnt + hist[x]
        # calc threshold value
        max_lo = max_lo // lo_cnt
        max_hi = max_hi // hi_cnt
        threshold = (max_lo + max_hi) // 2
        print("Threshold value is: " + str(threshold) + " with maximas: " + str(max_lo) + ", " + str(max_hi))

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        threshold = self.find_optimal_threshold(self.compute_histogram(image))
        print("Threshold is: " + str(threshold))

        bin_img = image.copy()
        for row in range(bin_img.shape[0]):
            for col in range(bin_img.shape[1]):
                if bin_img[row, col] <= threshold:
                    bin_img[row, col] = 255
                else:
                    bin_img[row, col] = 0

        return bin_img


