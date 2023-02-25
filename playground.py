import cv2
import pytesseract as pytsa

img = cv2.imread('images/529s.jpg', cv2.IMREAD_GRAYSCALE)

def show_image(img):
    try:
        cv2.imshow('derp', img)
        cv2.startWindowThread()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)

#           h     w
box1 = img[78:97,62:93]

show_image(box1)

# text = pytsa.image_to_string(box1)
# print(text)