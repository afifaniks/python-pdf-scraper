import pdftotext
from six.moves.urllib.request import urlopen
import io

def get_pdf_content(url, file_name):
    '''
    This function fetches PDF and prints contents
    :param url: PDF URL
    :return: None
    '''
    print("Downloading...")
    remote_file = urlopen(url).read()
    memory_file = io.BytesIO(remote_file)

    pdf = pdftotext.PDF(memory_file)

    print("Saving File...")

    pg_ctr = 0;
    # Iterate over all the pages
    for page in pdf:
        print("Working on page", pg_ctr)
        pg_ctr += 1
        with open(file_name, "a") as myfile:
            myfile.write(page)

    print(file_name + " Saving Completed")

urls = ['''Write URLS here (comma separated)''']

file_names = ['''Write File names here (comma separated | maintain serial)''']


for url, file_name in zip(urls, file_names):
    print("Working on file: " + file_name)
    print("URL: " + url)

    get_pdf_content(url, file_name)