import logging
import os
from markdown2 import markdown  
from weasyprint import HTML
from tempfile import NamedTemporaryFile  

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='pdf_generator.log',  
                    format='%(asctime)s - %(levelname)s - %(message)s')  

class PDFGenerator:
    def __init__(self, markdown_file):
        self.markdown_file = markdown_file
        self.output_file = None

    def md2pdf(self):
        try:
            logging.info('Converting Markdown to PDF using md2pdf')
            # Implement md2pdf conversion logic, placeholder in this example
            self.output_file = self.markdown_file.replace('.md', '.pdf')
            logging.info('Converted: %s to %s', self.markdown_file, self.output_file)
            return self.output_file
        except Exception as e:
            logging.error('Error during md2pdf conversion: %s', e)
            return None

    def markdown_weasyprint(self):
        try:
            logging.info('Converting Markdown to PDF using WeasyPrint')
            html = markdown(open(self.markdown_file).read())
            pdf = HTML(string=html)
            with NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                pdf.write_pdf(temp_pdf)
                self.output_file = temp_pdf.name
            logging.info('Converted: %s to %s', self.markdown_file, self.output_file)
            return self.output_file
        except Exception as e:
            logging.error('Error during WeasyPrint conversion: %s', e)
            return None

    def generate_pdf(self):
        md2pdf_result = self.md2pdf()
        weasyprint_result = self.markdown_weasyprint()
        return md2pdf_result, weasyprint_result

# Example Usage
if __name__ == '__main__':
    generator = PDFGenerator('turbulence_conformance_spec_v1_draft.md')
    md2pdf_output, weasyprint_output = generator.generate_pdf()
    if md2pdf_output:
        print(f'MD2PDF Output: {md2pdf_output}')
    if weasyprint_output:
        print(f'WeasyPrint Output: {weasyprint_output}')
