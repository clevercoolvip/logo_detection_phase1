import cv2
from script5_fg_bg import get_bg

def overlay_rgba_on_rgb(logoFilePath, rgb_template_path, outputFolder, x=0, y=0):
    rgba_overlay = get_bg(logoFilePath)
    rgb_image = cv2.imread(rgb_template_path)
    # rgba_overlay = cv2.imread(rgba_overlay_path, -1)
    overlay_alpha = rgba_overlay[:, :, 3] / 255.0  # Normalize alpha channel (0.0 - 1.0)

    # Convert RGB image to BGRA (for compatibility with OpenCV functions)
    bgra_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2RGBA)
    # Use alpha blending to combine the images
    for c in range(3):
        bgra_image[:80, :80, c] = (1 - overlay_alpha) * bgra_image[:80, :80, c] + overlay_alpha * rgba_overlay[:, :, c]

    # Convert back to RGB if desired
    rgb_image_with_overlay = cv2.cvtColor(bgra_image, cv2.COLOR_RGBA2RGB)
    cv2.imwrite(outputFolder, rgb_image_with_overlay)
    return rgb_image_with_overlay




if __name__=="__main__":
    result_image = overlay_rgba_on_rgb("formatTemplates/1.PNG", "noBGOutput/test.png", "static/generatedTemplates/output__1.png", x=5, y=5)

    # Display or save the result
    cv2.imshow("Image with Overlay", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
