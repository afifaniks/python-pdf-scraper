import pdftotext
from six.moves.urllib.request import urlopen
import io

def get_pdf_content(url):
    '''
    This function fetches PDF and prints contents
    :param url: PDF URL
    :return: None
    '''
    remote_file = urlopen(url).read()
    memory_file = io.BytesIO(remote_file)

    pdf = pdftotext.PDF(memory_file)

    # Iterate over all the pages
    for page in pdf:
        print(page)
        # Uncomment to save text
        # with open("out.txt", "a") as myfile:
        #     myfile.write(page)

url = 'https://www.utc.wa.gov/regulatedIndustries/utilities/Documents/2019%20Avista%20Corporation.pdf'
get_pdf_content(url)