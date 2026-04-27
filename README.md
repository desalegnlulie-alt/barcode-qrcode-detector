# Automated Barcode and QR Code Detection System 📷🔍

An optical machine-readable data extraction tool built with Python, OpenCV, and PyZbar. This project was developed as a group project for the **Introduction to Computer Vision** course at **Addis Ababa Science and Technology University (AASTU)**.

## 🎯 Project Objective
The primary goal of this project is to develop a robust, real-time application capable of detecting, localizing, and decoding both linear barcodes (such as Code-128) and complex QR codes using a standard computer webcam. This eliminates the need for expensive, specialized laser-scanning hardware.

## 🛠️ Core Technologies
* **Python:** The primary programming environment and backbone of the application logic.
* **OpenCV (Open Source Computer Vision):** Utilized for essential spatial domain filtering, matrix manipulations, and real-time bounding box rendering.
* **PyZbar:** Advanced mathematical algorithms used to locate the precise geometric coordinates of the code, extract the binary payload, and translate it into a human-readable format.

## ✨ Key Features
* **Real-Time Detection:** Asynchronous video stream processing with zero perceptible lag.
* **Moiré Effect Mitigation:** Uses a customized pre-processing pipeline (including 5x5 Gaussian Blurring) to eliminate digital screen distortion when scanning codes directly from smartphone screens.
* **Dynamic Spatial Localization:** Draws a dynamic, 4-pixel thick green bounding box around moving targets in real-time.
* **Hardware Optimization:** Maintains webcam hardware at its fast native resolution to prevent CPU bottlenecking, while mathematically upscaling the display window for a better User Experience (UX).

## ⚙️ How It Works (The Pipeline)
Our system feeds raw video into a 3-stage pre-processing pipeline before decoding:
1. **Video Capture:** Captures native resolution frames.
2. **Grayscale Conversion:** Reduces data by 66% (since barcodes are inherently black and white), optimizing processing speed.
3. **Gaussian Blurring:** Acts as a low-pass filter to erase high-frequency pixel grids (Moiré effect) from digital screens.
4. **PyZbar Decoding:** Searches the optimized matrix for recognized structural patterns.
5. **Rendering:** Overlays bounding boxes and decoded UTF-8 text onto the live feed.

## 🚀 Installation and Setup

**1. Clone the repository:**
git clone https://github.com/yourusername/barcode-qrcode-detector.git
cd barcode-qrcode-detector

**2. Install the required libraries:**
Make sure you have Python installed. Then run:
pip install opencv-python pyzbar

*(Note for Mac/Linux users: You might need to install the zbar shared library via "brew install zbar" or "sudo apt-get install libzbar0")*

**3. Run the application:**
python detector.py

*(Press 'q' to quit the webcam window).*
