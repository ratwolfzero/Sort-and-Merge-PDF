import os
from pypdf import PdfWriter
 
# Directory containing PDF files
directory = r"/Users/ralf/Downloads"
 
# Initialize PdfWriter
merger = PdfWriter()
 
# Get and sort the list of PDF files in the directory (case-insensitive)
pdf_files = sorted([f for f in os.listdir(directory) if f.endswith(".pdf")], key=str.lower)
 
# Loop through each sorted PDF file
for filename in pdf_files:
    file_path = os.path.join(directory, filename)
    print(f"Adding: {file_path}")
    merger.append(file_path)
 
# Output file name
output_path = os.path.join(directory, "finalFile.pdf")
 
# Write the merged PDF to the output file
merger.write(output_path)
merger.close()
 
print(f"PDF files merged successfully into {output_path}")
