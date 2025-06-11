import sys
import PyPDF2
import pyfiglet

Title= pyfiglet.figlet_format("FDF PROTECTION TOOL")
print(Title)

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def create_password_protector_pdf(input_pdf, out_pdf, password):
    try:
        with open(input_pdf, 'rb') as f1:
            pdf_reader = PyPDF2.PdfReader(f1)
            pdf_writer = PyPDF2.PdfWriter()
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
            pdf_writer.encrypt(password)
            with open(out_pdf, 'wb') as f2:
                pdf_writer.write(f2)
            print(f'{GREEN}password-protected PDF file saved as {out_pdf}{RESET}\n')
    except FileNotFoundError:
        print(f'{RED}the file {input_pdf} was not found.{RESET}\n')

def main():
    if len(sys.argv) != 4:
        print(f"{RED}Usage: python3 script.py <input_pdf> <output_pdf> <password>{RESET}\n")
        sys.exit(1)
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    create_password_protector_pdf(input_pdf, output_pdf, password)

if __name__== "__main__":
    main()
