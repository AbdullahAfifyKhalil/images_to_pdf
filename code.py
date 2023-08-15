import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt
from PIL import Image

class ImageToPDFConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.btn_select_folder = QPushButton('Select Images Folder', self)
        self.lbl_folder_path = QLabel('Folder Path:', self)
        self.txt_output_pdf = QLineEdit('output.pdf', self)
        self.btn_convert = QPushButton('Convert to PDF', self)
        self.lbl_status = QLabel('', self)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_select_folder)
        layout.addWidget(self.lbl_folder_path)
        layout.addWidget(QLabel('Output PDF Name:'))
        layout.addWidget(self.txt_output_pdf)
        layout.addWidget(self.btn_convert)
        layout.addWidget(self.lbl_status)

        self.setLayout(layout)

        # Connect signals
        self.btn_select_folder.clicked.connect(self.select_folder)
        self.btn_convert.clicked.connect(self.convert_to_pdf)

        # Window settings
        self.setWindowTitle('Image to PDF Converter')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.show()

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Image Folder')
        if folder_path:
            self.lbl_folder_path.setText(f'Folder Path: {folder_path}')

    def convert_to_pdf(self):
        folder_path = self.lbl_folder_path.text().replace('Folder Path: ', '')
        if not folder_path:
            self.lbl_status.setText('Please select an image folder.')
            return

        output_pdf = self.txt_output_pdf.text().strip()
        if not output_pdf:
            self.lbl_status.setText('Please specify the output PDF name.')
            return

        # Convert images to PDF
        try:
            self.images_to_pdf(folder_path, output_pdf)
            self.lbl_status.setText(f'Successfully converted images in {folder_path} to {output_pdf}.')
        except Exception as e:
            self.lbl_status.setText(f'Error: {e}')

    def images_to_pdf(self, image_folder, output_pdf, page_size=(595, 842)):
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # Custom sort function that takes numbers in the filenames into account
        image_files.sort(key=lambda f: [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', f)])

        images = []

        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = Image.open(image_path)
            image = image.convert('RGB')
            image = image.resize(page_size, Image.ANTIALIAS)
            images.append(image)

        if images:
            images[0].save(output_pdf, save_all=True, append_images=images[1:])
        else:
            raise Exception("No images found in the folder.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageToPDFConverter()
    sys.exit(app.exec_())
