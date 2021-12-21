import cv2
from images import img_path

if __name__ == '__main__':
    img = cv2.imread(img_path('statue_small.jpg'), 0)
    cv2.imshow('img', img)
    cv2.imshow('canny', cv2.Canny(img, 200, 300))
    cv2.waitKey()
    cv2.destroyAllWindows()