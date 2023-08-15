# images_to_pdf
A simple Python script with Gui to take all the images of a specific folder and convert them to one pdf file with images in order and the images take the full page view.

Image to PDF Converter
Introduction
The Image to PDF Converter is a simple PyQt5-based GUI application that allows users to select a folder containing images and convert them into a single PDF file. The application supports various image formats including PNG, JPEG, BMP, GIF, TIFF, HEIF, and HEIC.

Requirements
Python 3.x
PyQt5
PIL (Pillow)
pyheif
You can install the required packages using the following command:

bash
Copy code
pip install PyQt5 Pillow pyheif
Usage
Select Images Folder: Click the "Select Images Folder" button to choose a folder containing images that you want to convert to a PDF.
Specify Output PDF Name: Enter the desired name for the output PDF file in the text field.
Convert to PDF: Click the "Convert to PDF" button to start the conversion process. The status of the conversion will be displayed below the button.
Code Overview
ImageToPDFConverter class: The main class that creates the GUI and handles the conversion process.
init_ui method: Sets up the layout and widgets for the application.
select_folder method: Opens a dialog for selecting the folder containing the images.
convert_to_pdf method: Controls the process of converting the images to a PDF.
images_to_pdf method: Responsible for reading, resizing, and converting the images to a PDF.
Customization
Page Size: The default page size for the PDF is A4 (595, 842). You can change the page_size parameter in the images_to_pdf method to set a custom page size.
