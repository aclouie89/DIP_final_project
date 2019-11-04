__author__ = "Jiahui Li"
__email__ = "lijiahui702@gmail.com"
__version__ = "1.0.0"

import cv2
import sys
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from region_analysis import binary_image as bi
from region_analysis import morphology as mor

def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def main():
    """ The main function that parses input arguments, calls the appropriate
    interpolation method and writes the output image"""
    # Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-m", "--morphology", dest="morphology",
                        help="specify the morphology method (dialte, erode, open, or close)",
                        metavar="MORPHOLOGY METHOD")
    parser.add_argument("-w", "--window", dest="window",
                        help="specify the window size", metavar="WINDOW")

    args = parser.parse_args()

    # Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    # Check morphology method argument
    if args.morphology is None:
        print("Morphology method not specified, using default=dilate")
        print("use the -h option to see usage information")
        morphology = "dilate"
    else:
        if args.morphology not in ["dilate", "erode", "open", "close"]:
            print("Invalid morphology method, using default=dilate")
            print("use the -h option to see usage information")
            morphology = "dilate"
        else:
            morphology = args.morphology

    # Check window size argument
        if args.window is None:
            print("Window size not specified, using default=0")
            print("use the -h option to see usage information")
            window = "0"
        else:
            if args.window not in ["0", "1"]:
                print("Invalid window size, using default=0")
                print("use the -h option to see usage information")
                window = "0"
            else:
                window = args.window


    bin_img = bi.binary_image()
    hist = bin_img.compute_histogram(input_image)

    outputDir = 'output/'

    # Saving histogram to output directory
    hist_fig = plt.plot(hist)
    plt.savefig(outputDir+"hist.png")

    threshold = bin_img.find_optimal_threshold(hist)
    print("Optimal threshold: ", threshold)

    binary_img = bin_img.binarize(input_image)
    output_image_name = outputDir + "binary_image_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(output_image_name, binary_img)

    # Morphology
    mor_obj = mor.morphology()

    if morphology == "dilate":
        # dilation
        dilation_img = mor_obj.dilate(binary_img, window)
        output_image_name = outputDir + "dilation_image_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, dilation_img)
    elif morphology == "erode":
        # erosion
        erosion_img = mor_obj.erode(binary_img, window)
        output_image_name = outputDir + "erosion_image_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, erosion_img)
    elif morphology == "open":
        # opening
        opening_img = mor_obj.open(binary_img, window)
        output_image_name = outputDir + "opening_image_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, opening_img)
    elif morphology == "close":
        # closing
        closing_img = mor_obj.close(binary_img, window)
        output_image_name = outputDir + "closing_image_" + datetime.now().strftime("%m%d-%H%M%S") + ".jpg"
        cv2.imwrite(output_image_name, closing_img)


if __name__ == "__main__":
    main()