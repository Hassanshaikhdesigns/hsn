🚗 License Plate Detection & Recognition using OpenCV and EasyOCR

This project detects a vehicle license plate from an image using OpenCV and extracts the license number using EasyOCR.

📌 Features

Detects license plates using contour detection

Automatically crops the detected plate

Enhances image quality for better OCR accuracy

Extracts text from the license plate using EasyOCR

Displays the detected license plate image

🛠️ Technologies Used

Python 3

OpenCV

EasyOCR

NumPy

Matplotlib

📂 Project Structure
project/
│
├── test_images/
│   └── car.jpg
│
├── license_plate_detection.py
├── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/license-plate-ocr.git
cd license-plate-ocr

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv


Activate the environment:

Linux / macOS

source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install Required Dependencies
pip install opencv-python easyocr matplotlib numpy


⚠️ Note: EasyOCR may take a few seconds to load models on the first run.

▶️ How to Run the Project

Place your test image inside the test_images folder
Example:

test_images/car.jpg


Run the script:

python license_plate_detection.py

✅ Output

Prints detected license plate text in the terminal

Displays the cropped license plate image

Example Output:

✅ Detected Text:
MH12AB1234

🧠 How It Works

Converts the image to grayscale

Applies bilateral filtering and edge detection

Finds contours and selects a rectangular contour

Crops the license plate area

Enhances the image using thresholding

Extracts text using EasyOCR

❌ Common Issues

Image not found → Check the image path

No license plate detected → Use clear, front-facing vehicle images

Poor OCR results → Try higher resolution images

📌 Future Improvements

Support for video streams

Deep learning-based plate detection (YOLO)

Multi-language license plate support

Real-time camera detection

📜 License

This project is for educational purposes only.
