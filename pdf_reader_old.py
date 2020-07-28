import PyPDF2
import requests
import io

def get_pdf_content(url):
    '''
    :param url: PDF URL
    :return: Nothing
    '''
    r = requests.get(url)
    file = io.BytesIO(r.content)

    read_pdf = PyPDF2.PdfFileReader(file)
    number_of_pages = read_pdf.getNumPages()

    for i in range(number_of_pages):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        print(page_content)

url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
get_pdf_content(url)



