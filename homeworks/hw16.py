import shutil
from pathlib import Path
import cv2


def prepare_scan(path):
    gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("scan.png", binary)


def make_avatar(path):
    image = cv2.imread(path)
    h, w = image.shape[:2]
    side = min(h, w)
    y, x = (h - side) // 2, (w - side) // 2
    avatar = cv2.resize(
        image[y : y + side, x : x + side], (250, 250), interpolation=cv2.INTER_AREA
    )
    cv2.imwrite("avatar.png", avatar)


def check_image(path):
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    h, w = image.shape[:2]
    channels = image.shape[2] if image.ndim == 3 else 1
    if channels != 3 or w < 800 or h < 600:
        print(
            f"Error: {w}x{h}, {channels} channel(s); need 3 channels and at least 800x600"
        )
        return
    Path("processed").mkdir(exist_ok=True)
    shutil.copy2(path, "processed")


def main():
    prepare_scan("./assets/scan.png")
    make_avatar("./assets/avatar.jpg")
    check_image("./assets/check.jpg")


if __name__ == "__main__":
    main()
