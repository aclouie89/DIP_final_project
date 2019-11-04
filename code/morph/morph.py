def open(image, threshold, window):
  return image

def close(image, threshold, window):
  return image

def erosion(image, threshold, window):
  return image

def dilation(image, threshold, window):
  return image

def setWindow(matrix, row_index, col_index):
  matrix[row_index][col_index] = 1
  return matrix

def setPlusWindow(window):
  # window = setWindow(window, 1,0 )
  # window = setWindow(window, 1,1 )
  # window = setWindow(window, 1,2 )
  # window = setWindow(window, 0,1 )
  # window = setWindow(window, 2,1 )
  return window