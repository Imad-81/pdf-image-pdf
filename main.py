import sys
import argparse
import io

try:
    import fitz  # PyMuPDF
    from PIL import Image
except ImportError:
    print("Error: Missing required libraries.")
    print("Please install them using: pip install PyMuPDF Pillow")
    sys.exit(1)


def convert_pdf_to_image_pdf(input_path, output_path, dpi=300):
    """
    Converts a normal PDF to an image-based PDF where each page is a JPEG image.
    """
    try:
        # Open the input PDF
        pdf_document = fitz.open(input_path)
        print(f"Opened '{input_path}' (Pages: {len(pdf_document)})")
    except Exception as e:
        print(f"Error opening '{input_path}': {e}")
        sys.exit(1)

    images = []
    
    # Calculate matrix for desired DPI (default PyMuPDF resolution is 72 DPI)
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    
    for page_num in range(len(pdf_document)):
        print(f"Processing page {page_num + 1}/{len(pdf_document)}...")
        page = pdf_document.load_page(page_num)
        
        # Render page to a pixmap (image)
        # alpha=False ensures the background is white instead of transparent
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        # Convert pixmap to JPEG bytes, then load into a PIL Image
        img_data = pix.tobytes("jpeg")
        img = Image.open(io.BytesIO(img_data)).convert('RGB')
        images.append(img)
        
    pdf_document.close()
    
    if images:
        print(f"Saving output to '{output_path}'...")
        # Save the first image as a PDF and append the rest
        images[0].save(
            output_path,
            "PDF",
            save_all=True,
            append_images=images[1:],
            resolution=float(dpi)
        )
        print("Done successfully!")
    else:
        print("No pages found in the input PDF.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a normal PDF into a PDF containing only JPEG images.")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_pdf", help="Path for the output PDF file")
    parser.add_argument("--dpi", type=int, default=300, help="Resolution in DPI for the output images (default: 300)")
    
    args = parser.parse_args()
    convert_pdf_to_image_pdf(args.input_pdf, args.output_pdf, args.dpi)
