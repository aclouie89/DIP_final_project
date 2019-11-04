class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        # Jiahui Li 1809871
        # COSC6380 9/18/2019
        # hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist = [0]*256

        # Calculate the intensity of each pixel and store them in the hist array
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                intensity = image[x][y]
                hist[intensity] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold, flag = 128, True
        p = [0] * 256

        # Find the optimal threshold value
        while(flag):
            sum1, sum2, u1, u2 = 0, 0, 0, 0
            # Calculate the sum
            for i in range(threshold):
                sum1 += hist[i]
            for i in range(threshold, 256):
                sum2 += hist[i]

            # Calculate the probability
            for i in range(threshold):
                p[i] = hist[i] / sum1
            for i in range(threshold, 256):
                p[i] = hist[i] / sum2

            # Calculate the expectation
            for i in range(threshold):
                u1 += i * p[i]
            for i in range(threshold, 256):
                u2 += i * p[i]

            # Calculate the threshold: if it is not the optimal threshold, calculate again
            if (threshold != round((u1 + u2) / 2)):
                threshold = round((u1 + u2) / 2)
            else:
                flag = False

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        # Create an object to call functions to find the optimal threshold
        obj = binary_image()
        threshold = obj.find_optimal_threshold(obj.compute_histogram(image))

        # March each pixel, if the intensity is less than threshold,
        # use 255 instead of original value. Otherwise, use 0.
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                if(bin_img[x][y] <= threshold):
                    bin_img[x][y] = 255
                else:
                    bin_img[x][y] = 0

        return bin_img