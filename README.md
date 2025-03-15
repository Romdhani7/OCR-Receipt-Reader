# 📄 OCR Receipt Reader

## Purpose
The purpose of this project is to develop a web application that helps users extract important data from receipt images using Optical Character Recognition (OCR). The app enables the upload of receipt images, processes them to extract text, and automatically detects the total amount on the receipt, displaying it along with the extracted text for easy reference.

This is especially useful for automating receipt management, such as tracking expenses, organizing purchases, or digitizing paper-based receipts for further analysis.

## Features
- **Receipt Image Upload**: Users can upload receipt images through a simple web interface.
- **Text Extraction via OCR**: The EasyOCR library extracts all text content from the uploaded receipt.
- **Total Amount Detection**: A regular expression detects and highlights the total amount from the receipt (e.g., "Total", "Grand Total").
- **Dynamic HTML Interface**: The app renders HTML pages using FastAPI's templating engine (Jinja2), showing extracted text and total amounts.

## Technologies Used
- **FastAPI**: A modern, fast web framework used to build the API and handle requests.
- **EasyOCR**: A powerful OCR library used to recognize and extract text from receipt images.
- **Jinja2**: A templating engine for rendering dynamic HTML pages.
- **HTML/CSS**: Used to style and create user-friendly pages for image uploads and result displays.

## Installation

1. Clone the repository:
**********************************************************************************
   git clone https://github.com/yourusername/ocr-receipt-reader.git
   cd ocr-receipt-reader
**********************************************************************************   
## Running the Project
Run the app using the following command:
**********************************************************************************
uvicorn main:app --reload
**********************************************************************************
Once the server is running, open your browser and navigate to http://127.0.0.1:8000/ to start uploading receipt images.

## How It Works
Receipt Image Upload: Users upload a receipt image using a simple form in the web interface.
OCR Text Extraction: The uploaded image is processed by EasyOCR, extracting any readable text from the receipt.
Total Amount Detection: A regex pattern searches the extracted text for total amounts (like "Total", "Grand Total").
Result Display: The extracted text and total amount (if found) are displayed on a result page.

## Example of Input and Output
After uploading a receipt image, the application will extract and display all the text from the receipt. If a total amount is found, it will be highlighted on the result page.

## Example Output:
The app will display the following on the result page:
**********************************************************************************
Extracted Text:
Receipt #5678
Items:
- Item 1: $3.50
- Item 2: $4.25
- Item 3: $2.75
Grand Total: $10.50

Total Amount: $10.50
**********************************************************************************
