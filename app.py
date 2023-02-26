# app.py
import cv2                      # pip3 install opencv-python
import pytesseract as pytsa     # pip3 install pyTesseract

img = cv2.imread('images/529s.jpg', cv2.IMREAD_GRAYSCALE)

# Lines that divide the image vertically
y_lines = [ 1, 32, 62, 93, 123, 153, 184, 214, 245, 275, 306 ]
# Lines that divide the image horizontally
x_lines = [ 1, 20, 39, 58, 78, 97, 116, 135, 153, 173, 
            192, 211, 230, 250, 268, 288, 307, 326, 345, 
            364, 384, 403, 422, 441, 460 ]

## Just some math code I wrote to confirm how many slices I would
## end up "reading" with Tesseract
# 275 squares
len_x_lines = len(x_lines) # 0 - 24
len_y_lines = len(y_lines) # 0 - 10
total_squares = len_y_lines * len_x_lines
# print(f"Total squares: {total_squares} with ylines [{len_y_lines}] and xlines [{len_x_lines}]")

def show_image(img):
    ''' show_image() - A function that will open the image with OpenCV and disappear after a key press.
        Pro-tip: Don't use this with JuPyter. It will hang endlessly. 
    '''
    try:
        cv2.imshow('derp', img)
        cv2.startWindowThread()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)


tiles = []
for i, x in enumerate(x_lines):
    # If we've hit the 25th x index, break out of the loop.
    if i == 24: break
    
    # Define the left and right positions
    left, right = x, x_lines[i+1]

    for i, y in enumerate(y_lines):
        # If we've hit the 10th y index, break out of the loop.
        if i == 10: break

        # Define the top and bottom positions.
        top, bottom = y, y_lines[i+1]
        
        # Bam! Now we have a tile. Let's add it to our master "tiles" list. 
        tiles.append([(left, right), (top, bottom)])


for tile in tiles:
    # Define the area and position of the tile in the main image
    # by calling out two array ranges within the main OpenCV image data
    # - the format is like this:      h , w   where h = height, w = width
    #                            img[x:y,x:y]
    slice = img[tile[0][0]:tile[0][1],tile[1][0]:tile[1][1]]
    
    # Now let's try to read that data with Tesseract!
    #
    # Tesseract was giving me newline characters, so let's replace them
    # with an empty string.
    ocrtext = pytsa.image_to_string(slice).replace("\n", "")

    # Since "529" is the known number in the puzzle, we're going to only
    # print out text that doesn't match "529"
    if ocrtext != "529":
        print(ocrtext)

    # Uncomment to debug for any tiles tesseract can't extract text.
    # I mainly used this for fine tuning of the colum and row positions.
    #
    # if ocrtext == "":
    #     print(f"{tile[0][0]}:{tile[0][1]},{tile[1][0]}:{tile[1][1]}")

