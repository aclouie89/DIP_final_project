import cv2
import numpy as np

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()

        # Create a new image img_count to replicate the first row and
        # first column, then copy the original image to the new image
        img_count = np.zeros((image.shape[0]+1, image.shape[1]+1), np.uint8)
        for x in range(image.shape[0]+1):
            for y in range(image.shape[1]+1):
                if x == 0 or y == 0:
                    continue
                else:
                    img_count[x][y] = image[x-1][y-1]

        # Define a "region color" r, r[i][j] = region number of pixel i[i][j]
        # k = region number counter
        r = np.zeros((image.shape[0]+1, image.shape[1]+1))
        k = 1

        # Blob coloring Algorithm
        for y in range(1, img_count.shape[1]):
            for x in range(1, img_count.shape[0]):
                if img_count[x][y] == 255 and img_count[x][y-1] == 0 and img_count[x-1][y] == 0:
                    r[x][y] = k

                    if k in regions.keys():
                        regions[k].append([x - 1, y - 1])
                    else:
                        regions[k] = [[x - 1, y - 1]]

                    k += 1
                elif img_count[x][y] == 255 and img_count[x][y-1] == 0 and img_count[x-1][y] == 255:
                    r[x][y] = r[x-1][y]
                    # if r[x-1][y] in regions.keys():
                    regions[(r[x-1][y])].append([x - 1, y - 1])
                    # else:
                    #     regions[r[x-1][y]] = [[x - 1, y - 1]]

                elif img_count[x][y] == 255 and img_count[x][y-1] == 255 and img_count[x-1][y] == 0:
                    r[x][y] = r[x][y-1]
                    # if r[x][y-1] in regions.keys():
                    regions[r[x][y-1]].append([x - 1, y - 1])
                    # else:
                    #     regions[r[x][y-1]] = [[x - 1, y - 1]]

                elif img_count[x][y] == 255 and img_count[x][y-1] == 255 and img_count[x-1][y] == 255:
                    r[x][y] = r[x][y-1]
                    regions[r[x][y - 1]].append([x - 1, y - 1])
                    if r[x][y-1] != r[x-1][y]:
                        # print(r[x][y-1],r[x-1][y])
                        #print(r[regions[r[x-1][y]]] )
                        delete_reg = r[x-1][y]
                        # print("-----------",delete_reg)
                        # for pix in regions[r[x-1][y]]:
                        #     print("o", r[pix[0]+1][pix[1]+1])
                        for pix in regions[r[x-1][y]]:
                            # print("k",pix)
                            # print("pix", r[pix])
                            r[pix[0]+1][pix[1]+1] = r[x][y - 1]
                        # for pix in regions[r[x - 1][y]]:
                        #     print("c", r[pix[0]+1][pix[1]+1])
                        # exit()
                        #r[regions[r[x-1][y]]] = r[x][y-1]
                        #print("...............",r[regions[r[x-1][y]]])
                        regions[r[x][y - 1]].extend(regions[r[x - 1][y]])
                        # if r[x][y-1] in regions.keys():
                        #     regions[r[x][y-1]].extend(regions[r[x-1][y]])
                        # else:
                        #     regions[r[x][y-1]] = regions[r[x-1][y]]
                        # print("delete", r[x-1][y])
                        del regions[delete_reg]
                        # print(r[r==delete_reg])
                        # for i in range(len(regions(r[x-1][y]])):
                        #     r[regions(r[x-1][y][i][0]][regions(r[x-1][y][i][1]] = r[x-1][y]

        return regions



    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        stats = dict()

        #  Generate a report of the remaining cells and print out
        index = 1
        for k in region:
            # Initialize the min and max to calculate the centroid
            x_min, x_max, y_min, y_max, x_center, y_center = 1e9, 0, 1e9, 0, 0, 0
            # Ignore cells smaller than 15 pixels in area
            if len(region[k]) >= 15:
                # Calculate the centroid coordinates
                for i in range(len(region[k])):
                    x_min = min(x_min, region[k][i][0])
                    x_max = max(x_max, region[k][i][0])
                    y_min = min(y_min, region[k][i][1])
                    y_max = max(y_max, region[k][i][1])
                x_center = int(x_min + (x_max - x_min) / 2. + .5)
                y_center = int(y_min + (y_max - y_min) / 2. + .5)
                centroid = [x_center, y_center]
                # print(region[k])
                # print(x_min, x_max, y_min, y_max)
                # print(centroid)
                # # exit()

                # print(x_min, x_max, y_min, y_max, x_center, y_center)
                # print("region", k, "\n", region[k])
                # print(centroid1)
                # print(region[k][0])
                # print(len(region[k]))

                # centroid = region[k][round(len(region[k]) / 2.)]
                # print("centroid2:\n", centroid2)


                # Set keys and values to the stats
                stats[index] = (centroid, len(region[k]))
                index += 1
        # for x, y in stats.items():
        #     print(x, y)
        return stats



    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        output_image = image.copy()

        for x, y in stats.items():
            # string = str(x) + "\n" + str(y[1])
            # print(string)
            # print(stats[k])
            # print(stats[k][0])
            # print(stats[k][1])
            # print("x",stats[k][0][0])
            # print("y",stats[k][0][1])
            cv2.putText(output_image, "*", (y[0][1], y[0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.3, 0)
            cv2.putText(output_image, str(x), (y[0][1], y[0][0]+6), cv2.FONT_HERSHEY_COMPLEX, 0.3, 200)
            cv2.putText(output_image, str(y[1]), (y[0][1], y[0][0]+12), cv2.FONT_HERSHEY_COMPLEX, 0.2, 200)

        return output_image