# Import necessary libraries for FastAPI, file handling, OCR, and templating
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import easyocr  # OCR library for text extraction from images
import re  # Regular expressions for pattern matching
import os  # File and directory handling

# Create FastAPI application instance
app = FastAPI()

# Mount a static directory to serve files like images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates for rendering HTML pages
templates = Jinja2Templates(directory="templates")

# Root endpoint to render the upload HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

# POST endpoint to handle image upload and OCR processing
@app.post("/upload/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    # Save uploaded image to the 'static' directory
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())  # Write the file content to the specified location

    # Initialize EasyOCR reader for English language
    reader = easyocr.Reader(['en'])
    result = reader.readtext(file_location, detail=0)  # Perform OCR on the image and extract text
    extracted_text = '\n'.join(result)  # Join the extracted text into a single string

    # Improved regex pattern to capture variations of the word "Total" and the amount
    total_amount_match = re.search(
        r"(?:total\s*(?:achats)?|grand\s*total|t[\s\W]*o[\s\W]*t[\s\W]*a[\s\W]*l)\s*[:$-]?\s*(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)",
        extracted_text,
        re.IGNORECASE  # Case insensitive matching
    )
    total_amount = total_amount_match.group(1) if total_amount_match else "Amount not found"

    # Render a success page with the extracted text and total amount
    return templates.TemplateResponse("success.html", {
        "request": request,
        "filename": file.filename,  # Return the filename of the uploaded image
        "extracted_text": extracted_text,  # Display the extracted text from the image
        "total_amount": total_amount  # Display the found total amount or a message
    })
