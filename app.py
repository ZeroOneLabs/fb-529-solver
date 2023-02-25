# app.py
import cv2                      # pip3 install opencv-python
import pytesseract as pytsa     # pip3 install pyTesseract

img = cv2.imread('images/529s.jpg', cv2.IMREAD_GRAYSCALE)

# Lines that divide the image vertically
y_lines = [1, 32, 62, 93, 123, 153, 184, 214, 245, 275, 306]
# Lines that divide the image horizontally
x_lines = [1, 20, 39, 58, 78, 97, 116, 135, 153, 173, 192, 211, 230, 250, 268, 288, 307, 326, 345, 364, 384, 403, 422, 441, 460]

# 275 squares
len_x_lines = len(x_lines) # 0 - 24
len_y_lines = len(y_lines) # 0 - 10
total_squares = len_y_lines * len_x_lines

# print(f"Total squares: {total_squares} with ylines [{len_y_lines}] and xlines [{len_x_lines}]")

def show_image(img):
    try:
        cv2.imshow('derp', img)
        cv2.startWindowThread()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)


tiles = []
for i, x in enumerate(x_lines):
    # If we've hit the 25th index, break out of the loop.
    if i == 24:
        break
    
    # Define the left and right sides of the tile
    left = x
    right = x_lines[i+1]

    for i, y in enumerate(y_lines):
        if i == 10:
            break
        top = y
        bottom = y_lines[i+1]
        
        tiles.append(
            [(left, right), (top, bottom)]
        )


for tile in tiles:
    slice = img[tile[0][0]:tile[0][1],tile[1][0]:tile[1][1]]
    ocrtext = pytsa.image_to_string(slice).replace("\n", "")

    # Since "529" is the known number in the puzzle, we're going to only
    # print out text that doesn't match "529"
    if ocrtext != "529":
        print(ocrtext)

    # Uncomment to debug for any tiles tesseract can't extract text.
    #
    # if ocrtext == "":
    #     print(f"{tile[0][0]}:{tile[0][1]},{tile[1][0]}:{tile[1][1]}")

