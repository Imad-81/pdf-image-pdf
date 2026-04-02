# PDF to Image-PDF Converter

A Python script that takes a standard PDF file, converts each page into a JPEG image, and compiles those images back into a new PDF file. This essentially flattens the PDF, turning all text, shapes, and vectors into a rasterized image array.

## Prerequisites

You need to have `PyMuPDF` and `Pillow` installed. They can be installed via pip:

```bash
pip install PyMuPDF Pillow
```

## Usage

You can run the script from your terminal:

```bash
python main.py <input_pdf>
```

**Options:**

- `--dpi`: Sets the DPI (resolution) of the generated JPEG images. The default value is `300`.

### Example

Convert a PDF with the default 300 DPI resolution:
```bash
python main.py my_document.pdf
```

Convert a PDF using a lower 150 DPI resolution for a smaller file size:
```bash
python main.py my_document.pdf --dpi 150
```
