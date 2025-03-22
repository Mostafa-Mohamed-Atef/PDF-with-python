import aspose.pdf as ap
import os

def pdf_to_latex(filepath):
    # Clean the filepath by removing quotes and converting to absolute path
    filepath = filepath.strip().strip('"\'')
    filepath = os.path.abspath(filepath)

    # Open PDF file
    document = ap.Document(filepath)

    # Create an object of LaTeXSaveOptions class
    saveOptions = ap.LaTeXSaveOptions()

    # Save PDF as TEX
    document.save("output.tex", saveOptions)

    
if __name__ == "__main__":
    filepath = input("File path: \n")
    pdf_to_latex(filepath)