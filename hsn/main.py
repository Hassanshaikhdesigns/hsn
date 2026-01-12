import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Load image
# -----------------------------
image_path = "test_images/car.jpg"
img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found")
    exit()

# -----------------------------
# Preprocessing
# -----------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 11, 17, 17)
edges = cv2.Canny(blur, 30, 200)

# -----------------------------
# Find contours
# -----------------------------
contours, _ = cv2.findContours(
    edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
plate_contour = None

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.018 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        plate_contour = approx
        break

if plate_contour is None:
    print("❌ No license plate detected")
    exit()

# -----------------------------
# Crop license plate
# -----------------------------
x, y, w, h = cv2.boundingRect(plate_contour)
plate = img[y:y+h, x:x+w]

# -----------------------------
# Improve OCR readability
# -----------------------------
plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
plate_gray = cv2.resize(plate_gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
_, plate_thresh = cv2.threshold(
    plate_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# -----------------------------
# OCR
# -----------------------------
reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext(plate_thresh)

print("✅ Detected Text:")
for res in results:
    print(res[1])

# -----------------------------
# Show result
# -----------------------------
plt.figure(figsize=(6, 3))
plt.imshow(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB))
plt.title("Detected License Plate")
plt.axis("off")
plt.show()
