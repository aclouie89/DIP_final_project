import numpy as np

WIN_BAR = 0
WIN_PLUS = 1

def dilate(image, window):
    # Padding
    original = np.zeros((image.shape[0]+2, image.shape[1]+2), np.uint8)
    # Copy image information
    for x in range(1, image.shape[0]+1):
        for y in range(1, image.shape[1]+1):
            original[x][y] = image[x-1][y-1]

    # Dilation
    output = original.copy()
    if window == WIN_BAR:
        for x in range(1, image.shape[0] + 1):
            for y in range(1, image.shape[1] + 1):
                output[x][y] = output[x][y] or original[x][y-1]
                output[x][y] = output[x][y] or original[x][y+1]
    else:
        for x in range(1, image.shape[0] + 1):
            for y in range(1, image.shape[1] + 1):
                output[x][y] = output[x][y] or original[x][y-1]
                output[x][y] = output[x][y] or original[x][y+1]
                output[x][y] = output[x][y] or original[x-1][y]
                output[x][y] = output[x][y] or original[x+1][y]

    # Remove padding
    oImg = image.copy()
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            oImg[x][y] = output[x+1][y+1]

    return oImg

def erode(image, window):
    # Padding
    original = np.zeros((image.shape[0] + 2, image.shape[1] + 2), np.uint8)
    # Copy image information
    for x in range(1, image.shape[0] + 1):
        for y in range(1, image.shape[1] + 1):
            original[x][y] = image[x - 1][y - 1]

    # Erosion
    output = original.copy()
    if window == WIN_BAR:
        for x in range(1, image.shape[0] + 1):
            for y in range(1, image.shape[1] + 1):
                output[x][y] = output[x][y] and original[x][y - 1]
                output[x][y] = output[x][y] and original[x][y + 1]
    else:
        for x in range(1, image.shape[0] + 1):
            for y in range(1, image.shape[1] + 1):
                output[x][y] = output[x][y] and original[x][y - 1]
                output[x][y] = output[x][y] and original[x][y + 1]
                output[x][y] = output[x][y] and original[x - 1][y]
                output[x][y] = output[x][y] and original[x + 1][y]

    # Remove padding
    oImg = image.copy()
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            oImg[x][y] = output[x + 1][y + 1]

    return oImg


def open(image, window):
    oImg = erode(image, window)
    oImg = dilate(oImg, window)

    return oImg


def close(image, window):
    oImg = dilate(image, window)
    oImg = erode(oImg, window)

    return oImg