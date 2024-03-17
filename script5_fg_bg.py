import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_bg(filename):
    img = cv2.imread(filename)

    mask = np.zeros(img.shape[:2], dtype='uint8')

    rect = (0, 0, img.shape[0]-1, img.shape[1]-1)
    fgModel = np.zeros((1, 65), dtype="float")
    bgModel = np.zeros((1, 65), dtype="float")

    (mask, bgModel, fgModel) = cv2.grabCut(img, mask, rect, bgModel, fgModel, iterCount=10, mode=cv2.GC_INIT_WITH_RECT)

    values = (
        ("Definite background", cv2.GC_BGD),
        ("Probable background", cv2.GC_PR_BGD),
        ("Definite background", cv2.GC_FGD),
        ("Probable background", cv2.GC_PR_BGD),
    )

    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
    outputMask = (outputMask * 255).astype("uint8")
    output = cv2.bitwise_and(img, img, mask=outputMask)

    cv2.imwrite(f"output/only_logo_{filename.split('.')[0]}.png", output)
    print(output.shape)

    return output

if __name__=="__main__":
    output = get_bg("logo33.png")
    cv2.imshow("Before", output)
    cv2.waitKey(0)